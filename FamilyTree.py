class FamilyMember:

    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye color is:", self.eye_color)
        print("Height is:", self.height_cm,"cm")

class Kid(FamilyMember):

    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)

    def show_traits(self):
        print("Name is:",  self.name)
        print("Age is:", self.age)
        super().show_traits()

    def favoritehobby(self, hobby):
        self.hobby = hobby
        print(self.name, "loves", hobby)

child = Kid("Emir", 12, "Brown", 159)
child.show_traits()
child.favoritehobby("Fishing")
print("Is kid a subclass of FamilyMember? :", issubclass(Kid, FamilyMember))