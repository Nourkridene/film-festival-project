from exceptions import NombreOscarsNegatifError, FilmSansRealisateurError

class Film:
    def __init__(self, realisateur, festival=None):
        if not realisateur:
            raise FilmSansRealisateurError("Le réalisateur ne peut pas être vide.")
        self.realisateur = realisateur
        self._nombre_oscars = 0
        self._festival = festival  # Plus de setter pour éviter la relation bidirectionnelle

    @property
    def nombre_oscars(self):
        return self._nombre_oscars

    @nombre_oscars.setter
    def nombre_oscars(self, nombre_oscars):
        if nombre_oscars < 0:
            raise NombreOscarsNegatifError("Le nombre d'Oscars ne peut pas être négatif.")
        self._nombre_oscars = nombre_oscars

    @property
    def festival(self):
        return self._festival

    def ajouter_oscar(self):
        self._nombre_oscars += 1
