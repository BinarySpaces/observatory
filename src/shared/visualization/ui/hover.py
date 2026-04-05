from src.stars.domain import Star


class HoverFormatter:
    """Formats HTML tooltips for stars displayed in the Plotly chart."""

    def format(self, star: Star) -> str:
        '''Generates an HTML tooltip with star information.'''
        name = star.name if star.name else 'Unnamed star'

        if star.parallax and star.parallax > 0:
            distance_pc = 1000.0 / star.parallax
            distance_ly = distance_pc * 3.26
            dist_str = f'{distance_ly:.1f} ly'
        else:
            dist_str = 'unknown'

        hover_text = f'''
        <b>{name}</b><br>
        RA: {star.ra:.4f}°<br>
        Dec: {star.dec:.4f}°<br>
        Magnitude: {star.phot_g_mean_mag:.2f}<br>
        Distance: {dist_str}
        '''

        return hover_text
