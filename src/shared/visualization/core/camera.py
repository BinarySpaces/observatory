from typing import Any


class Camera:
    """Controls the 3D camera view for the star visualization scene."""

    def __init__(self) -> None:
        """Initializes the camera with default position and orientation."""
        self.eye = {"x": 0, "y": 0, "z": 0}
        self.center = {"x": 0, "y": 0, "z": 0}
        self.up = {"x": 0, "y": 0, "z": 1}

    def get_layout(self) -> dict[str, Any]:
        """Returns the Plotly layout configuration for the 3D scene."""
        return {
            'xaxis': {'visible': False},
            'yaxis': {'visible': False},
            'zaxis': {'visible': False},
            'camera': {
                'eye': self.eye,
                'center': self.center,
                'up': self.up
            },
            'bgcolor': 'black'
        }
