from src.stars.domain import Star


class StarColorCalculator:
    """Determines the color of a star based on its spectral class (currently white)."""

    def calculate_color(self, star: Star) -> str:
        """Returns the color for a given star."""
        return 'white'
