from behave import given, when, then
from film import Film
from exceptions import NombreOscarsNegatifError

@given('un film réalisé par "{realisateur}"')
def step_impl(context, realisateur):
    context.film = Film(realisateur)

@when("j'ajoute un Oscar à ce film")
def step_impl(context):
    context.film.ajouter_oscar()

@when("j'ajoute -1 Oscar à ce film")
def step_impl(context):
    try:
        context.film.nombre_oscars = -1
        context.erreur = None
    except NombreOscarsNegatifError:
        context.erreur = "ERREUR"

@when("je définis le nombre d'Oscars à {nombre_oscars}")
def step_impl(context, nombre_oscars):
    try:
        context.film.nombre_oscars = int(nombre_oscars)
        context.erreur = None
    except NombreOscarsNegatifError:
        context.erreur = "ERREUR"

@then("le nombre d'Oscars doit être {resultat_attendu}")
def step_impl(context, resultat_attendu):
    if resultat_attendu == "ERREUR":
        assert context.erreur == "ERREUR", "Aucune erreur levée alors qu'elle était attendue"
    else:
        assert context.film.nombre_oscars == int(resultat_attendu), \
            f"Attendu {resultat_attendu}, mais obtenu {context.film.nombre_oscars}"

@then("une erreur doit être levée")
def step_impl(context):
    assert context.erreur == "ERREUR", "Aucune erreur levée alors qu'elle était attendue"
