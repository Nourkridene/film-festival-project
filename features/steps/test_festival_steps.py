from behave import given, when, then
from film import Film
from festival import Festival

# Étape 1 : Créer un festival nommé
@given(u'un festival nommé "{nom}"')
def step_given_un_festival(context, nom):
    context.festival = Festival(nom)

# Étape 2 : Attribuer un film gagnant sans Oscars à un festival
@when(u"j'attribue le film \"{titre}\" réalisé par \"{realisateur}\" comme gagnant")
def step_when_attribuer_film(context, titre, realisateur):
    film = Film(realisateur)  # Créer le film sans Oscars
    context.festival.attribuer_film_gagnant(film)  # Attribuer le film comme gagnant du festival

# Étape 3 : Attribuer un film gagnant avec des Oscars
@when(u"j'attribue le film \"{titre}\" réalisé par \"{realisateur}\" comme gagnant avec {oscars} Oscar(s)")
def step_when_attribuer_film_oscars(context, titre, realisateur, oscars):
    film = Film(realisateur)  # Créer le film sans Oscar
    film.nombre_oscars = int(oscars)  # Définir le nombre d'Oscars
    context.festival.attribuer_film_gagnant(film)  # Attribuer le film comme gagnant du festival

# Étape 4 : Attribuer un film vide avec 0 Oscar(s) à un festival
@when(u'aucun film n\'est attribué comme gagnant')
def step_when_aucun_film(context):
    # Pas de film gagnant attribué, donc on ne fait rien
    pass


# Étape 5 : Vérifier la description du festival avec un film gagnant
@then(u'le festival doit afficher "{expected_description}"')
def step_then_verifier_description(context, expected_description):
    actual_description = context.festival.obtenir_description_festival()
    assert actual_description == expected_description, f"Attendu : '{expected_description}', mais obtenu : '{actual_description}'"

