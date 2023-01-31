# class MarimbaHitList:
#     def __init__(self, list):
#         self.degree =

class MarimbaHit:
    def __init__(self, degree, velocity, onset):
        self.degree = degree
        self.velocity = velocity
        self.onset = round(onset, 3)

    def __str__(self):
        return "{}, {}".format(self.degree, self.onset)
