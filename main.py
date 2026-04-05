import json
import os
import sys

from dotenv import load_dotenv
import psycopg2

from src.shared.visualization import SkyRenderer
from src.stars.application import StarSyncService
from src.stars.infrastructure import (
    GaiaDataProvider,
    SimbadDataProvider,
    StarCommands,
    StarQueries
)
from src.telescopes.application import TelescopeService
from src.telescopes.infrastructure import LCOTelescopeAPI


load_dotenv()


def main() -> None:
    """Main entry point for the application."""
    args = sys.argv[1:]
    mode = 'load' if args and args[0] == 'l' else 'normal'

    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    conn = psycopg2.connect(config['db_connection_string'])

    star_queries = StarQueries(conn)

    if mode == 'load':
        print('Loading data')

        star_commands = StarCommands(conn)
        gaia_data_provider = GaiaDataProvider()
        simbad_data_provider = SimbadDataProvider()
        stars_sync_service = StarSyncService(
            gaia_data_provider,
            simbad_data_provider,
            star_commands,
            star_queries
        )

        stars_sync_service.sync_stars()
    else:
        print('Using DB')

        stars = star_queries.get_all()

        telescope_service = TelescopeService(
                LCOTelescopeAPI(
                    os.getenv('LCO_TELESCOPE_API_TOKEN'),
                    os.getenv('PROPOSAL_ID')
                )
            )

        sky_renderer = SkyRenderer()
        sky_renderer.add_stars(stars)
        sky_renderer.register_callback(telescope_service.point_to_star)
        sky_renderer.show()

    conn.close()


if __name__ == '__main__':
    main()
