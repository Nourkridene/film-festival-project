import unittest
import perso
import aventure


class TestAventure(unittest.TestCase):

    def setUp(self):
        """ Initialise une aventure avec un héros """
        self.hero = perso.PersonnageMythologique("Ulysse", "good")
        self.aventure1 = aventure.Aventure(self.hero, "Greece", -800)

    def tearDown(self):
        pass

    def test_initialisation_aventure(self):
        """ Vérifie que l'aventure est bien initialisée avec les bonnes valeurs. """
        self.assertEqual(self.aventure1.hero.name, "Ulysse")
        self.assertEqual(self.aventure1.hero.mood, "good")
        self.assertEqual(self.aventure1.place, "Greece")
        self.assertEqual(self.aventure1.year, -800)
        self.assertEqual(self.aventure1.weather, "sunny")

    def test_set_hero(self):
        """ Vérifie que l'on peut changer le héros de l'aventure. """
        new_hero = perso.PersonnageMythologique("Achille", "neutral")
        self.aventure1.hero = new_hero
        self.assertEqual(self.aventure1.hero.name, "Achille")
        self.assertEqual(self.aventure1.hero.mood, "neutral")

    def test_set_place(self):
        """ Vérifie qu'on peut changer le lieu de l'aventure. """
        self.aventure1.place = "Rome"
        self.assertEqual(self.aventure1.place, "Rome")

    def test_set_year(self):
        """ Vérifie qu'on peut changer l'année de l'aventure. """
        self.aventure1.year = -500
        self.assertEqual(self.aventure1.year, -500)

    def test_set_weather(self):
        """ Vérifie qu'on peut changer la météo de l'aventure. """
        self.aventure1.weather = "rainy"
        self.assertEqual(self.aventure1.weather, "rainy")

    def test_change_weather(self):
        """ Vérifie que la météo change et affecte l'humeur du héros. """
        self.assertEqual("storm", self.aventure1.change_weather())
        self.assertEqual("bad", self.hero.mood)  # Vérifie que l'humeur du héros a changé

    def test_bad_mood(self):
        """ Vérifie que la méthode bad_mood du héros fonctionne. """
        self.hero.bad_mood()
        self.assertEqual(self.hero.mood, "bad")

    def test_hero_is_not_none(self):
        """ Vérifie que le héros de l'aventure n'est pas None. """
        self.assertIsNotNone(self.aventure1.hero)

    def test_weather_initial(self):
        """ Vérifie que la météo initiale est correcte. """
        self.assertEqual(self.aventure1.weather, "sunny")

    def test_change_hero_mood_after_weather_change(self):
        """ Vérifie que l'humeur du héros change après un changement de météo. """
        self.aventure1.change_weather()
        self.assertEqual(self.hero.mood, "bad")



    # Test: Vérifie qu'un héros peut avoir un compagnon
    def test_hero_companion(self):
        """ Vérifie que le héros peut avoir un compagnon. """
        companion = perso.PersonnageMythologique("Hercule", "good")
        self.hero.companion = companion  # Assurez-vous que vous avez une méthode pour gérer les compagnons
        self.assertEqual(self.hero.companion.name, "Hercule")
        self.assertEqual(self.hero.companion.mood, "good")

    # Test: Vérifie qu'un héros avec une humeur mauvaise a une météo différente
    def test_change_weather_if_bad_mood(self):
        """ Vérifie que la météo change même si l'humeur du héros est déjà mauvaise. """
        self.hero.mood = "bad"
        initial_weather = self.aventure1.weather
        self.aventure1.change_weather()
        self.assertNotEqual(self.aventure1.weather, initial_weather)

if __name__ == "__main__":
    unittest.main()
