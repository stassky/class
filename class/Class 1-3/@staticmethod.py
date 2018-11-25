class car:                  #Eliminates the usage of "self" argument"
    @staticmethod
    def honk():
        print("Beep Beep ")

    def lights():
        print("Lights on ")



if __name__ == '__main__':
    car.lights()
