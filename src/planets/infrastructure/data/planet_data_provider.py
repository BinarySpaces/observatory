from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive

from src.planets.domain.repositories.iplanet_data_provider import IPlanetRepository
from src.planets.domain.entities.planet import Planet


class PlanetRepository(IPlanetRepository):

    def get_planets_by_name(self, name, limit):
        table = NasaExoplanetArchive.query_criteria(
            table="exoplanets",
            select="pl_name, pl_orbper, pl_bmassj",
            limit=limit
        )

        planets = {}
        for row in table:
            planet = Planet(
                name=row['pl_name'],
                orbital_period=row['pl_orbper'],
                mass=row['pl_bmassj']
            )
            planets[planet.name] = planet
        return planets
