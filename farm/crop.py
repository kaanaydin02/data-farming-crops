# pylint: disable=too-few-public-methods
"""Crop module — shared parent class for all crops."""


class Crop:
    """Base class for all crops, storing grain count and ripeness logic."""

    def __init__(self):
        self.grains = 0

    def ripe(self):
        """Return True if the crop has at least 15 grains."""
        return self.grains >= 15
