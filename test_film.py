import pytest
from exceptions import NombreOscarsNegatifError, FilmSansRealisateurError
from film import Film  # Assurez-vous que le fichier Film est bien importé
from film_mythologique import FilmMythologique  # Import de la classe FilmMythologique
from aventure import Aventure  # Import de la classe Aventure
from adaptateur import AdaptateurFilmAventure
# Test de la création d'un film avec un réalisateur valide
def test_creation_film():
    film = Film("Quentin Tarantino")
    assert film.realisateur == "Quentin Tarantino"
    assert film.nombre_oscars == 0

# Test de l'ajout d'un Oscar
def test_ajouter_oscar():
    film = Film("Quentin Tarantino")
    film.ajouter_oscar()
    assert film.nombre_oscars == 1

# Test de l'exception pour un réalisateur vide
def test_creation_film_sans_realisateur():
    with pytest.raises(FilmSansRealisateurError):
        Film("")

# Test de l'exception pour un nombre d'Oscars négatif
def test_set_nombre_oscars_negatif():
    film = Film("Quentin Tarantino")
    with pytest.raises(NombreOscarsNegatifError):
        film.nombre_oscars = -1


# Test de la création d'un film mythologique
def test_creation_film_mythologique():
    film_mythologique = FilmMythologique("Les aventures d'Hercule", "John Doe")
    assert film_mythologique.titre == "Les aventures d'Hercule"
    assert film_mythologique.realisateur == "John Doe"

# Test de l'adaptateur qui associe un film mythologique à une aventure
def test_adaptateur_film_aventure():
    class PersonnageMythologique:
        def __init__(self, nom, mood):
            self.nom = nom
            self.mood = mood

        def __str__(self):
            return f"{self.nom} ({self.mood})"

    hero = PersonnageMythologique("Hercule", "Happy")

    # Création du film mythologique
    film_mythologique = FilmMythologique("Les aventures d'Hercule", "John Doe")

    # Création de l'adaptateur qui associe le film à une aventure
    adaptateur = AdaptateurFilmAventure(film_mythologique, hero, "Olympus", -750)

    # Tests des attributs de l'adaptateur
    assert adaptateur.place == "Olympus"
    assert adaptateur.year == -750
    assert adaptateur.weather == "sunny"

    # Test de la modification de la météo via l'adaptateur
    adaptateur.weather = "rainy"
    assert adaptateur.weather == "rainy"