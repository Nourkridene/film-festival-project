import unittest
import perso
import aventure


class TestAventure(unittest.TestCase):

    def setUp(self):
        self.hero = perso.PersonnageMythologique("Ulysse", "good")
        self.aventure1 = aventure.Aventure(self.hero, "Greece", -800)

    def tearDown(self):
        pass

    def test_change_weather(self):
        self.assertEqual("storm", self.aventure1.change_weather())
        self.assertEqual("bad", self.hero.mood)


if __name__ == "__main__":
    unittest.main()