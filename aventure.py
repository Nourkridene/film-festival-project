import perso


class Aventure:
    def __init__():
        self._place = "Island"
        self._year = "-750"
        self._weather = "sunny"

    def __init__(self, hero: perso.PersonnageMythologique, place: str, year: int):
        self._hero = hero
        self._place = place
        self._year = year
        self._weather = "sunny"

    @property
    def hero(self) -> perso.PersonnageMythologique:
        return self._hero

    @hero.setter
    def hero(self, new_hero: perso.PersonnageMythologique):
        self._hero = new_hero

    @property
    def place(self) -> str:
        return self._place

    @place.setter
    def place(self, new_place: str):
        self._place = new_place

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, new_year: int):
        self._year = new_year

    @property
    def weather(self) -> str:
        return self._weather

    @weather.setter
    def weather(self, new_weather: str):
        self._weather = new_weather

    def change_weather(self) -> str:
        self._weather = "storm"
        self.hero.bad_mood()
        return self.weather
