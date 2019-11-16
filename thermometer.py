class Thermometer():

    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self, unit="C"):
        if unit == "C":
            return self.temperature
        elif unit == "F":
            return self.to_fahrenheit(self.temperature)

    def set_temperature(self, temperature):
        self.temperature = temperature

    def to_celsius(self, temperature):
        temperature = (temperature - 32) * 5 / 9
        return temperature

    def to_fahrenheit(self, temperature):
        temperature = temperature * 9 / 5 + 32
        return temperature
