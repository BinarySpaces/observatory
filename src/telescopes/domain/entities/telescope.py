# class Telescope:

#     def __init__(self, name, dec_min, dec_max, ra_min, ra_max) -> None:
#         self.name = name
#         self.dec_min = dec_min
#         self.dec_max = dec_max
#         self.ra_min = ra_min
#         self.ra_max = ra_max

#     def can_see(self, ra, dec) -> bool:
#         if not self.dec_min < dec < self.dec_max:
#             return False

#         if self.ra_max > self.ra_min:
#             return self.ra_min <= ra <= self.ra_max
#         else:
#             return self.ra_min <= ra or ra <= self.ra_max
