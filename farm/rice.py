"""Rice crop module."""
from farm.crop import Crop


class Rice(Crop):
    """A rice crop."""

    def water(self):
        """Add 5 grains to the crop."""
        self.grains += 5

    def transplant(self):
        """Add 10 grains to the crop."""
        self.grains += 10
