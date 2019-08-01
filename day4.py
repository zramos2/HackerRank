class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.iniAge = initialAge
        if self.iniAge < 0:
            print("Age is not valid, setting age to 0.")
            self.iniAge = 0
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.iniAge < 13:
            print("You are young.")
        elif self.iniAge >= 13 and self.iniAge < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.iniAge += 1
