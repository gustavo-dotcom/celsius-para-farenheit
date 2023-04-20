class Conversor:
    def __init__(self):
        self.celsius = int(input("Digite uma temperatura em celsius:"))

    def converter_para_farenheit(self):
        self.farenheit = (self.celsius * 1.8) + 32
        print("Essa temperatura em farenheit seria", self.farenheit)