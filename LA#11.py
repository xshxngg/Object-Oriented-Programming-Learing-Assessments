class Phone():
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
    def describePhone(self):
        return print(f"brand: {self.brand}, model: {self.model}")
    
class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)
        
phone1= Android("Samsung", "Galaxy")
phone1.describePhone()
