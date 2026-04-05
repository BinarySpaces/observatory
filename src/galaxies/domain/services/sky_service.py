from src.galaxies.domain.repositories.igalaxy_data_provider import IGalaxyRepository


class SkyService:

    def __init__(self, galaxy_repository: IGalaxyRepository):
        self._galaxy_repository = galaxy_repository

    def get_galaxies(self, ra=0.0, dec=0.0, radius=1.0):
        return self._galaxy_repository.get_galaxies_by_region(ra, dec, radius)
