class Vehicle:
    def __init__(self, model):
        self.model = model
        print(f"model is {self.model}")

class Car(Vehicle):
    def __init__(self, model):
        super().__init__(model)
        print(self.model)


bmw =  Car("bmw")