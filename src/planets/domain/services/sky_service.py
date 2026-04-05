from src.planets.domain.repositories.iplanet_data_provider import IPlanetRepository


class SkyService:

    def __init__(self, planet_repository: IPlanetRepository):
        self._planet_repository = planet_repository

    def get_planets(self, name=None, limit=1):
        return self._planet_repository.get_planets_by_name(name, limit)
