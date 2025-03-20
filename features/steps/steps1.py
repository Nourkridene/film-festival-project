import Mythology.perso as perso


@given('un {nom1} et une {humeur1}')
def step_given_nom_et_humeur(context, nom1, humeur1):
    context.nom = nom1
    context.humeur = humeur1

@given('un {nom1}')
def step_given_nom_seul(context, nom1):
    context.nom = nom1
    context.humeur = "happy"  # Valeur par défaut

@given('rien ou seulement une humeur')
def step_given_rien_ou_humeur(context):
    context.nom = None


@when('utilisateur le valide')
def step_when_valide(context):
    if context.nom:
        context.heros = perso.PersonnageMythologique(context.nom, context.humeur)

    else:
        context.heros = None

@then('un personnage mythologique est créé')
def step_then_heros_cree(context):
    assert context.heros is not None, "Le héros n'a pas été créé !"

@then('un personnage mythologique est créé avec une humeur par défaut : happy')
def step_then_heros_defaut(context):
    assert context.heros is not None
    assert context.heros.mood == "happy"

@then('le système refuse avec un {messageErreur}')
def step_then_erreur(context, messageErreur):
    assert context.heros is None, "Le héros ne devrait pas être créé !"
    assert messageErreur == "Il manque des informations pour créer votre héros", "Le message d'erreur ne correspond pas !"
