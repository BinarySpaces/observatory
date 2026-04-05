class Galaxy:

    def __init__(self, objid, ra, dec, redshift):
        self.id = objid
        self.ra = ra
        self.dec = dec
        self.redshift = redshift

    def __repr__(self):
        return (
            f'Galaxy(id={self.id}, '
            f'ra={self.ra}, '
            f'dec={self.dec}, '
            f'redshift={self.redshift})'
        )
