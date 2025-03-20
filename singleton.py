from festival import Festival

class FestivalMythologique(Festival):
    _instance = None  # L'instance unique du Singleton

    def __new__(cls, nom: str = "Festival Mythologique"):
        # Si aucune instance n'existe, crée-la
        if cls._instance is None:
            # Appelle le constructeur de la classe parente
            cls._instance = super(FestivalMythologique, cls).__new__(cls)
            cls._instance.__init__(nom)  # Appelle le constructeur de Festival
        return cls._instance

    @classmethod
    def get_instance(cls, nom: str = "Festival Mythologique"):
        """Retourne l'unique instance du festival"""
        return cls(nom)  # Cela appellera __new__ et gérera l'instance unique
