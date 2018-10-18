import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	
	infile = open(file, 'r')
	line = infile.readlines()
	infile.close()

	dictionary = []

	for line in line:

		definedDict = {}
		integer = line.split(",")
		first = integer[0]
		last = integer[1]
		email = integer[2]
		classyear = integer[3]
		dateofbirth = integer[4]

		definedDict["First"] = first
		definedDict["Last"] = last
		definedDict["Email"] = email
		definedDict["Class year"] = classyear
		definedDict["Date of Birth"] = dateofbirth

		dictionary.append(definedDict)
	return dictionary
	pass

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	sorted_list = sorted(data, key=lambda i: i[col])
	return (sorted_list[0]["First"] + ' ' + sorted_list[0]["Last"])
	pass


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	pass


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	pass

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	pass

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.


		dateofbirth = integer[3]

#def sortData



print(mySort(getData("P1DataA.csv"), "First"))
#infile2.close()