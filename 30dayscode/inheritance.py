import sys
import statistics
from io import StringIO

sys.stdin = StringIO("""Heraldo Memelli 8135627
2
100 80""")

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    
    def calculate(self):
        new_scores = statistics.mean(scores)
        if 90 <= new_scores <= 100:
           	return "O"
        elif 80 <= new_scores < 90:
            return "E"
        elif 70 <= new_scores < 80:
            return "A"
        elif 55 <= new_scores < 70:
            return "P"
        elif 40 <= new_scores < 55:
            return "D"
        else:
            return "T"
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())