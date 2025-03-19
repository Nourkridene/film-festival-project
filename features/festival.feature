Feature: Gestion des festivals
  En tant qu'utilisateur,
  Je veux pouvoir attribuer un film gagnant à un festival,
  Afin de connaître le film récompensé.

  Scenario: Attribuer un film gagnant à un festival
    Given un festival nommé "Cannes"
    When j'attribue le film "Inception" réalisé par "Christopher Nolan" comme gagnant
    Then le festival doit afficher "Le film réalisé par 'Christopher Nolan' a remporté le festival Cannes avec 0 Oscar(s)."



  Scenario: Festival sans film gagnant
    Given un festival nommé "Berlin"
    When aucun film n'est attribué comme gagnant
    Then le festival doit afficher "Aucun film n'a été désigné gagnant pour le festival Berlin."



  Scenario Outline: Vérification de l'attribution d'un film gagnant
    Given un festival nommé "<nom_festival>"
    When j'attribue le film "<titre>" réalisé par "<realisateur>" comme gagnant avec <nombre_oscars> Oscar(s)
    Then le festival doit afficher "Le film réalisé par '<realisateur>' a remporté le festival <nom_festival> avec <nombre_oscars> Oscar(s)."

    Examples:
      | nom_festival | titre           | realisateur         | nombre_oscars |
      | Toronto      | Titanic         | James Cameron       | 3             |
      | Sundance     | Whiplash        | Damien Chazelle     | 1             |
      | Cannes       | Inception       | Christopher Nolan   | 0             |
      | Venise       | Pulp Fiction    | Quentin Tarantino   | 2             |
