# File: Student.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 10/17/2021
# Date Last Modified: 10/20/2021
# Description of Program: The following program defines a Student class. A name and any recorded exam grades can be entered. The program will then display this information as requested. The program can also compute the average of the exam grades if they are provided.

class Student:
    def __init__(self, name, exam1 = None, exam2 = None):
        self.__name = name
        self.__exam1 = exam1
        self.__exam2 = exam2
    def getName(self):
        return self.__name
    def getExam1Grade(self):
        if(self.__exam1 != None):
            return self.__exam1
    def setExam1Grade(self, exam1):
        self.__exam1 = exam1
    def getExam2Grade(self):
        if(self.__exam2 != None):
            return self.__exam2
    def setExam2Grade(self, exam2):
        self.__exam2 = exam2
    def getAverage(self):
        if(self.__exam1 != None) and (self.__exam2 != None):
            return (self.__exam1 + self.__exam2) / 2
        else:
            print("Some exam grades not available.")
    def __str__(self):
        return "Student: " + self.__name + "\n  Exam1: " + str(self.__exam1) + "\n  Exam2: " + str(self.__exam2)
