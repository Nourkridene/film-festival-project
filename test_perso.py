import unittest
import perso
#import aventure


class TestPersonnageMythologique(unittest.TestCase):

    def setUp(self):

        self.hero = perso.PersonnageMythologique("Ulysse", "good")
        #self.hero.name = "Ulysse"
        #self.hero.mood = "good"

    def tearDown(self):
        pass

    def test_get_name(self):
        self.assertEqual(self.hero.name, "Ulysse")

    def test_get_mood(self):
        self.assertEqual(self.hero.mood, "good")

    def test_set_name(self):
        self.hero.name = "Achilles"
        self.assertEqual(self.hero.name, "Achilles")

    def test_set_mood(self):
        self.hero.mood = "sad"
        self.assertEqual(self.hero.mood, "sad")

    #def test_set_companion(self):
        #companion = perso.PersonnageMythologique()
        #companion.name = "Achilles"
        #companion.mood = "happy"
        #self.hero.companions = companion
        #self.assertEqual(self.hero.companions, [companion])

    def test_bad_mood(self):
        self.assertEqual("bad", self.hero.bad_mood())





if __name__ == "__main__":
    unittest.main()