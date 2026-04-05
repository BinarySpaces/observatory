from typing import Callable, List, Optional

from dash import Dash, Input, Output, dcc, html
import plotly.graph_objects as go

from src.shared.visualization import (
    Camera,
    HoverFormatter,
    Sphere,
    StarColorCalculator,
    StarSizeCalculator,
)
from src.stars.domain import Star


class SkyRenderer:
    """
    Main class for rendering interactive 3D star map using Plotly and Dash.
    Handles star data storage, visualization, and click events.
    """

    def __init__(self) -> None:
        """Initializes the renderer with empty data containers and default settings."""
        self.sphere = Sphere()
        self.camera = Camera()
        self.size_calc = StarSizeCalculator()
        self.color_calc = StarColorCalculator()
        self.hover = HoverFormatter()
        self.callback = None

        self.x_coords = []
        self.y_coords = []
        self.z_coords = []
        self.sizes = []
        self.colors = []
        self.hover_texts = []
        self.ids = []
        self.customdata = []

    def register_callback(self, callback: Callable[[float, float], None]) -> None:
        """Registers a callback function to be called when a star is clicked."""
        self.callback = callback

    def add_stars(self, stars: List[Star]) -> None:
        """Adds a list of stars to the renderer's internal data storage."""
        for star in stars:
            self.add_star(star)

    def add_star(self, star: Star) -> None:
        """
        Adds a single star to the renderer's internal data storage.
        Converts coordinates to Cartesian and computes visual properties.
        """
        x, y, z = self.sphere.to_cartesian(star.ra, star.dec)
        size = self.size_calc.calculate_size(star.phot_g_mean_mag)
        color = self.color_calc.calculate_color(star)
        hover_text = self.hover.format(star)

        self.x_coords.append(x)
        self.y_coords.append(y)
        self.z_coords.append(z)
        self.sizes.append(size)
        self.colors.append(color)
        self.hover_texts.append(hover_text)
        self.ids.append(star.source_id)
        self.customdata.append([star.ra, star.dec])

    def build(self, title: str = 'Night sky') -> go.Figure:
        """Builds a Plotly 3D figure from the stored star data."""
        scatter = go.Scatter3d(
            x=self.x_coords,
            y=self.y_coords,
            z=self.z_coords,
            mode='markers',
            marker=dict(
                size=self.sizes,
                color=self.colors,
                opacity=0.9,
                symbol='circle'
            ),
            text=self.hover_texts,
            hoverinfo='text',
            ids=self.ids,
            customdata=self.customdata
        )
        # scatter.on_click(self.on_click)

        fig = go.Figure(data=[scatter])
        fig.update_layout(
            title=title,
            scene=self.camera.get_layout(),
            showlegend=False,
            margin=dict(l=0, r=0, t=30, b=0)
        )

        return fig

    # def on_click(self, trace, points, state):
    #     if points.point_inds:
    #         idx = points.point_inds[0]
    #         data = trace.customdata[idx]
    #         self.callback(data[0], data[1])

    def show(self, title: str = 'Night sky') -> None:
        """
        Launches a Dash web server to display the interactive star map.

        The function creates a Dash application with a full-screen 3D plot.
        Click events on stars are handled by the registered callback.
        """
        fig = self.build(title)

        fig.update_layout(
            autosize=True,
            height=800,
            margin=dict(l=0, r=0, t=30, b=0)
            )

        app = Dash(__name__)
        app.layout = html.Div([
            dcc.Graph(
                id='sky-graph',
                figure=fig,
                config={'clickMode': 'event'},
                style={'height': '97vh', 'width': '100%'}
            )
        ])

        @app.callback(
            Output('sky-graph', 'figure'),
            Input('sky-graph', 'clickData'),
            prevent_initial_call=True
        )
        def handle_click(clickData: Optional[dict]) -> go.Figure:
            if clickData and self.callback:
                points = clickData['points'][0]
                customdata = points['customdata']
                self.callback(customdata[0], customdata[1])
            return fig

        app.run(debug=False, use_reloader=False)
