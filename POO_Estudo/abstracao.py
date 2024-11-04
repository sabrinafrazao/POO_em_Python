from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        ...

    def dormir(self):
        print("Este animal está dormindo. ")

class Cachorro(Animal):
    def fazer_som(self):
      print("O cachorro late")

class Gato(Animal):
    def fazer_som(self):
        print("Gato mia.")