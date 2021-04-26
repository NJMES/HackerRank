
''' Day 4: Class vs. Instance

Objective
In this challenge, we're going to learn about the difference between a class and an instance; 
because this is an Object Oriented concept, it's only enabled in certain languages. 
Check out the Tutorial tab for learning materials and an instructional video!

Task
Write a Person class with an instance variable, 'age' , and a constructor that takes an integer, 'initial age'
, as a parameter. The constructor must assign'initial age' to 'age' after confirming the argument passed 
as 'initial age' is not negative; if a negative argument is passed as 'initial age' , 
the constructor should set 'age' to '0'and print Age is 'not valid', setting age to 0.. 
In addition, you must write the following instance methods:

1. yearPasses() should increase the 'age' instance variable by '1' 

2. amIOld() should perform the following conditional actions:
    - If 'age < 13', print You are young.. 
    - if 'age >= 13' and age <18 print 'you are a teenager..
    - otherwise print 'you are old'

To help you learn by example and complete this challenge, 
much of the code is provided for you, but you'll be writing everything in the future. 
The code that creates each instance of your Person class is in the main method. 
Don't worry if you don't understand it all quite yet!

Note: Do not remove or alter the stub code in the editor.

Input Format
Input is handled for you by the stub code in the editor.

The first line contains an integer, 'T' (the number of test cases), and the'T' subsequent lines 
each contain an integer denoting the 'age' of a Person instance.

Constraints
    - 1<= T <=4 
    - -5<= age <= 30

Output Format
Complete the method definitions provided in the editor so they meet the specifications outlined above; 
the code to test your work is already in the editor. If your methods are implemented correctly, 
each test case will print '2' or '3' lines 
(depending on whether or not a valid 'initial age' was passed to the constructor).

Sample Input
4
-1
10
16
18

Sample Output

Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.

'''

''' Starting code

class Person:       #class - run multiple methods?
    def __init__(self,initialAge):  #initial age.
        # Add some more code to run some checks on initialAge
    def amIOld(self):           
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here

t = int(input())           #input = T  =current age
for i in range(0, t):      # run 0 to current age 
    age = int(input())     # age = T
    p = Person(age)        # run person class on age. 
    p.amIOld()             # run person class check specific amiold method
    for j in range(0, 3):  # run 0 to 3 - 4 counts
        p.yearPasses()          # run person class year passes.  
    p.amIOld()             # run person class check specific amiold method
    print("")              # print result
'''

#solution:

class Person:
    def __init__(self,initialAge):  
        '''what is __init__ ~ It is called as a constructor in object oriented terminology. 
        This method is called when an object is created from a class and it allows the class to initialize the 
        attributes of the class. 'self' The self parameter is a reference to the current instance of the class, 
        and is used to access variables that belongs to the class.'''
        if initialAge <= 0:         #self is default refernce to current instance of class, any input will be registered as initialAge.
            self.age = 0            #self.age = 0 - starts new method call age.
            print ('Age is not valid, setting age to 0.')
        else :
            self.age = initialAge
            
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print ('You are young.')
        elif self.age >= 13 and self.age < 18:
            print ('You are a teenager.')
        else:
            print ('You are old.')
        
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(input())            #To read how many inputs ('t') to prompt.
for i in range(0, t):       #i go through range (0,1,2... to stop before 't' ) to prompt age inputs sucessively.
    age = int(input())      #the inputs will become the 'age'. #how does age become initialAge??
    p = Person(age)         #Class 'person' reads the 'age' and run the methods.
    p.amIOld()              #person's 'amiold' method check.
    for j in range(0, 3):   # 'j' goes through range (0,1,2 to stop before '3') ~ 3 times
        p.yearPasses()      # runs person's 'yearpasses' method #age up by 3 years
    p.amIOld()              # runs 'amiold' method check again
    print("")               # print nothing.