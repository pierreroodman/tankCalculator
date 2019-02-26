import math
from PIL import Image


class cubeTank:
	# constructor method
	def __init__(self, tankHeight, tankWidth, tankLength, fuelHeight):
		self.tankHeight = tankHeight
		self.tankWidth = tankWidth
		self.tankLength = tankLength
		self.fuelHeight = fuelHeight

	# class method for creating an object using user inputs
	@classmethod
	def from_input(cls):
		return cls(
        float(raw_input("\n\nPlease enter height of tank in cm, decimal point is allowed: ")),
        float(raw_input("Please enter width of tank in cm, decimal point is allowed: ")), 
        float(raw_input("Please enter length of tank in cm, decimal point is allowed: ")), 
        float(raw_input("Please enter fuel level from bottom of the tank in cm, decimal point is allowed: "))
        )

	# method used for calculating and displaying all the information needed to install sensor and calibrate sensor for the specific tank
	def calculate(self):
		# calculate and display the maximum volume of the tank
		print("\n\nMax volume of tank is " + str(((math.pi * self.tankHeight * self.tankWidth * self.tankLength)/4)/1000) + " litres.")

		# calculate and display the current volume of fuel in tank in litres
		fuelVolume = (((self.tankHeight*(self.tankWidth)*self.tankLength)/4)*((math.acos(1-((2*self.fuelHeight)/self.tankHeight)))-((1-((2*self.fuelHeight)/self.tankHeight))*(math.sqrt(((4*self.fuelHeight)/self.tankHeight)-(((4)*(self.fuelHeight**2))/(self.tankHeight**2)))))))/1000
		print("\n\nActual fuel volume is " + str(fuelVolume) + " litres. ")

		#calculate and display the length to cut sensor to
		sensorLength = self.tankHeight - 1.5
		print("\n\nCut sensor to " + str(sensorLength) + " cm. ")

		# this loop iterates from 0 to 100 in order to calculate and display the calibration data needed for each percentage point that the sensor can be covered by fuel.
		print("\n\n\nCalibration points: \n")
		for i in range(101):

			calibrationPoint = ((float(i)/100) * sensorLength) + 1.5
			calibrationPointVolume = (((self.tankHeight*(self.tankWidth)*self.tankLength)/4)*((math.acos(1-((2*calibrationPoint)/self.tankHeight)))-((1-((2*calibrationPoint)/self.tankHeight))*(math.sqrt(((4*calibrationPoint)/self.tankHeight)-(((4)*(calibrationPoint**2))/(self.tankHeight**2)))))))/1000
			print(str(i) + "%" + " - " + str(calibrationPointVolume) + " litres. ")





class cylindricalTank:
	# constructor method
	def __init__(self, tankDiameter, tankLength, fuelHeight):
		self.tankDiameter = tankDiameter
		self.tankLength = tankLength
		self.fuelHeight = fuelHeight


	# class method for creating an object using user inputs
	@classmethod
	def from_input(cls):
		return cls(
        float(raw_input("\n\nPlease enter diameter of tank in cm, decimal point is allowed: ")),
        float(raw_input("Please enter length of tank in cm, decimal point is allowed: ")), 
        float(raw_input("Please enter fuel level from bottom of the tank in cm, decimal point is allowed: "))
        )


	# method used for calculating and displaying all the information needed to install sensor and calibrate sensor for the specific tank
	def calculate(self):
		# calculate and display the maximum volume of the tank
		tankRadius = float(self.tankDiameter/2)
		print("\nMax volume of tank is " + str(math.pi*tankRadius*self.tankLength/100) + " litres.")

		# calculate and display the current volume of fuel in tank in litres
		fuelVolume = (self.tankLength*(((tankRadius**2)*math.acos((tankRadius-self.fuelHeight)/tankRadius))-((tankRadius-self.fuelHeight)*(math.sqrt((2*tankRadius*self.fuelHeight)-(self.fuelHeight**2))))))/1000
		print("\nActual fuel volume is " + str(fuelVolume) + " litres. ")

		#calculate and display the length to cut sensor to
		sensorLength = self.tankDiameter - 1.5
		print("\nCut sensor to " + str(sensorLength) + " cm. ")


		# this loop iterates from 0 to 100 in order to calculate and display the calibration data needed for each percentage point that the sensor can be covered by fuel.
		print("\n\n\nCalibration points: \n")
		for i in range(101):

			calibrationPoint = ((float(i)/100) * sensorLength) + 1.5
			calibrationPointVolume = (self.tankLength*(((tankRadius**2)*math.acos((tankRadius-calibrationPoint)/tankRadius))-((tankRadius-calibrationPoint)*(math.sqrt((2*tankRadius*calibrationPoint)-(calibrationPoint**2))))))/1000
			print(str(i) + "%" + " - " + str(calibrationPointVolume) + " litres. ")





