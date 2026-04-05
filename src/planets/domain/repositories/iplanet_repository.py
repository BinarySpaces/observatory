from abc import ABC, abstractmethod


class IPlanetRepository(ABC):

    @abstractmethod
    def create_planets_table(self):
        pass

    @abstractmethod
    def get_planets(self, source_id):
        pass

    @abstractmethod
    def get_planet(self, source_id):
        pass

    @abstractmethod
    def save_planet(self, planet):
        pass

    @abstractmethod
    def update_planet(self, planet):
        pass

    @abstractmethod
    def delete_planet(self, planet):
        pass
