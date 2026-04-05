from abc import ABC, abstractmethod


class IGalaxyRepository(ABC):

    @abstractmethod
    def create_galaxies_table(self):
        pass

    @abstractmethod
    def get_galaxies(self, source_id):
        pass

    @abstractmethod
    def get_galaxy(self, source_id):
        pass

    @abstractmethod
    def save_galaxy(self, galaxy):
        pass

    @abstractmethod
    def update_galaxy(self, galaxy):
        pass

    @abstractmethod
    def delete_galaxy(self, galaxy):
        pass
