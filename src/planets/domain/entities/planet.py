class Planet:

    def __init__(self, name, orbital_period, mass):
        self.name = name
        self.orbital_period = orbital_period
        self.mass = mass

    def __repr__(self):
        return (
            f'Planet(name={self.name}, '
            f'orbital_period={self.orbital_period}, '
            f'mass={self.mass}'
        )
