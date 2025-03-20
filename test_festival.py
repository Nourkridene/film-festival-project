import pytest
from film import Film
from festival import Festival


def test_festival_sans_film_gagnant():
    """ Vérifie que la description du festival est correcte quand aucun film n'a gagné. """
    festival = Festival("Sundance")
    assert festival.obtenir_description_festival() == "Aucun film n'a été désigné gagnant pour le festival Sundance."


def test_attribuer_film_gagnant():
    """ Vérifie qu'un film peut être attribué comme gagnant du festival. """
    film = Film("Martin Scorsese")
    festival = Festival("Cannes")

    festival.attribuer_film_gagnant(film)
    assert festival.film_gagnant == film
    assert festival.obtenir_description_festival() == "Le film réalisé par 'Martin Scorsese' a remporté le festival Cannes avec 0 Oscar(s)."


def test_attribuer_plusieurs_films_gagnants():
    """ Vérifie qu'on peut changer le film gagnant plusieurs fois. """
    film1 = Film("Stanley Kubrick")
    film2 = Film("Ridley Scott")

    festival = Festival("Venise")

    festival.attribuer_film_gagnant(film1)
    assert festival.obtenir_description_festival() == "Le film réalisé par 'Stanley Kubrick' a remporté le festival Venise avec 0 Oscar(s)."

    festival.attribuer_film_gagnant(film2)
    assert festival.obtenir_description_festival() == "Le film réalisé par 'Ridley Scott' a remporté le festival Venise avec 0 Oscar(s)."


def test_obtenir_description_festival_apres_ajout_oscar():
    """ Vérifie que la description est mise à jour après ajout d'un Oscar. """
    film = Film("Quentin Tarantino")
    festival = Festival("Toronto")

    festival.attribuer_film_gagnant(film)
    assert festival.obtenir_description_festival() == "Le film réalisé par 'Quentin Tarantino' a remporté le festival Toronto avec 0 Oscar(s)."

    film.ajouter_oscar()
    assert festival.obtenir_description_festival() == "Le film réalisé par 'Quentin Tarantino' a remporté le festival Toronto avec 1 Oscar(s)."


def test_nom_festival():
    """ Vérifie que le nom du festival peut être défini et récupéré. """
    festival = Festival("Berlin")
    assert festival.nom == "Berlin"

    festival.nom = "Toronto"
    assert festival.nom == "Toronto"


def test_festival_nom_vide():
    """ Vérifie que le festival accepte un nom vide (optionnel selon la logique métier). """
    festival = Festival("")
    assert festival.nom == ""


def test_attribuer_film_null():
    """ Vérifie qu'un festival peut ne pas avoir de film gagnant. """
    festival = Festival("Sundance")
    assert festival.film_gagnant is None


def test_nom_festival_apres_modification():
    """ Vérifie que le setter du nom fonctionne correctement. """
    festival = Festival("Berlin")
    assert festival.nom == "Berlin"

    festival.nom = "Locarno"
    assert festival.nom == "Locarno"


### NOUVEAUX TESTS POUR AUGMENTER LA COUVERTURE 📈 ###

def test_retirer_film_gagnant():
    """ Vérifie que l'on peut retirer un film gagnant d'un festival. """
    film = Film("Christopher Nolan")
    festival = Festival("Oscars")

    festival.attribuer_film_gagnant(film)
    assert festival.film_gagnant == film

    festival.attribuer_film_gagnant(None)  # On enlève le film gagnant
    assert festival.film_gagnant is None
    assert festival.obtenir_description_festival() == "Aucun film n'a été désigné gagnant pour le festival Oscars."





def test_film_gagnant_avec_plusieurs_oscars():
    """ Vérifie que la description s'adapte correctement quand un film gagne plusieurs Oscars. """
    film = Film("Steven Spielberg")
    festival = Festival("Golden Globes")

    festival.attribuer_film_gagnant(film)
    assert "0 Oscar(s)" in festival.obtenir_description_festival()

    film.ajouter_oscar()
    film.ajouter_oscar()
    film.ajouter_oscar()
    assert "3 Oscar(s)" in festival.obtenir_description_festival()


def test_film_gagnant_changement_multiple():
    """ Vérifie qu'un festival peut attribuer plusieurs fois un film différent comme gagnant sans erreur. """
    film1 = Film("Peter Jackson")
    film2 = Film("James Cameron")
    film3 = Film("Francis Ford Coppola")

    festival = Festival("BAFTA")

    festival.attribuer_film_gagnant(film1)
    assert "Peter Jackson" in festival.obtenir_description_festival()

    festival.attribuer_film_gagnant(film2)
    assert "James Cameron" in festival.obtenir_description_festival()

    festival.attribuer_film_gagnant(film3)
    assert "Francis Ford Coppola" in festival.obtenir_description_festival()
