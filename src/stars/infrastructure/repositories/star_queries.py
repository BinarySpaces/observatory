from typing import Optional

from src.stars.domain import Star, IStarQueries
from src.stars.infrastructure.repositories import BaseRepository


class StarQueries(BaseRepository, IStarQueries):
    """Implements read operations (SELECT) on the stars table."""

    def get_all(self, offset: int = None, limit: int = None) -> list[Star]:
        """Retrieves a paginated list of all stars, ordered by source_id."""
        cur = self.conn.cursor()
        cur.execute("""
            SELECT source_id, ra, dec, parallax, phot_g_mean_mag, name
            FROM stars
            ORDER BY source_id
            OFFSET %s LIMIT %s
        """, (offset, limit))
        rows = cur.fetchall()
        cur.close()

        return [Star(*row) for row in rows]

    def find(self, source_id: int) -> Optional[Star]:
        """Finds a single star by its Gaia source_id."""
        cur = self.conn.cursor()
        cur.execute("""
            SELECT source_id, ra, dec, parallax, phot_g_mean_mag, name
            FROM stars
            WHERE source_id = %s
        """, (source_id,))
        row = cur.fetchone()
        cur.close()

        return Star(*row) if row else None
