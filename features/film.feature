Feature: Gestion des films
    En tant qu'utilisateur,
    Je veux pouvoir ajouter un Oscar à un film,
    Afin d'augmenter son nombre d'Oscars.

    Scenario: Ajouter un Oscar à un film
        Given un film réalisé par "Quentin Tarantino"
        When j'ajoute un Oscar à ce film
        Then le nombre d'Oscars doit être 1


    Scenario: Ajouter un Oscar négatif à un film (non valide)
        Given un film réalisé par "Christopher Nolan"
        When j'ajoute -1 Oscar à ce film
        Then une erreur doit être levée


    Scenario Outline: Définir le nombre d'Oscars pour un film
        Given un film réalisé par "<realisateur>"
        When je définis le nombre d'Oscars à <nombre_oscars>
        Then le nombre d'Oscars doit être <resultat_attendu>

        Examples:
            | realisateur         | nombre_oscars | resultat_attendu |
            | Quentin Tarantino   | 2            | 2               |
            | Christopher Nolan   | 0            | 0               |
            | Martin Scorsese     | -1           | ERREUR          |