class elipticalTank:
	# constructor method
	def __init__(self, tankHeight, tankWidth, tankLength, fuelHeight):
		self.tankHeight = tankHeight
		self.tankWidth = tankWidth
		self.tankLength = tankLength
		self.fuelHeight = fuelHeight


	# class method for creating an object using user inputs
	@classmethod
	def from_input(cls):
		return cls(
		float(raw_input("\n\nPlease enter height of tank in cm, decimal point is allowed: ")),
		float(raw_input("Please enter width of tank in cm, decimal point is allowed: ")),
		float(raw_input("Please enter length of tank in cm, decimal point is allowed: ")),
		float(raw_input("Please enter fuel level from bottom of the tank in cm, decimal point is allowed: "))
		)


	# method used for calculating and displaying all the information needed to install sensor and calibrate sensor for the specific tank
	def calculate(self):
		# calculate and display the maximum volume of the tank
		print("\nMax volume of tank is " + str(((math.pi * self.tankHeight * self.tankWidth * self.tankLength)/4)/1000) + " litres.")

		# calculate and display the current volume of fuel in tank in litres
		fuelVolume = (((self.tankHeight*(self.tankWidth)*self.tankLength)/4)*((math.acos(1-((2*self.fuelHeight)/self.tankHeight)))-((1-((2*self.fuelHeight)/self.tankHeight))*(math.sqrt(((4*self.fuelHeight)/self.tankHeight)-(((4)*(self.fuelHeight**2))/(self.tankHeight**2)))))))/1000
		print("\nActual fuel volume is " + str(fuelVolume) + " litres. ")

		#calculate and display the length to cut sensor to
		sensorLength = self.tankHeight - 1.5
		print("\nCut sensor to " + str(sensorLength) + " cm. ")


		# this loop iterates from 0 to 100 in order to calculate and display the calibration data needed for each percentage point that the sensor can be covered by fuel.
		print("\n\n\nCalibration points: \n")
		for i in range(101):

			calibrationPoint = ((float(i)/100) * sensorLength) + 1.5
			calibrationPointVolume = (((self.tankHeight*(self.tankWidth)*self.tankLength)/4)*((math.acos(1-((2*calibrationPoint)/self.tankHeight)))-((1-((2*calibrationPoint)/self.tankHeight))*(math.sqrt(((4*calibrationPoint)/self.tankHeight)-(((4)*(calibrationPoint**2))/(self.tankHeight**2)))))))/1000
			print(str(i) + "%" + " - " + str(calibrationPointVolume) + " litres. ")



class dShapedTank:
	# constructor method
	def __init__(self, tankHeight, squareWidth, dWidth, tankLength, fuelHeight):
		self.tankHeight = tankHeight
		self.rectWidth = rectWidth
		self.dWidth = dWidth
		self.tankLength = tankLength
		self.fuelHeight = fuelHeight


	# class method for creating an object using user inputs
	@classmethod
	def from_input(cls):
		return cls(
		float(raw_input("\n\nPlease enter height of tank in cm, decimal point is allowed: ")),
		float(raw_input("Please enter width of square-shaped portion of tank profile in cm, decimal point is allowed: ")),
		float(raw_input("Please enter width of D-shaped portion of tank profile in cm, decimal point is allowed: ")),
		float(raw_input("Please enter length of tank in cm, decimal point is allowed: ")),
		float(raw_input("Please enter fuel level from bottom of the tank in cm, decimal point is allowed: "))
		)


	# method used for calculating and displaying all the information needed to install sensor and calibrate sensor for the specific tank
	def calculate(self):
		# calculate and display the maximum volume of the tank
		print("\nMax volume of tank is " + str(((self.tankHeight*self.squareWidth*self.tankLength)/1000)+(((3.14*(self.tankHeight/2)*self.dWidth)/2)*self.tankLength)/1000) + " litres.")

		# calculate and display the current volume of fuel in tank in litres
		fuelVolume = ((self.fuelHeight*self.squareWidth*self.tankLength)/1000)+((((self.tankHeight*(2*self.dWidth)*self.tankLength)/4)*((math.acos(1-((2*self.fuelHeight)/self.tankHeight)))-((1-((2*self.fuelHeight)/self.tankHeight))*(math.sqrt(((4*self.fuelHeight)/self.tankHeight)-(((4)*(self.fuelHeight**2))/(self.tankHeight**2)))))))/2)/1000
		print("\nActual fuel volume is " + str(fuelVolume) + " litres. ")


		#calculate and display the length to cut sensor to
		sensorLength = self.tankHeight - 1.5
		print("\nCut sensor to " + str(sensorLength) + " cm. ")


		# this loop iterates from 0 to 100 in order to calculate and display the calibration data needed for each percentage point that the sensor can be covered by fuel.
		print("\n\n\nCalibration points: \n")
		for i in range(101):

			calibrationPoint = ((float(i)/100) * sensorLength) + 1.5
			calibrationPointVolume = ((calibrationPoint*self.squareWidth*self.tankLength)/1000)+((((self.tankHeight*(2*self.dWidth)*self.tankLength)/4)*((math.acos(1-((2*calibrationPoint)/self.tankHeight)))-((1-((2*calibrationPoint)/self.tankHeight))*(math.sqrt(((4*calibrationPoint)/self.tankHeight)-(((4)*(calibrationPoint**2))/(self.tankHeight**2)))))))/2)/1000
			print(str(i) + "%" + " - " + str(calibrationPointVolume) + " litres. ")

programRunning = True
while (programRunning): 
	try:
		choice = int(raw_input("Enter 1 for a Cube or Rectangular shaped tank: \nEnter 2 for a Cylindrical tank: \nEnter 3 for a Eliptical tank: \nEnter 4 for a D-shaped tank eg. Volvo: "))
	except ValueError:
		print("That was not a number! \n\n")
		continue

	if (choice < 1 or choice > 4):
		print("Please enter a valid choice: \n\n")
		continue

	elif (choice == 1):
		tank = cubeTank.from_input()
		tank.calculate()
		break

	elif (choice == 2):
		tank = cylindricalTank.from_input()
		tank.calculate()
		break

	elif (choice == 3):
		tank = elipticalTank.from_input()
		tank.calculate()
		break

	elif (choice == 4):

		img = Image.open('dShaped.jpg')
		img.show()


		tank = dShapedTank.from_input()
		tank.calculate()
		break

quit = raw_input("Press enter to quit program. ")