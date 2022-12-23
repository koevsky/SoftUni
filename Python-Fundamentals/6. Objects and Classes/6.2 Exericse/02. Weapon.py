class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        res = ""
        if self.bullets - 1 >= 0:
            self.bullets -= 1
            res = "shooting..."
        else:
            res = "no bullets left"
        return res

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"
    
weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
