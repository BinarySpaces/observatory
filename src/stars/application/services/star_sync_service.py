from src.stars.domain import (
    IGaiaDataProvider,
    ISimbadDataProvider,
    IStarCommands,
    IStarQueries,
)


class StarSyncService:
    """
    Coordinates the synchronization of star data from Gaia and SIMBAD into the local database.
    Fetches stars from Gaia, enriches them with names from SIMBAD, and saves or updates them.
    """

    def __init__(
        self,
        gaia_data_provider: IGaiaDataProvider,
        simbad_data_provider: ISimbadDataProvider,
        star_commands: IStarCommands,
        star_queries: IStarQueries
    ) -> None:
        """Initializes the sync service with required providers and repositories."""
        self.gaia_data_provider = gaia_data_provider
        self.simbad_data_provider = simbad_data_provider
        self.star_commands = star_commands
        self.star_queries = star_queries

    def sync_stars(self) -> None:
        """
        Fetches stars from Gaia, adds names from SIMBAD, and saves/updates them in the database.
        Prints status messages for each processed star.
        """
        stars = self.gaia_data_provider.get_stars()

        for star in stars.values():
            if self.star_queries.find(star.source_id):
                self.star_commands.update(star)
                print(f'Star {star.source_id} ({star.name}) updated.')
            else:
                star.name = self.simbad_data_provider.get_name_by_coordinates(
                    star.ra, star.dec
                )
                self.star_commands.save(star)
                print(f'Star {star.source_id} ({star.name}) saved.')
