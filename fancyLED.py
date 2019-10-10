import digitalio # pylint: disable=import-error
import board     # pylint: disable=import-error
import time
import random

class FancyLED(object): # defining FancyLED as a class 

	pins = [] # list of the pins for the class (will make coding more efficient for future functions)
	outputs = [True, False] # list of outputs for the sparkle function (frequency of the number of Falses will vary on given parameters)


	def __init__(self, pin1, pin2, pin3): # __init__ function for class saying that the class takes 3 arguments, 1 for each pin
		self.pin1 = digitalio.DigitalInOut(pin1) # defining self.pin1 as a DigitalInOut object located on whatever pin that pin1 is
		self.pin1.direction = digitalio.Direction.OUTPUT # setting pin1's direction as output since they are led's
		self.pin2 = digitalio.DigitalInOut(pin2) # same as above but for pin2
		self.pin2.direction = digitalio.Direction.OUTPUT # setting pin2's direction
		self.pin3 = digitalio.DigitalInOut(pin3) # same as above but for pin3
		self.pin3.direction = digitalio.Direction.OUTPUT # setting pin3's direction
		self.pins = [self.pin1, self.pin2, self.pin3] # adding all pins into the previously defined pins list


	def off(self): # off function will will set all led's to off
		
		for i in range(0, 3): # this is why I chose to make a list - this way, I don't have to set each pin as False one line at a time
			self.pins[i].value = False # setting the pins at index "i" to False


	def alternate(self, rate, duration): # function that will first turn on the middle leds, then the two adjacent leds
		
		for b in range(0, duration): # code will run however many times as the argument says
			for i in range(0, 3, 2): # setting the two side pins to True (the third argument in the for loop is the number at which the variable will increase each time)
				self.pins[i].value = True
			
			self.pins[1].value = False
			time.sleep(rate) # waiting for however long the rate is (an argument of the function)
			
			for i in range(0, 3):
				self.pins[i].value = not self.pins[i].value # switching all values for each led
			time.sleep(rate)	
		
		self.off() # turning off all leds once the function is done running	


	def blink(self, rate, duration): # function will blink at the given rate and duration
		
		for b in range(0, duration):
			for i in range(0, 3): # setting all pins to True
				self.pins[i].value = True 
			
			time.sleep(rate)
			self.off() # turning off all leds (after waiting for the rate)
			time.sleep(rate)


	def chase(self, rate, duration): # function making leds turn on/off in sequence
		
		for b in range(0, duration):
			for i in range(0, 3):
				self.pins[i].value = True # the following code sets one pin to True... 
				
				for b in range(0,3):
					if self.pins[b] != self.pins[i]: # ...and then sets every pin that is not that first pin to False
						self.pins[b].value = False
				
				time.sleep(rate)
		self.off()

	#   S P I C Y   C O D E

	def sparkle(self, rate, freq):

		# frequency code:
		if len(self.outputs) != freq: # if the contents of self.outputs does not already match the frequency the user wants,
			self.outputs.clear() # clears the list
			self.outputs.append(True) # adds in one True since we need at least one
			
			for c in range(0, freq-1): # since frequency is given as the ratio (a frequency of 2 means there is a 1:2 chance the led will be False)
				self.outputs.append(False) # append one False per frequency

		# sparkle code
		for i in range(0,3): # for each led...
			self.pins[i].value = random.choice(self.outputs) # randomly assign it to be True or False
		time.sleep(rate) # wait for rate before turning off
		self.off()
