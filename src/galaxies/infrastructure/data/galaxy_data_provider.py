from astroquery.sdss import SDSS

from src.galaxies.domain.entities.galaxy import Galaxy
from src.galaxies.domain.repositories.igalaxy_data_provider import IGalaxyRepository


class GalaxyRepository(IGalaxyRepository):

    def get_galaxies_by_region(self, ra, dec, radius):
        query = f"""
        SELECT objid, ra, dec, z
        FROM specObj
        WHERE ra BETWEEN {ra - radius} AND {ra + radius}
          AND dec BETWEEN {dec - radius} AND {dec + radius}
        """
        result = SDSS.query_sql(query)
        print(result)

        galaxies = {}
        for row in result:
            galaxy = Galaxy(
                id=row['objid'],
                ra=row['ra'],
                dec=row['dec'],
                redshift=row['z']
            )
            galaxies[galaxy.id] = galaxy
        return galaxies


if __name__ == '__main__':
    obj = GalaxyRepository()
    print(obj.get_galaxies_by_region(ra=0.0, dec=0.0, radius=1.0))
