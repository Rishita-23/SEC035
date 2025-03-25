class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def greet(self):
            return "Hello, my name is{self.name} and I am {self.age} years old."
p = Person("Alice", 25)
print(p.greet())