<<<<<<< HEAD

class Weapon:

    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"
=======

class Weapon:

    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"
>>>>>>> 208b47ea4d0bcafc85cf570be2bfb1f6ac828c17
