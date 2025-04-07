import random

class Character:
    def __init__(self):
        # Private properties
        self._combat_strength = random.randint(1, 6)
        self._health_points = random.randint(1, 6)

    def __del__(self):
        print("The Character object is being destroyed by the garbage collector")

    # Complex getters
    @property
    def combat_strength(self):
        return self._combat_strength

    @property
    def health_points(self):
        return self._health_points

    # Complex setters
    @combat_strength.setter
    def combat_strength(self, value):
        if isinstance(value, int) and value >= 0:
            self._combat_strength = value
        else:
            raise ValueError("Combat strength must be a non-negative integer")

    @health_points.setter
    def health_points(self, value):
        if isinstance(value, int) and value >= 0:
            self._health_points = value
        else:
            raise ValueError("Health points must be a non-negative integer") 