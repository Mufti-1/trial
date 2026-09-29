# myapp/bikes.py

class Bike:
    def __init__(self):
        self.company = "Honda"
        self.model = "Honda125"

class Motorcar:
    def __init__(self):
        self.name = "Sonata"
        
    def display(self):
        return "Motorcar ...."  # Changed print() to return for web display
