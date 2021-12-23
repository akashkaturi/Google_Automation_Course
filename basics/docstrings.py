class PersonalInfo:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        """
        This displays the name, age and gender of a person
        """
        print(
            f"Your name is {self.name}, Your age is {self.age}, You are a {self.gender}")


k = PersonalInfo("Akash", 21, "Male")
print(k.display.__doc__)
