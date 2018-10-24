

class Animal:
    name = None
    height = 30

    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def get_type(self):
        print("==Animal==")

    def __str__(self):
        return "Animal {} {}".format(self.name, self.height)

class Dog(Animal):
    owner = ""
    bark_message = "Bark!"

    def __init__(self, name, height, owner):
        super().__init__(name, height)
        self.owner = owner

    def get_type(self):
        print("==Dog==")

    def __str__(self):
        return "Dog {} {} owner={}".format(
            self.name, self.height, self.owner
        )

    def bark(self, times=1):
        for i in range(0, times):
            print(self.bark_message)

cat = Animal("Boi", 20)
cat.get_type()
print(str(cat))

dog = Dog("Brook", 20, "Seb")
dog.get_type()
print(str(dog))

dog.bark(3)