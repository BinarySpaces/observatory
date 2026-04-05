from abc import ABC, abstractmethod


class IPlanetRepository(ABC):

    @abstractmethod
    def get_planets_by_name(self, name, limit):
        pass
