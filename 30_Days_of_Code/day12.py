class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


#https://www.w3schools.com/python/python_inheritance.asp
#Use link to understand why class is used liked this.
#It is using "Inheritance"

class Student(Person):
    # Class Constructor
    #
    # Parameters:
    # firstName - A string denoting the Person's first name.
    # lastName - A string denoting the Person's last name.
    # id - An integer denoting the Person's ID number.
    # scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        # Keeps the inheritance of the 'Parent Class'
        Person.__init__(self, firstName, lastName, idNumber)

        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #  Function Name: calculate
    # Return: A character denoting the grade.
    # Description: Functions to get average and find grade letter given the grades
    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg <= 100.0 and avg >= 90.0:
            return 'O'
        elif avg < 90.0 and avg >= 80.0:
            return 'E'
        elif avg < 80.0 and avg >= 70.0:
            return 'A'
        elif avg < 70.0 and avg >= 55.0:
            return 'P'
        elif avg < 55.0 and avg >=40.0:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
