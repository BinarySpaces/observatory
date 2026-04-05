from src.stars.domain import Star, IStarCommands
from src.stars.infrastructure.repositories import BaseRepository


class StarCommands(BaseRepository, IStarCommands):
    """Implements write operations (INSERT, UPDATE, DELETE) on the stars table."""

    def save(self, star: Star) -> None:
        """Inserts a new star into the database. Does nothing if the source_id already exists."""
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO stars (
                    source_id, ra, dec, parallax, phot_g_mean_mag, name
                )
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (source_id) DO NOTHING
        """, (
            star.source_id,
            star.ra,
            star.dec,
            star.parallax,
            star.phot_g_mean_mag,
            star.name
            ))
        self.conn.commit()
        cur.close()

    def update(self, star: Star) -> None:
        """Updates an existing star's data (excluding source_id)."""
        cur = self.conn.cursor()
        cur.execute("""
            UPDATE stars
            SET ra = %s, dec = %s, parallax = %s, phot_g_mean_mag = %s
            WHERE source_id = %s
        """, (
            star.ra,
            star.dec,
            star.parallax,
            star.phot_g_mean_mag,
            star.source_id
        ))
        self.conn.commit()
        cur.close()

    def delete(self, source_id: int) -> None:
        """Deletes a star by its Gaia source_id."""
        cur = self.conn.cursor()
        cur.execute("DELETE FROM stars WHERE source_id = %s", (source_id,))
        self.conn.commit()
        cur.close()

    def delete_all(self) -> None:
        """Deletes all stars from the table."""
        cur = self.conn.cursor()
        cur.execute("DELETE FROM stars")
        self.conn.commit()
        cur.close()
