from astroquery.gaia import Gaia

from src.stars.domain import Star, IGaiaDataProvider


class GaiaDataProvider(IGaiaDataProvider):
    """
    Fetches star data from the Gaia Archive using synchronous TAP queries.
    Implements pagination via OFFSET.
    """

    def get_stars(self, offset: int = 0) -> list[Star]:
        """Retrieves a batch of stars from Gaia."""
        query = f"""
        SELECT TOP 2000 source_id, ra, dec, parallax, phot_g_mean_mag
        FROM gaiadr3.gaia_source
        WHERE phot_g_mean_mag < 6
        AND parallax IS NOT NULL
        ORDER BY parallax DESC, phot_g_mean_mag
        OFFSET {offset}
        """
        job = Gaia.launch_job(query)
        result_table = job.get_results()

        stars = []
        for row in result_table:
            star = Star(
                source_id=int(row['source_id']),
                ra=float(row['ra']),
                dec=float(row['dec']),
                parallax=float(row['parallax']),
                phot_g_mean_mag=float(row['phot_g_mean_mag'])
            )
            stars.append(star)

        return stars
