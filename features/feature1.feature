Feature: US_000 Créer un héros

  En tant qu'Utilisateur
  Je veux créer un héros mythologique personalisé, avec son nom et son humeur
  Afin de m'immiscer dans mon propre univers mythologique

  Scenario Outline: Création du personnage mythologique
    Given un <nom1> et une <humeur1>
    When utilisateur le valide
    Then un personnage mythologique est créé

    Examples:
    | nom1    | humeur1 |  PersonnageMythologique |
    | Ulysse  | happy   |  Héros1                 |
    | Achille | bad     |  Héros2                 |

  Scenario Outline: Création partielle du personnage mythologique
    Given un <nom1>
    When utilisateur le valide
    Then un personnage mythologique est créé avec une humeur par défaut : happy

     Examples:
     | nom1    | PersonnageMythologique | humeur  |
     | Ulysse  | Héros1                 | happy   |
     | Achille | Héros2                 | happy   |

  Scenario Outline: Erreur de création du personnage mythologique
    Given rien ou seulement une humeur
    When utilisateur le valide
    Then le système refuse avec un <messageErreur>

      Examples:
      | humeur |  messageErreur                                          |
      |         |   Il manque des informations pour créer votre héros     |
      | good    |   Il manque des informations pour créer votre héros     |