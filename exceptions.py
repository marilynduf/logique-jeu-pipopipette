
class ErreurPositionCoup(Exception):

    def __init__(self, valeur):
        self.valeur = valeur

    def __str__(self):
        return repr(self.valeur)


class ErreurValeurTropGrande(ErreurPositionCoup):
    pass


class ErreurOrientation(ErreurPositionCoup):
    pass


class ErreurHorsLimites(ErreurPositionCoup):
    pass


class ErreurDejaJouee(ErreurPositionCoup):
    pass