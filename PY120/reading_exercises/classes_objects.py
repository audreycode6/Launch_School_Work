class Car:
	
	def __init__(self, model, model_year, color): # initializer
	# instance vairables V
		self.model = model
		self.model_year = model_year
		self.color = color
		self.current_speed = 0

	@staticmethod
	def engine_on():
		print(f"The engine is on.")
		
	def accelerate(self, speed_to_accelerate):
		self.current_speed += speed_to_accelerate
		print(f"{self.model} has accelerated {speed_to_accelerate} mph.")
		
	def brake(self, speed_to_decelerate):
		self.current_speed -= speed_to_decelerate
		if self.current_speed < 0: 
			self.current_speed = 0
		print(f"{self.model} has decelerated {speed_to_decelerate} mph.")
		
	def engine_off(self):
		self.current_speed = 0
		print(f"The engine is turned off.")
		
	def display_current_speed(self):
		print(f"{self.model}'s current speed is {self.current_speed} mph.")


car1 = Car('Saturn', 2006, 'white')
car2 = Car('Toyota', 2010, 'gray')

Car.engine_on()
car1.display_current_speed()
car1.accelerate(5)
car1.display_current_speed()
car1.accelerate(10)
car1.display_current_speed()
car1.brake(10)
car1.display_current_speed()
car1.brake(10)
car1.display_current_speed()
car1.engine_off()
'''
Saturn's engine is on.
Saturn's current speed is 0 mph.
Saturn has accelerated 5 mph.
Saturn's current speed is 5 mph.
Saturn has accelerated 10 mph.
Saturn's current speed is 15 mph.
Saturn has decelerated 10 mph.
Saturn's current speed is 5 mph.
Saturn has decelerated 10 mph.
Saturn's current speed is 0 mph.
Saturn's engine is turned off.
'''