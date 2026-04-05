class Star:
    """Domain entity representing a star with its astronomical properties."""

    def __init__(self, source_id, ra, dec, parallax, phot_g_mean_mag, name=None) -> None:
        """Initializes a Star instance."""
        self.source_id = source_id
        self.ra = ra
        self.dec = dec
        self.parallax = parallax
        self.phot_g_mean_mag = phot_g_mean_mag
        self.name = name
