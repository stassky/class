class car:                  #once we created our class (car), we can create an object (Don)
    def honk(self):
        print("Beep Beep ")

    def lights(self):
        print("Lights on ")

def main():
    Don=car()
    Don.honk()
    Don.lights()

if __name__ == '__main__':
    main()
