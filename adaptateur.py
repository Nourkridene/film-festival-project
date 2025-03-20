from film_mythologique import FilmMythologique
from aventure import Aventure

class AdaptateurFilmAventure(Aventure):
    def __init__(self, film: FilmMythologique, hero, place: str, year: int):
        super().__init__(hero, place, year)  # Initialise une aventure
        self.film = film  # Associe un film mythologique

    def __str__(self):
        return f"Film: {self.film.titre}, Lieu: {self.place}, Année: {self.year}, Météo: {self.weather}"
