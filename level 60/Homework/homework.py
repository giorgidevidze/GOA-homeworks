class Motorcycle:
    total_motorcycles = 0

    def __init__(self, brand, model, year, engine_capacity):
        self.brand = brand  
        self.model = model  
        self.year = year    
        self.engine_capacity = engine_capacity 
        
        Motorcycle.total_motorcycles += 1

    def display_info(self):
        """პრინტავს მოტოციკლეტის ინფორმაციას."""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Engine Capacity: {self.engine_capacity}L")
    
    @classmethod
    def get_total_motorcycles(cls):
        """გადმოიტანთ შექმნილი მოტოციკლეტების რაოდენობას."""
        return cls.total_motorcycles


moto1 = Motorcycle("Harley-Davidson", "Sportster", 2023, 1.2)
moto2 = Motorcycle("Yamaha", "MT-07", 2024, 0.7)
moto3 = Motorcycle("Honda", "CBR500R", 2022, 0.5)

moto1.display_info()
moto2.display_info()
moto3.display_info()

print(f"Total motorcycles created: {Motorcycle.get_total_motorcycles()}")