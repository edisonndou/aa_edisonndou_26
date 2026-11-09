"""Hash-table deduplication, independent of files and console output."""

from dataclasses import dataclass
from itertools import product as combinations


@dataclass(frozen=True)
class Product:
    product_id: str
    brand: str
    model: str
    description: str
    supplier_id: str

    def __post_init__(self):
        for field in ("product_id", "brand", "model", "description", "supplier_id"):
            if not isinstance(getattr(self, field), str):
                raise ValueError(field + " must be a string")
        if not self.product_id.strip() or not self.supplier_id.strip():
            raise ValueError("product_id and supplier_id must not be blank")


@dataclass(frozen=True)
class DuplicateGroup:
    products: tuple
    confidence: str
    reason: str


@dataclass(frozen=True)
class DeduplicationResult:
    groups: tuple
    unique_products: tuple


class InventoryDeduplicator:
    """The injected callable maps a Product to immutable Attributes."""

    def __init__(self, normalize):
        self._normalize = normalize

    def find_duplicates(self, inventory, incoming):
        inventory, incoming = tuple(inventory), tuple(incoming)
        buckets = {}
        incoming_keys = {}
        seen_ids = set()
        for records, is_new in ((inventory, False), (incoming, True)):
            for record in records:
                if record.product_id in seen_ids:
                    raise ValueError("Repeated product_id: " + record.product_id)
                seen_ids.add(record.product_id)
                key = self._normalize(record)
                buckets.setdefault(key, []).append(record)
                if is_new:
                    incoming_keys[key] = None

        groups = []
        matched = set()
        for key, records in buckets.items():
            if key in incoming_keys and len(records) > 1:
                groups.append(DuplicateGroup(
                    tuple(records), "HIGH", "All normalized attributes match."
                ))
                matched.add(key)

        # None is a lookup wildcard; () means an attribute was not extracted.
        # Each signature has four projections, avoiding an all-products scan.
        index = {}
        for key in buckets:
            if not key.brand or not key.model:
                continue
            for size, color in combinations((key.sizes, None), (key.colors, None)):
                projection = (key.brand, key.model, size, color)
                index.setdefault(projection, []).append(key)

        emitted = set()
        for key in incoming_keys:
            if not key.brand or not key.model:
                continue
            size_options = (key.sizes, ()) if key.sizes else (None,)
            color_options = (key.colors, ()) if key.colors else (None,)
            for size, color in combinations(size_options, color_options):
                candidates = index.get((key.brand, key.model, size, color), ())
                for other in candidates:
                    if key == other:
                        continue
                    pair = frozenset((key, other))
                    if pair in emitted:
                        continue
                    emitted.add(pair)
                    missing_count = sum((key.sizes != other.sizes, key.colors != other.colors))
                    groups.append(DuplicateGroup(
                        tuple(buckets[other] + buckets[key]),
                        "MEDIUM" if missing_count == 1 else "LOW",
                        "Brand/model match; no known size/color conflicts; "
                        + str(missing_count) + " attribute(s) missing on one side.",
                    ))
                    matched.update((key, other))

        matched_ids = {
            record.product_id for key in matched for record in buckets[key]
        }
        unique = tuple(record for record in incoming if record.product_id not in matched_ids)
        return DeduplicationResult(tuple(groups), unique)
