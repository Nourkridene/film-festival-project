import pytest
from singleton import FestivalMythologique  # Assurez-vous d'importer votre classe Singleton correctement


@pytest.fixture
def festival_mythologique():
    """Fixture pour obtenir l'instance du FestivalMythologique"""
    return FestivalMythologique.get_instance("Cannes")


def test_singleton_instance(festival_mythologique):
    """Vérifie que deux appels à get_instance() retournent la même instance"""
    festival1 = FestivalMythologique.get_instance("Cannes")
    festival2 = FestivalMythologique.get_instance("Venise")

    # Vérifie que les deux instances sont identiques (Singleton)
    assert festival1 is festival2, "Les deux instances doivent être identiques (Singleton)."


def test_nom_festival(festival_mythologique):
    """Vérifie que le nom du festival est correctement défini"""
    assert festival_mythologique.nom == "Cannes", "Le nom du festival doit être 'Cannes'."




def test_change_festival_name(festival_mythologique):
    """Vérifie que le nom du festival peut être modifié correctement"""
    # Modifie le nom du festival
    festival_mythologique.nom = "Sundance"

    assert festival_mythologique.nom == "Sundance", "Le nom du festival doit être 'Sundance'."


def test_no_multiple_instances():
    """Vérifie qu'il n'y a qu'une seule instance du FestivalMythologique"""
    festival1 = FestivalMythologique.get_instance("Cannes")
    festival2 = FestivalMythologique.get_instance("Venise")

    # Vérifie qu'il n'y a qu'une seule instance
    assert festival1 is festival2, "Il ne doit y avoir qu'une seule instance de FestivalMythologique."


