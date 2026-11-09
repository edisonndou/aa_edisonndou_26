"""Normalize supplier names and extract size/color from descriptions."""

from dataclasses import dataclass
from decimal import Decimal
import re
import unicodedata


def normalized_text(value):
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    return "".join(char for char in decomposed if char.isalnum())


@dataclass(frozen=True)
class Attributes:
    brand: str
    model: str
    sizes: tuple
    colors: tuple


class AttributeNormalizer:
    """Callable extraction policy; alias tables own the recognized vocabulary."""

    COLOR_ALIASES = {
        "black": "black", "blk": "black", "bk": "black",
        "white": "white", "wht": "white", "wh": "white",
        "blue": "blue", "blu": "blue", "bl": "blue",
        "red": "red", "rd": "red", "green": "green", "grn": "green",
        "gray": "gray", "grey": "gray", "gry": "gray",
        "gold": "gold", "gld": "gold", "silver": "silver", "slv": "silver",
        "yellow": "yellow", "ylw": "yellow", "pink": "pink",
        "purple": "purple", "violet": "purple", "orange": "orange",
        "brown": "brown", "beige": "beige", "navy": "navy",
    }
    APPAREL_ALIASES = {
        "xxs": "xxs", "xs": "xs", "s": "s", "small": "s",
        "m": "m", "medium": "m", "l": "l", "large": "l",
        "xl": "xl", "xxl": "xxl", "2xl": "xxl",
        "xxxl": "xxxl", "3xl": "xxxl",
    }
    UNIT_ALIASES = {
        "mb": ("storage_mb", Decimal(1)),
        "gb": ("storage_mb", Decimal(1000)),
        "gigabyte": ("storage_mb", Decimal(1000)),
        "gigabytes": ("storage_mb", Decimal(1000)),
        "tb": ("storage_mb", Decimal(1000000)),
        "terabyte": ("storage_mb", Decimal(1000000)),
        "terabytes": ("storage_mb", Decimal(1000000)),
        "mm": ("length_mm", Decimal(1)),
        "cm": ("length_mm", Decimal(10)),
        "in": ("length_mm", Decimal("25.4")),
        "inch": ("length_mm", Decimal("25.4")),
        "inches": ("length_mm", Decimal("25.4")),
        '"': ("length_mm", Decimal("25.4")),
        "ml": ("volume_ml", Decimal(1)),
        "l": ("volume_ml", Decimal(1000)),
        "liter": ("volume_ml", Decimal(1000)),
        "litre": ("volume_ml", Decimal(1000)),
        "g": ("mass_g", Decimal(1)),
        "kg": ("mass_g", Decimal(1000)),
    }

    def __init__(self):
        units = "|".join(re.escape(unit) for unit in sorted(
            self.UNIT_ALIASES, key=len, reverse=True
        ))
        self._measurement = re.compile(
            r"(?<![\w.])([0-9]+(?:[.,][0-9]+)?)\s*-?\s*("
            + units + r")(?!\w)"
        )
        apparel = "|".join(self.APPAREL_ALIASES)
        self._apparel = re.compile(r"\b(?:size\s*[:=-]?\s*)?(" + apparel + r")\b")
        self._labeled_size = re.compile(r"\bsize\s*[:=-]?\s*([0-9]+(?:[.,][0-9]+)?)\b")

    def __call__(self, product):
        description = product.description.replace("\u2033", '"').replace("\u201d", '"')
        description = unicodedata.normalize("NFKC", description).casefold()
        sizes = set()
        for match in self._measurement.finditer(description):
            dimension, multiplier = self.UNIT_ALIASES[match.group(2)]
            amount = Decimal(match.group(1).replace(",", ".")) * multiplier
            sizes.add(dimension + ":" + format(amount.normalize(), "f"))

        # Avoid treating a unit in a measured quantity as an apparel size.
        remaining = self._measurement.sub(" ", description)
        for match in self._apparel.finditer(remaining):
            sizes.add("apparel:" + self.APPAREL_ALIASES[match.group(1)])
        for match in self._labeled_size.finditer(remaining):
            amount = Decimal(match.group(1).replace(",", "."))
            sizes.add("size:" + format(amount.normalize(), "f"))

        colors = {
            self.COLOR_ALIASES[token]
            for token in re.findall(r"\b[a-z]+\b", description)
            if token in self.COLOR_ALIASES
        }
        return Attributes(
            normalized_text(product.brand), normalized_text(product.model),
            tuple(sorted(sizes)), tuple(sorted(colors)),
        )
