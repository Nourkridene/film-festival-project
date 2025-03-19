from film import Film
from festival import Festival  # Assurez-vous que le fichier Festival est bien importé


def test_obtenir_description_festival():
    film = Film("Quentin Tarantino")
    festival = Festival("Cannes", film)

    # Test avec 0 Oscars
    assert festival.obtenir_description_festival() == 'Le film réalisé par "Quentin Tarantino" a remporté le festival Cannes avec 0 Oscar(s).'

    # Ajout d'un Oscar et test à nouveau
    film.ajouter_oscar()
    assert festival.obtenir_description_festival() == 'Le film réalisé par "Quentin Tarantino" a remporté le festival Cannes avec 1 Oscar(s).'
