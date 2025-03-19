import pytest
from exceptions import NombreOscarsNegatifError, FilmSansRealisateurError
from film import Film  # Assurez-vous que le fichier Film est bien importé

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
