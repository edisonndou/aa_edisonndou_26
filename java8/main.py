"""JSON input and command-line output for the supply-chain assignment."""

import argparse
from dataclasses import asdict
import json
from pathlib import Path
import sys

if __package__:
    from .deduplication import InventoryDeduplicator, Product
    from .normalization import AttributeNormalizer
else:
    from deduplication import InventoryDeduplicator, Product
    from normalization import AttributeNormalizer


def load_products(path):
    with path.open(encoding="utf-8-sig") as stream:
        document = json.load(stream)
    if not isinstance(document, dict):
        raise ValueError("Input must be an object with inventory and incoming arrays")
    result = []
    required = {"product_id", "brand", "model", "description", "supplier_id"}
    for name in ("inventory", "incoming"):
        records = document.get(name)
        if not isinstance(records, list):
            raise ValueError(name + " must be an array")
        products = []
        for position, record in enumerate(records, 1):
            if not isinstance(record, dict) or set(record) != required:
                raise ValueError(
                    "{} record {} must contain exactly: {}".format(
                        name, position, ", ".join(sorted(required))
                    )
                )
            products.append(Product(**record))
        result.append(products)
    return result


def print_report(result):
    print("DUPLICATE GROUPS FOUND:")
    if not result.groups:
        print("None")
    for number, group in enumerate(result.groups, 1):
        representative = group.products[0]
        print("Group {} ({} {}):".format(
            number, representative.brand, representative.model
        ))
        for record in group.products:
            print("-{} (Supplier: {})".format(record.product_id, record.supplier_id))
        print("Confidence: " + group.confidence)
        if group.confidence != "HIGH":
            print("Reason: " + group.reason)
        print()
    print("NEW UNIQUE PRODUCTS:")
    if not result.unique_products:
        print("None")
    for record in result.unique_products:
        print("-{} ({} {})".format(record.product_id, record.brand, record.model))


def main():
    parser = argparse.ArgumentParser(description="Find inventory duplicates using hash tables.")
    parser.add_argument(
        "input", nargs="?", type=Path,
        default=Path(__file__).with_name("example.json"),
        help="JSON document containing inventory and incoming arrays",
    )
    parser.add_argument("--json", action="store_true", help="Print structured JSON output")
    args = parser.parse_args()
    try:
        inventory, incoming = load_products(args.input)
        result = InventoryDeduplicator(AttributeNormalizer()).find_duplicates(inventory, incoming)
    except (OSError, ValueError) as error:
        print("Error: " + str(error), file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(asdict(result), indent=2, ensure_ascii=False))
    else:
        print_report(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
