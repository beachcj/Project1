import os
import csv
import filecmp
from dateutil.relativedelta import *
from datetime import date
import matplotlib.pyplot as plt

def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows



	infile = open(file, 'r')
	line = infile.readlines()
	infile.close()

	dictionary = []

	for x in line:

		definedDict = {}
		listdata = x.split(",")
		first = listdata[0]
		last = listdata[1]
		email = listdata[2]
		classyear = listdata[3]
		dateofbirth = listdata[4]

		definedDict["First"] = first
		definedDict["Last"] = last
		definedDict["Email"] = email
		definedDict["Class"] = classyear
		definedDict["DOB"] = dateofbirth

		dictionary.append(definedDict)
	return dictionary

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	sorted_list = sorted(data, key=lambda i: i[col])
	return (sorted_list[0]["First"] + ' ' + sorted_list[0]["Last"])
	


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	students = []
	students.append(["Senior",0])
	students.append(["Junior",0])
	students.append(["Sophomore",0])
	students.append(["Freshman",0])
	
	for student in data:
		if student['Class'] == 'Senior':
			students[0][1] += 1
		elif student['Class'] == 'Junior':
			students[1][1] += 1
		elif student['Class'] == 'Sophomore':
			students[2][1] += 1
		elif student['Class'] == 'Freshman':
			students[3][1] += 1

	grades = [x[0] for x in students]
	values = [x[1] for x in students]

	plt.bar(grades,values, label = "Class Distribution")
	plt.show()

	for x in range(len(students)):
		students[x] = tuple(students[x])

	sorted_students = sorted(students, reverse=True, key = lambda x: x[1])
	return sorted_students


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	accumulatemonth = {
		'1':0,
		'2':0,
		'3':0,
		'4':0,
		'5':0,
		'6':0,
		'7':0,
		'8':0,
		'9':0,
		'10':0,
		'11':0,
		'12':0		  }

	for x in a:
		months = x['DOB'].split("/")[0]
		if months.strip() in list(accumulatemonth.keys()):
			accumulatemonth[months] += 1
	
	sorted_months = sorted(accumulatemonth, reverse=True, key = accumulatemonth.get)
	
	return int(sorted_months[0])
	

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	
	data_list = sorted(a, key=lambda i: i[col])
	newlist = []

	for i in data_list:
		newlist.append((i["First"] + ', ' + i["Last"] + ', ' + i["Email"] + "\n"))

	outfile = open(fileName, 'w')
	for i in newlist:
		outfile.write(i)

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	
	pass

#def sortData



#infile2.close()
## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()