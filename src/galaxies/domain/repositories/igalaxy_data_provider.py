from abc import ABC, abstractmethod


class IGalaxyRepository(ABC):

    @abstractmethod
    def get_galaxies_by_region(self, ra, dec, radius):
        pass
