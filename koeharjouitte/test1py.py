class Engine:
    E_num = 0

    def __init__(self, num, type="Fuel"):
        self.num = num
        self.type = type
        self.E_num = Engine.E_num + 1
        Engine.E_num += 1


class Vehicle:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def start(self):
        print(F"{self.year} {self.make} {self.model} with {self.engine.type} engine starting s/n #{self.engine.E_num}")

    def stop(self):
        print(F"{self.year} {self.make} {self.model} with {self.engine.type} engine stopping s/n #{self.engine.E_num}")


car_engine = Engine(123)
car_engine_2 = Engine(400, "hybrid")
car1 = Vehicle("Ford", "mustang", 2000, car_engine)
car2 = Vehicle("mercedes", "W126", 1987, car_engine_2)

car1.start()
car1.stop()
car2.start()
car2.stop()

#Tuloste tulee olla:

#2013 Ford mustang with Fuel engine starting s/n #1
#2013 Ford mustang with Fuel engine stopping s/n #1
#1987 mercedes W126 with hybrid engine starting s/n #2
#1987 mercedes W126 with hybrid engine stopping s/n #2
