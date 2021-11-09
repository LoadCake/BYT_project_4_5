import copy


class Car:
    def __init__(self):
        self.seats = 0
        self.engine = ""
        self.doors = 0
        self.type = ""
        self.tankCapacity = 0
        self.drive = ""


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def setSeats(self, seatNumber):
        self.car.seats = seatNumber

    def setEngine(self, engineDescription):
        self.car.engine = engineDescription

    def setDoors(self, doorNumber):
        self.car.doors = doorNumber

    def setCarType(self, carType):
        self.car.type = carType

    def setTankCapacity(self, tankCapacity):
        self.car.tankCapacity = tankCapacity

    def setCarDrive(self, carDrive):
        self.car.drive = carDrive

    def reset(self):
        self.car = Car()

    def getResult(self):
        return copy.copy(self.car)


car = CarBuilder()
print("fill in the info about the car")
car.setSeats(input("seat number:"))
car.setDoors(input("door number:"))
car.setEngine(input("engine description:"))
car.setCarType(input("car type description:"))
car.setCarDrive(input("car drive:"))
car.setTankCapacity(input("Tank capacity:"))
resultCar = car.getResult()
print(f"seats:{resultCar.seats}, doors:{resultCar.doors}, engine:{resultCar.engine}, car type:{resultCar.type}, car drive:{resultCar.drive}, tank capacity:{resultCar.tankCapacity}")