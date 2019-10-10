class Fish(object):
    kind = "Antigonia"
    eaten = False

    def __init__(self, name, species, age, edibility):
        self.name = name
        self.species = species
        self.age = age
        self.edibility = edibility
        if not isinstance(self.edibility, bool):
            self.edibility = False

        self.tricks = []

    def fish_stats(self):
        if not self.eaten:
            print("Name: " + self.name)
            print("Species: " + self.species)
            print("Age: " + self.age)
            print("Edibility: " + str(self.edibility))
            print("Tricks learned: ")
            for i in range(0, len(self.tricks)):
                print(self.tricks[i])
        else:
            print(self.name + " has been eaten. You monster.")

    def teach(self, trick):
        if not self.eaten:
            self.tricks.append(trick)
        else:
            print("You cannot teach " + self.name + " any tricks because " + self.name + " has been eaten. You monster.")

    def blub(self):
        if not self.eaten:
            return "blub"
        if eaten:
            print("No bubbles appear, because " + self.name + " is being digested in your stomach")

    def eat(self):
        try:
            if self.edibility:
                print("If you say so. You force an uncooked " + self.name + " down your slimy throat without chewing. The fish dies via chemical burns because of your stomach acid.")
                self.eaten = True
            elif not self.edibility:
                print("You cannot eat a " + self.species + ".")
        except ValueError:
            print("Your fish doesn't have a True/False identifier for edibility.")