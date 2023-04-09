#####################################################################################################################################

'''
Singleton design pattern is one of the Credential Design Pattern and it is easiest to implement. As the name describes itself, it is a way to 
provide one object of a particular type. It is used to describe the formation of a single instance of class while offering a single global 
access point to the object.

It prevents the creation of multiple objects of the single class. The newly created object will be shared globally in an application.

We can understand it with the simple example of Data connectivity. While setting up the database connection, we generate an exclusive Database 
connection object to work with the Database. We can perform every operation regarding database using that single connection object. 
This process is called a Single design pattern.


###### Motivation
Singleton design patterns are specially used in application types that need mechanisms over access to a mutual resource. As we have discussed earlier, 
a single class can be used to define a single instance.

One of the best benefits of using a singleton pattern is that we can restrict the shared resource and maintain integrity. It also prevents the 
overwriting in the current code by the other classes ensuing perilous or incompetent code. We can call the same object at multiple points of 
programs without worrying that it may be overwritten in the same points.


##### Implementation
To implement the singleton pattern, we use the static method. We create the getInstance() method that can return the shared resources. When we call 
the static method, either it gives the unique singleton object or an error singling an instantiated object's existence.

It restricts to create the multiple objects of a defined class and maintain integrity.

We can take an example of the simple analogy - A county has a single central government that controls and accesses the country's operation. 
No one can create another government in a certain period.

We can implement this analogy using the singleton pattern.
'''
#####################################################################################################################################


################ Example 1 #########################

class GovtSingleton:  
   __instance__ = None  
  
   def __init__(self):  
       # This is a Constructor  
      
       if GovtSingleton.__instance__ is None:  
           GovtSingleton.__instance__ = self  
       else:  
           raise Exception("We can not creat another class")  
  
   @staticmethod  
   def get_instance():  
       # We define the static method to fetch instance  
       if not GovtSingleton.__instance__:  
           GovtSingleton()  
       return GovtSingleton.__instance__  
  
# Creating an object of above defined class.  
gover = GovtSingleton()  
print(gover)  
  
same_gover = GovtSingleton.get_instance()  
print(same_gover)  
  
another_gover = GovtSingleton.get_instance()  
print(another_gover)  
  
new_gover = GovtSingleton()  
print(new_gover)


'''
Explanation -

In the above code, we have instantiated an object and stored it in a variable. We have also defined construction, which checks if there is 
another existing class; otherwise, it will raise an exception. We have then defined the static method named get_instance(), 
which returns the existing instance; if it is not available, then create it and return.

When we execute the script, the one GovInstance object is stored at a single point in the memory. When we create another object, it raises an exception.
'''


'''
Method - 2: Double Checked Locking Singleton Design Pattern

The synchronization of the threading is no longer in use because the object never is equal to the None. Let's understand the following example.

'''

############ Example 2 ######################

# Double Checked Locking singleton pattern   
import threading

class Single_Checked(object):   
  
   # resources shared by each and every   
   # instance   
  
   __single_acq_lock = threading.Lock()   
   __singleton_instance = None  
  
   # define the classmethod   
   @classmethod  
   def instance(cls):   
  
      # check for the singleton instance   
      if not cls.__singleton_instance:   
         with cls.__single_acq_lock:   
            if not cls.__singleton_instance:   
               cls.__singleton_instance = cls()   
  
      # return the singleton instance   
      return cls.__singleton_instance   
  
# main method   
if __name__ == '__main__':   
  
   # create class A   
   class A(Single_Checked):   
      pass  
  
   # create class B  
   class B(Single_Checked):   
      pass  
  
   X1, X2 = A.instance(), A.instance()   
   Y1, Y2 = B.instance(), B.instance()   
  
   assert X1 is not Y1   
   assert X1 is X2   
   assert Y1 is Y2   
  
   print('X1 : ', X1)   
   print('X2 : ', X2)   
   print('Y1 : ', Y1)   
   print('Y2 : ', Y2)


'''
###########
Advantages of Singleton Patterns
###########
This pattern provides the following advantages.

A class created using the singleton pattern violates the Single Responsibility Principle, which means it can solve two problems simultaneously.
Single Pattern is difficult to implement in the multithreading environment because we need to ensure that the multithreading environment wouldn't 
create singleton objects several times.
It makes the unit testing very hard because they follow the global state to an application.

##############
Disadvantages of Single Pattern
#############
Single Patterns also contain few demerits which are given below.

A class created using the singleton pattern violates the Single Responsibility Principle which means it can solve two problems at a single time.
Single Pattern is difficult to implement in the multithreading environment, because we need to ensure that multithreading environment wouldn't 
create singleton object several times.
It makes the unit testing very hard because they follow the global state to an application.

##########
Applicability of Design Pattern
##########
We define the applicability of singleton design pattern as follows.

In the project, where we need a firm control over the global variables, we must use the Singleton Method.
Singleton patterns solves the most occurring problems such as logging, caching, thread pools, and configuration setting and often used in 
conjunction with the Factory design pattern.
'''