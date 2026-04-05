import astropy.units as u
from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
from typing import Optional

from src.stars.domain import ISimbadDataProvider


class SimbadDataProvider(ISimbadDataProvider):
    """Resolves astronomical object names using the SIMBAD database."""

    def get_name_by_coordinates(self, ra: float, dec: float) -> Optional[str]:
        """Searches SIMBAD for an object at the given equatorial coordinates."""
        result = Simbad.query_region(
            SkyCoord(ra, dec, unit='deg'), radius=1 * u.arcsec
        )

        if result and len(result) > 0 and 'main_id' in result.colnames:
            return result[0]['main_id']

        return None
