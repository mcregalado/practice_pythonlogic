'''Create a Python program that simulates a car race using Object-Oriented Programming (OOP) concepts. 
Apply inheritance, method overriding, class and instance methods, and class attributes to manage car 
details, compare speeds, and calculate averages.'''

class Car:
	count = 0
	def __init__(self, brand, speed, price):
		self.brand = brand
		self.speed = speed
		self.price = price
		Car.count += 1
		Car.total_speed += speed
		
	def info(self):
		print(f"Car Info: {self.brand} | Speed: {self.speed} km/h | Price: {self.price}")
		
	def race_begins(self):
		if self.speed >= 400:
			print(f"{self.brand} is raging at {self.speed} km/h")
		elif self.speed < 400 and self.speed > 200:
			print(f"{self.brand} is racing at {self.speed} km/h")
		elif self.speed < 200:
			print(f"{self.brand} is silently racing at {self.speed} km/h")
	
	def comparing(self,other):
		return  self.speed >= other.speed
	
	@classmethod
	def average_speed(cls):
		return cls.total_speed / cls.count
		
class ElectricCar(Car):
	def __init__(self, brand, speed, price, battery):
		super().__init__(brand,speed,price)
		self.battery = battery
		
	def info(self):
		print(f"Electric Car Info: {self.brand} | Speed: {self.speed} km/h | Price: {self.price} | Battery: {self.battery}%\n")	

car1 = Car("Lamborghini", 350, 10000)
car2 = Car("Toyota", 140, 10000)
ecar1 = ElectricCar("Tesla", 450, 10000, 100)
ecar2 = ElectricCar("Ferrari", 373, 10000, 90)

print(f"{Car.count}	cars have joined the race!\n")

car1.info()
car2.info()
ecar1.info()
ecar2.info()

print("Race Begins!")
car1.race_begins()
car2.race_begins()
ecar1.race_begins()
ecar2.race_begins()

print("\nComparing Cars!")
print(f"Is {ecar1.brand} as fast as {car1.brand}?", Car.comparing(ecar1, car1))
print(f"Is {ecar2.brand} as fast as {car2.brand}?", Car.comparing(ecar2, car2))

print("\nRace Stats!")
print(f"Average top speed of all cars: {Car.average_speed():.2f} km/h")
print(f"Total cars created: {Car.count}")