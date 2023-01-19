PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

In this assignment, you will define a simple Student class. Each Student object contains a name (string), and two exam grades (floats or integers). You will always supply a name when you create the class, and also may supply one or both of the exam grades. If you don't supply an exam grade, it should default to None (indicating that that grade is not yet been recorded). You do not need to validate the exam scores entered by the user; you can assume that they are numbers (integer or float), though the numbers can be arbitrary and can even be negative. You should also be able to return the student's average, assuming both exam scores are available. Define a __str__ method so that you can print the Student information in a nice format.

Your code must appropriately handle the case where an exam grade is recorded as None. That is, it shouldn't crash if you ask for that grade or the average. See the example usage below.

You must have the Student class. It must have setters and getters for each of the two exam grades, and a getter for the name. You don't need a setter for the name field; we'll assume names don't change. Name your methods as illustrated by the example below. You can have additional subsidiary functions if you find them useful either within the class or outside it, but you don't have to.

Make the class data private. That is, the name and exam grades should not be accessible outside the class directly, but only through the setters and getters.

Sample Output:

Please make the behavior of your class conform to this example. Note that this examples uses the Python interactive loop. You can also call your class from within another Python program.

> python
Python 3.6.9 (default, Jan 26 2021, 15:33:00) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from Student import *
>>> susie = Student("Susie Q.")
>>> print( susie )
Student: Susie Q.
  Exam1: None
  Exam2: None
>>> susie.getName()
'Susie Q.'
>>> susie.getExam1Grade()              # Notice that None doesn't print
>>> susie.setExam1Grade( 100 )
>>> print( susie )
Student: Susie Q.
  Exam1: 100
  Exam2: None
>>> susie.getExam1Grade()  
100
>>> susie.getAverage()
Some exam grades not available.
>>> susie.setExam2Grade(87)
>>> print( susie )
Student: Susie Q.
  Exam1: 100
  Exam2: 87
>>> susie.getAverage()
93.5
>>> bob = Student( "Bobbie D.", 47, 92 )
>>> print( bob )
Student: Bobbie D.
  Exam1: 47
  Exam2: 92
>>> bob.getAverage()
69.5
>>> clark = Student( "Clark K.", 100 )
>>> print( clark )
Student: Clark K.
  Exam1: 100
  Exam2: None
