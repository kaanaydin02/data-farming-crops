"""Corn crop module."""
from farm.crop import Crop


class Corn(Crop):
    """A corn crop."""

    def water(self):
        """Add 10 grains to the crop."""
        self.grains += 10
