from film import Film

class FilmMythologique(Film):
    def __init__(self, titre, realisateur):
        super().__init__(realisateur)  # Appel du constructeur de Film
        self.titre = titre  # Attribut spécifique à FilmMythologique

    def __str__(self):
        return f"FilmMythologique: {self.titre}, Réalisateur: {self.realisateur}"
