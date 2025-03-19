from film import Film

class Festival:
    def __init__(self, nom: str):
        self.nom = nom
        self._film_gagnant = None  # Initialisation sans film gagnant

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nom: str):
        self._nom = nom

    @property
    def film_gagnant(self) -> Film:
        return self._film_gagnant

    def attribuer_film_gagnant(self, film: Film):
        self._film_gagnant = film  # Attribue un film gagnant au festival

    def obtenir_description_festival(self) -> str:
        if self._film_gagnant:
            return f"Le film réalisé par '{self._film_gagnant.realisateur}' a remporté le festival {self.nom} avec {self._film_gagnant.nombre_oscars} Oscar(s)."
        else:
            return f"Aucun film n'a été désigné gagnant pour le festival {self.nom}."