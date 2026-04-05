class StarSizeCalculator:
    """Calculates the visual marker size for a star based on its magnitude."""

    def __init__(self, base_size: float = 50.0, max_size: int = 100) -> None:
        """Initializes the size calculator with a base size value."""
        self.base_size = base_size
        self.max_size = max_size

    def calculate_size(self, magnitude: float) -> float:
        """Computes the marker size for a star."""
        if magnitude is None:
            return 2
        return min(max(self.base_size * 10 ** (-magnitude / 2.5), 2), self.max_size)
