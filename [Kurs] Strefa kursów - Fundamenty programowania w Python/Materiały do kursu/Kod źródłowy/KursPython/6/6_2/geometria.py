PHI = 1.618033988


def oblicz_pi():
    pi = (6 / 5) * PHI ** 2
    return round(pi, 2)


class Okrag:
    def __init__(self, promien):
        self.promien = promien

    def obwod(self):
        return 2 * oblicz_pi() * self.promien
