class BaseRepository:
    """Base class for database repositories, handling connection and table creation."""

    def __init__(self, conn) -> None:
        """Initializes the repository, creates the stars table if it does not exist."""
        self.conn = conn
        self.create_stars_table()

    def create_stars_table(self) -> None:
        """Creates the 'stars' table with the required schema."""
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS stars (
                source_id BIGINT PRIMARY KEY,
                ra DOUBLE PRECISION NOT NULL,
                dec DOUBLE PRECISION NOT NULL,
                parallax DOUBLE PRECISION,
                phot_g_mean_mag DOUBLE PRECISION,
                name VARCHAR(255)
            );
        """)
        self.conn.commit()
        cur.close()

    def close(self) -> None:
        """Closes the database connection if it is still open."""
        if self.conn and not self.conn.closed:
            self.conn.close()
            self.conn = None
