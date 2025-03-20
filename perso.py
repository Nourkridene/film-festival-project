#relier deux objets de la mêm classe : ex = compagnon
class PersonnageMythologique:
    #def __init__(self):
        #pass


    def __init__(self, name: str, mood: str):
        self._name: str = name
        self._mood: str = mood
        #self._trip = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def mood(self) -> str:
        return self._mood

    @mood.setter
    def mood(self, mood: str):
        self._mood = mood

    #@property
    #def companion(self) -> []:
       #return self._companion

    #@companion.setter
    #def companion(self, comp):
        #self._companions.append(comp)

    def bad_mood(self) -> str:
        self._mood = "bad"
        return self.mood
