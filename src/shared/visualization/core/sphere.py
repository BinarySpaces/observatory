import math


class Sphere:
    """Celestial sphere model that converts astronomical coordinates to 3D points."""

    def __init__(self, radius: int = 100) -> None:
        """Initializes the sphere with a fixed radius."""
        self.radius = radius

    def to_cartesian(self, ra_deg: float, dec_deg: float) -> tuple[float, float, float]:
        """Converts equatorial coordinates (RA, Dec) to Cartesian coordinates (x, y, z)."""
        ra_rad = math.radians(ra_deg * 15)
        dec_rad = math.radians(dec_deg)

        x = self.radius * math.cos(dec_rad) * math.cos(ra_rad)
        y = self.radius * math.cos(dec_rad) * math.sin(ra_rad)
        z = self.radius * math.sin(dec_rad)

        return x, y, z
