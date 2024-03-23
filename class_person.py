class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}. Thank you")

# Create an instance of the Person class
me = Person("Ben Onuorah", 37, "Male")

# Call the introduce method...
me.introduce()





