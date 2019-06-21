
+91 90360 vivek
vivek@conceptarchitect.in
https://github.com/vivekduttamishra/hp-py-201906
----------------------
#https://code.visualstudio.com/docs/python/tutorial-flask
#The default Python implementation, CPython, is actually written in the C programming language.
python -> to lunch python cli
exit() -> exit from python cli
list = [1,2,3]
tuple=(1,3,4)
set={1,2,4}
print(dir(sys))
isinstance(obj,class_name)
hasattr(obj,'attr_name')            #check if attribute 'attr_name' is available in obj or not.
setattr(obj,'myfunc',myfunc)        #add myfunc function to the object obj dynamically .
dir('abc')                          # print all the member available in string
type('abc')                         # print type of the 'abc' data
__str__(self)                       # just like toString in java
time.sleep(2)                       #sleep for particular duration of time
time.perf_counter                   # to check how long time taken to execute code
sys.getsizeof(12)                   # print the size of int used by python

# python store all state of the object in __dir__  in directory structure.
# python doesn't support overloading but support overriding.

#array it is not a datatype supported by python.. in case we want to create array.. have to import and array and use array.array(...).
# we should not override the existing name with anything else existing feature will go off.
  example: print= "rohit kumar"  // fine
           print("this is rohit")  // will throw error.
#we can access the class atrribute(varible or function) using object reference even from inside of the class with . operator.
#How can we add fucntion attribute after creating the object or after creating class:
  ##for method to get add to the class but not to any particular instance of the class:
      @add_method(A)    # custom decorator
      def myfunc():     #this function will be added to the class not to any particular object
          ......
   ## for method to get added to particular object but not on class level:
       ### setattr(object,<string fucntion name>,function name)
   example: setattr(obj,'myfunc',myfunc)



------------- print use ---------
print(f'my name is {name}')
print('my name is{}'.format(name))
print('my name is {0} and profession is:{1}'.format(name,profession))
print('profession:{profession} and name:{name}'.format(name,profession))


-------------- operator ----------
continuation operator: / 
spread operator list/set:  *passingargs
collecotor operator list/set: *receivingargs, 
dictionary collector operator: **
dictionary spread opertor: **
operetor to destroy the object: del obj
-------------------------------
x = input('enter first value:')   #by default it will be consider as string the input value from console
y = input('second number:')
z = int(x)/int(y)                  # convert string to int then perform the division operation
print(z)    # for python version 2.. it will give value 2 if x and y is int while for python 3.. it will give float12
# for python 2 might not to typecast the entered value from console
# How to use Jupyter tool for learning python
  # Jupyter is REPL Environment 
  # it has implcit print and can use explicit print
  # output of only last statem ent is print and rest earlier will not be printed if we are using implict print of Jupyter.
# breaking changes in python 2 and 3:
  # python 3: print is a function and requires parenthesis()
  # python 2: print is a language keyword and doesn't requuire parenthesis.
              # it can work with parenthesis also but will have different meaning
# print(1,2,4,5): in python 3: it is multiple value while in python 2: it is tuple which treated as single object array

# -------------------- Q&A -----------------------
# Q) what is significance of ID in python?
# Q) access specifier
# Q) How can we restrict to take only particular type of data not generic?
# Q) Global function like print, id or type?
# Q) What is tripple quoted String? 
    #Ans: if we want to split our large string in multiple line then, it is used.. (''' .... .... ''')
         # it preservers all the tab and space while printing...
# Q) what is String justification?
# Q) what is difference between pass and continue keyword?
# Q) How can we create empty body function and call it?
   #hint: use pass keyword
# Q difference detween list and array?
# Q) Ternary operation in python?
Ans: true_val if condition else false_val
 # Q) How to input boolean value from CLI?
Ans: take 0 input.. convert to int... convert to bool... then print
        # because... only 0 int consider as flase and non-zero value is treated as true... and all input cli value is by default
        #string which is non zero value any other than 0
# Q) what is difference between input() and raw_input() function
# Q) How to store range of value in list?
 Ans:  list = [val for val in range(1,10)]
        >>> list = [val for val in range(1,10) if val%3==0 or val%4==0]  # here range will not in memory store value.
        >>> list
        [3, 4, 6, 8, 9]
# Q) why there is global keyword in python.
# Q) what are default imported modules?
# Q) How to read value from cli in python?
Ans: sys.arg[0]  or sys.arg[1:]  .. other important sys api:
   sys.version_info   #to get the version of python
   sys.path           # to get the all the path where python look for for loading module.
Q) what is difference between sys.path and PYTHONPATH?
Ans: PYTHONPATH: this variable value only loaded once at the time of starting the application.
    sys.path: it load the module dynamically at run time itself.
  Example to import my custom module in cli: 
     in cmd: set PYTHONPATH=C:\Project_Work\Other_learn\PYTHON_Learn\python_VSC\day_2\
     then in python cli run below command:
     #import histogram_3 as h 
     #h.main()
      
# ================== basic language feature =====================
# Datatype: 
       # all data are object
       # all variable are consider as references and it as no type.. while value has type of object.
         #or all values are object of some type.
       # So, type of references are defined dynamically means.. based on the object we are assigning to the references it types become.
       # all object has some unique identity(ID) which can be printed as:
          #print(id(23))  or x = 3  and print(id(x))
          Example:
             x = 5         statement 1
             x = x + 10    statement 2
        #NOTE: ID of x in statement 1 will different from ID in statement 2
# in python, object can be mutable or immutable.
  # object immutable in python:  int, string
     # whenever we manupulate on the immutable object, it will create a new object memory... ealier value memory can be used by 
     # other references if assigning the same value
     # Objects of built-in types like (int, float, bool, str, tuple, unicode) are immutable. 
     # Objects of built-in types like (list, set, dict) are mutable. Custom classes are generally mutable.
# there is no increment or decrement operator in python.
# operator present in python but not in other language:
  # power operator(**):
    # x = 2**3   // return 8
  # '//' operator will work is int division operator or we can say.. it's always give integer value...
     #x = 7.0/3.0 // output 2.0
   and instead of &&
   or instead of ||
   not instead of !
# int datatype but not variation
# float datatype but not variation
# bool datatype... false or 0... true or non-zero value
#Python has value 'None' which is only value of type that is "NoneType"
  # it is simular to NULL used
  #we can mark a reference as None
# ====================== String method =================
# To declare an empty string, we may use the function str().
# "==" in python is similar to equals() method in java.
# "is" in python is similar to "==" of java.
# String is immutable, linear, indexable  sequence of character.
# what is String justification?
# String formatting....  ... used just like C language
    >>> name = "rohit kuamr"
    >>> empId=1234
    >>> msg = 'hello %s, your employee id is %d ' % (name,empId)
    >>> print(msg)
    hello rohit kuamr, your employee id is 1234
# above way of fomatting string is depricated in Python and below is the new and standard way:
    >>> name = 'rohit'
    >>> id = 1234
    >>> email='ravi@hpe.com'
    >>> msg =  'hello Mr. {}, your id is {} and email is {}'.format(name,id,email)           #way 1
    >>> print(msg)
    hello Mr. rohit, your id is 1234 and email is ravi@hpe.com
    >>> msg =  'hello Mr. {0}, your id is {1} and email is {2}'.format(name,id,email)         #way 2
    >>> print(msg)
    hello Mr. rohit, your id is 1234 and email is ravi@hpe.com
    >>> msg =  'hello Mr. {0}, your id is {1} and email is {web}'.format(name,id,web=email)   #way 3
    >>> print(msg)
    hello Mr. rohit, your id is 1234 and email is ravi@hpe.com
      --------------- OR -----------------
    htmlTag=''' <html>
           <head>{myLearn}</head>
           <body>{body}</body>
           <footer>{footer}</footer>
       </html>'''
    msg=htmlTag.format(myLearn="my python learning",body="this is body",footer='this is footer string')
    print("\n\n",msg)
    ------------------- OR but below not supported by py 2 version ------------------
    >>> print(1,2,4,end='\t')
        1 2 4
    >>> print(1,2,4,sep='=',end='\t')
        1=2=4   >>> print(1,2,4,sep='=',end='')
        1=2=4>>>

NOTE: name place holder must come after numbered values.
     we mixed way 1 and way 2 together.
# help(str)  // get the help about the function
""" >>> s = "ravi kumar"
>>> s.index(i)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'i' is not defined
>>> s.index('i')
3
>>> s.replace('ravi',"rohit")
'rohit kumar'
>>> s.count('i')
1 """
# what is use of fsstring in python?
#Ans We can insert variable, values and expression in the string.
-------------------------- type casting -----------------
int()
float()
bool()
eval()      # if input value is expression the it evaluate and provide output
set()      # convert other seqence to list
tuple()     # convert other sequnce to tuple

-------------------------- Statement ----------
# one big statement can be written in multiple line using continuation character '\' at the end of the line.
   x = 3 + 4 \
    -2
# we can write multiple statement in one line using semi colon character.
   x = 3; y = 5; 
# mulitple assignment 
   x,y,z = 1,3,6  or x,y=y,x   // it will swap the value in one statement.
------------------------------ code block ------------
if Statement
for statement
while statement  ... what is while else loop concept .. might used if we use break in while loop then else statement executed

----------------------------- function -----------------
# must provide the same number of argument as defined in the function while calling it.
# it also suport default value concept if caller is not passing value
      def fun(x, y =5):
          ...
# if we have created any default value concept in function .. then all the other variable in the function declaration 
   #should must have default value assignment concept
   example: def fun(x,y =  4,z=5):    # will work fine
            def fun(x,y = 5, z ):     # will not work fine... as z is not having default value.

--------------------------- Sequences ---------------------------
# it is series of values which can be accessed by for loop and can be stored in in-memory or computed fron non stored sequence
-------------------  about list:
-> list.pop(index)   // remove and return value at index
-> list.remove(value)  // just remove value
-> list.extend(list2)  // copy value from list2 into list
-> list.append(list2)  // added list2 to list as one element of list.
-------------------- tuple ------------
-> immutable array, lenear, indexed, 
-> does not support.. append, extend,del,remove  etc

--------------------- set --------------
s1 = {}
# will support all sorts of set related function like subset, union, intersection, disjoint, difference etc
# set provide add() method to insert value while list has append() method to do the same.
x = [4,2,5,7,8,2,5,7]
s1 = set(x[0::2])  # add value from index 0, 2, 4, 6 ....
s2 = set(x[1::3])  # add value 1, 4, 7, 10
s3 = set(x[::3])  # from from 0 and do like second way
s1.issubset(2)  ... s1.isdisjoint(s2) ...
s1.intersection(s2) ... s1.union(s2)
s1.intersection_update(s2)  ... s1.difference_update(s2)  .. s1.update(s2)
 
----------------------- Map

x = {1:"ravi",2:"raj"}  or x = dict(1="ravi",2="rajS")
x[12]       # will throw error
x.get(12)   # will return None
x.get(12,"Not found")   # if key is not presetn in dict then will it will return 'Not found'
# looping using key of dict
  #Example:
    for key in x:
           print(" key:{}  value:{}",key,x.get(key))
# looping using item of the dict and print key and value:
    for item in x.items():
           print(f" key {item[0]}  and value {item[1]}")

=================== Computed sequence ===============
-> it doesn't store value in memory and the values are calculated on the fly... 
# th value may come from outside sources such as :
   1. network
   2. file 
   3. database
# Example: range() ... random ....
   for i in range(1,10)    #value goes as 1,2,3, .... till 10 or can use: i in range(1,10,2) which means: 1, 3, 5, ....
      print(i)
# range() gives a list only before python v 2.

=========================== Function ========================
#python allows you to pass multiple undefined number of args to a function to match a single parameter.
#All the pass function to the function will be gathered as tuple..
# to achive this feature you need to prefix the parameter name with a collector operator *.
   def my_func(x,y,*other): #other will be a tuple of 0 or more values and will work as tuple.
      ....
#example: what to do, if we are passing list but it should go as multiple arguments.. not like single one then:
   li = [1,2,3]
   my_func(12,4,*li)  #li will spread and go multiple value. means... other will have a touple of 3 elements
--------------
  def my_func(x,*args,y):         # this type of function will throw error in python 2.
         print("x:{}.. args:{} .. y:{}",x,args,y)
   my_func(1,2,3,4,5)      #throw error
   my_func(1,2,3,4,y = 5)  #will work fine
------------ 
  def my_function(x, y = 10, *args, **kwargs):
         print(dictparam)
  my_function(1,4,4,5,8,name="rohit",phone="1234",where="bang")
  # x = 1, y = 4, args=[4,5,8], kwargs={'name':"rohit",'phone':"1234",'where':"bang"}
                     or
  dist = {name:"rohit",phone:"1234",where:"bang"}
  my_function(1,4,4,5,8,**dist)
  #Explanation: 
      **dist will spread the value as and then pass: name="rohit",phone="1234",where="bang"
      *dist will spread the value as of key only and then pass: [name,phone,where]
============================= scope available ================================
  1. global
  2. local
# there is no block scope for the variable. 
# we can't modify the global variable locally like in function.   
# if we want to modify the global variable locally, the function must declare the variable with global scope within the function.
  g = 10
  def access():
      global g
      l = g
      g*=10  #g =111 will also work fine.
      return(l,g)
# by default global variable is not available in our local function... we have to declare in block...... still doublt

============================= module =====================
# Q) module which is default loaded by all module.
  #Ans: __builtins__   which is 
      import __builtins__ *
   print = __builtins__.print  # in case we have override the print value then again we can get the ref as this code.
# Q) how can we create a module of multiple files?
# Q) How can we stop module from importing?
# each .py file is considered as a module and when we import it, it is always a global level.
# we may combile multiple file to create a single large module.
# way of importing:
   import <name of file without extension>   # provide object of that file module and would be able to access all element
   from flask import Flask, xyz              # provide only needed element(fun or class) of the module.
   import flask as fl         
   from flask import *                    # not recommended at all
   import abc.xyz.flask as flask                  # importing from module under the folder
# import create an module object and this object we use to again call the needed function or class from that module.
  #unlike java it's does not include all the code from the imported file while it provide the object of imported module.
# prolem with the second way of import is:
  # if two module is having same function, then last import statement will function will override the earlier one and same will
    #be impacted thoughout the below code.. there is not way to use both the function.. also if we have crated a function in our
    #current module code with the same name as imported event in that case... imported module gloval name will be overriden..
    #and our defined fucntion will be impacted.
   #Example:
             from dateUitl import display
             from funUtil import display      #prev one will overriden by this statement and same will relfect in code
  Solution: We will create a alias of the imported function or if two module is having same name.. then will create a alias Name
     for the module as well.
     #example:
            from dateUitl import display           # where we want to use dateutil display.. use display()
            from funUtil import display as fundisplay  # where we want to use funutil display use fundisplay()
   #NOTE: import along with crating a module object and import it. it execute the module code also and all above way of importing
          #module execute the module file gloval code before imported.
------------- How can we avoid the execution of code while importing ---------
every module object contains a name __name__ property that has value same as module name 
 #directly executing module using python will always have value : __main__ while the module which are being executed because of
   ##importing will have the value for __name__ is the name of the module file like: funUtil, dateUtil etc.
------------- How module is located?
# By default Python runtime searches for the module in the current working folder.
#if a module is usefule to more than one project (application) it makes sense to keep it on a shared location rather 
  # than keeping in the same folder as you main application
--- How to access the module not present in the current folder?
Ans: default:
   1. current working directory
   2. directory where the main script actually existing
   3. directory where python installtaion has stored it's own moudles (already know to python)
   4. PYTHONPATH is a list of paths where python runtime searches for modules.
        "set PYTHONPATH=C:\lib;C:\xyz\pyCustom\lib"   # we can add the path of our shared lib to the PYTHONPATH var in cmd
  #NOTE: PYTHONPATH should contain the folder that contains your module and not the module itself.
  python2: has additional requrirement for locating a module-folder:
       not every folder is module in python2
       a folder ecomes a module if it contains a special file __init__.py
  Python3 doesn't mandate that the file __init__.py must exist....  but if we have created the __init__.py file then still 
      load the module in the same way loaded by python 2.
  #siginificance of this file __init__.py particualrly for python 2:
     1. it is a module identifier
     2. needed only if a folder is treated as Module
     3. each submodule should must contains this this.
     4. __init__.py file is only a marker file and can be empty also.
       ## we can add some code to check when it is getting loaded like:
          #print('this init file is read and caused the current current module to loaded')
---- we can use the same logic in the all the module.. if we have anything global code which might cause execution while 
  importing then we should put the code in if condition.. and should run only if we are directly runing that module using python.
  Code example: 
     if __name__ == '__main__':
            main() # and inside the main() method we should have all global code.. things to keep in mind.. still all code in 
                    # in if condition is in global scope....
====================== important module available in python =============
sys, math, random etc...

============================= class and object =====================
#example of class:
       class myClass:
              count = 0                              #this is static variable which will be accessible by class name   
              def __init__(self):                    # this is similar to constructor of the java but declared differently
                   #initialize the instance variable 
               def __del__(self):   #del obj     // explicity detroying the object obj of the myClass
                  # this function used for clean up purpose when object get destroyed
              def draw(self,pic):                    #this is instance method
                     print(f'picuture has been drawn of pic {pic}')
              def display():                        #static method
                     print(f'this is static kind of method in java and count:{myClass.count}')
#NOTE: everythin inside of the class will be either accessible using class name(for static member) or by object var(for instance
     # member) from outside of the class unlike in java where from inside the class.. we can access other member directly. 

Explanation for the calling static function from object:
   obj.display()
# python first check if there is something attached ddirectly to object obj then retur from that method else go down statement
#if there is something attached to the type(obj) then return from that method else go to down statemtn.
# if first and second statement doesn't satisfied then it will throw error.. no attribute available error.
 NOTE: if we declare static and instance function with same name.. then last declared function will be impacted which can be either
      static or instance both will not be active. 
      #always annotate the static method with @staticmethod annotation. because we can access it using class name but might create
      #prblm while accessing it using object.


#things happens for the below statement:
   t=myClass()
   t.draw('wall')
 # 1.python runtime checks for type(t) which is Triangle
 # 2. it check if Trangle has a draw() method
 # 3. it invoke the draw() method and pass the first argument of the method 't' itself and then second argument will be 'wall' string
  #adding atrribute to the class object dynamically:
       obj.new_attr = 'new attribute added'
       setattr(obj,'myfuncNam',func)  #it will add the function fun for this object obj only... not to the class.

# desctruction of object of the class example:
            >>> class c:
            def __init__(self):
               print('this is init method')
               self.name='rohit kumar'
            def __del__(self):
               print('called at the time of class object destruction')		
            >>> obj = c()
            this is init method
            >>> obj1 = obj
            >>> id(obj)
            13652752
            >>> id(obj1)
            13652752
            >>> del obj    # it will only remove the obj of type c class. but note it.. actuall object is still in memory as obj1 is still referring to the object 
                           # so while deleing the ref obj.. not calling the method __del__(sef).
            >>> obj.name   
            Traceback (most recent call last):
            File "<pyshell#90>", line 1, in <module>
               obj.name
            NameError: name 'obj' is not defined
            >>> obj1.name
            'rohit kumar'
            >>> del obj1    # as this is last reference of the object of the class .. and it is getting delete.. so actual object
                            # object from memory will also get deleted. Hence here __del__(self) method is getting called
            called at the time of class object destruction

# KEY point to mention in the class:
   1. unlike java, we can call constructor of the class as many times as we want.
   2. function defined in the class without any prameter is considered as static function in java class. we can class it with
      class name.
   3. if we are deleting the ref of the object.. and no other ref is pointing to the object.. then at the time of deleting the 
      ref object, Actual object from memory also get deleted and call __del__(self): method.
   4. any class member that begins with an underscore prefix(_) shouldn\'t be accessed by outside.
      it is just convention but in actually we can still access and modify it.

=========================== inheritance =================================
class Employee:
       pass
class It(Employee):
       pass
class Support(Employee):
       pass
class It_support(It,Employee):
       pass
-------------
x = Support();
isinstance(x, Employee)   #output: True
isinstance(x,Support)     #output: True
isinstance(x,It_support)  #output: False
issubclass(It,Employee)   #output: True
issubclass(It,object)     #output: True

0 all class is subclass of object in python just like java
1. class level fields get inherited to the child class but not the instance field.
2. all method get inherited to the child class
2. from the base class we can call to the parent class function using super keyword.
   #call instance level class using super and class name:
     super(subClass, instance).method(args)  or
     super(subclass, subclass).method(args)     #when to use which one
   # python3 has provide the very simle syntax to call parent function:
     super().method(args)      # super.method(self,args)
     super().method(self,args) # for this class method will be called or treated as static class.

--------- multi level inheritance 
>>> class a:
    	def func(self):
		print('this is function a')
>>> class b:
	   def func(self):
		print('this is function b')	
>>> class c(a,b): # if multile super class will have samw function.. then first arg a in the c.. will be impacted on the c class
	   pass        # while same method from  b will be invoked
>>> x = c()
>>> x.func()
this is func a
#explnation: when we right the code: class c(a,b): it will convert to multiple inheritance to multi level inheritance which order
            # will be: b is top most class .. a is child class of b and c is child class of a
#another way to explain the same thing:  ## Method Resolution Order (MRO).
            #In the multiple inheritance scenario, any specified attribute is searched first in the current class. 
            # If not found, the search continues into parent classes in depth-first, left-right fashion without searching same 
            # class twice.


Q) How can we restrict the field or method or class from getting inherited

Q) There is error and solution in the below code.. explain why it is throwing error and how can it solve it:
   Error:
   CASE-1
         >>> class parent:
         count = 'this is in a '
         abx='w323'
         @staticmethod
         def display():
            print('this parent display function')
      >>> class child(parent):
         def display(self):
            super().display()
            print('this is child display function')   
      >>> obj = child()
      >>> obj.display()
      this parent display function
      this is child display function
  CASE-2: 
      >>> class parent:
      count = 'this is in a '
      abx='w323'
      @staticmethod
      def display():
         print('this parent display function') 
      >>> class child(parent):
         @staticmethod
         def display(self):
            super().display()
            print('this is child display function')    
      >>> obj = child()
      >>> obj.display('arg value')
      Traceback (most recent call last):
      File "<pyshell#24>", line 1, in <module>
         obj.display('arg value')
      File "<pyshell#22>", line 4, in display
         super().display()
      TypeError: super(type, obj): obj must be an instance or subtype of type
  CASE-3:  # solution for 2
         >>> class parent:
            count = 'this is in a '
            abx='w323'
            @staticmethod
            def display():
               print('this parent display function')
            >>> class child(parent):
               def display(self):
                  super().display()
                  print('this is child display function')	
            >>> class parent:
               count = 'this is in a '
               abx='w323'
               @staticmethod
               def display():
                  print('this parent display function')
            >>> class child(parent):
               def display(self):
                  super(child,child).display()
                  print('this is child display function')	
            >>> obj = child()
            >>> obj.display()
            this parent display function
            this is child display function

============================= scope ========================
#to get the behavriour of private variable. we can acheive using double underscore prefix in the variable name. ex: __var
 ## same behaviour goes with function name also.
#double underscore use to creat private member:
 ##python renames double underscored member by prefixing ClassName before given name...
   #when you try to access the member using class method.. same translation is done...
     self.__critical=vlaue 'changed to'  self._FinanceInfo__critical = value
#this kind of transformation will be done.. if we will only access the member from inside of the code.. but if 
#we will access directly from outside.. obj.__critical then it will not get transform... and will be treated as a new 
#another new field of the class.
      "self.__critical" in class is different from "obj.__critical" outside of the class.
   # it can be seen by using :
       dir(obj)
#NOTE: double underscore doesn't mean it will not allow the modify the member from outside...we can still accesss it from the 
     # modified member name.. only here is.. if we are doing it means we are doing it consiously not by mistake.
#Significance of @property annotation in python.
   @property: allow to access the function using name without provide the parathesis on it.
 # example is: 
          obj.value()  'annotated with @property  .. must need to called like:' 
         obj.value
     
   
================================ Exception ========================================
# In Python, there are two kinds of errors: 
  1. SyntaxError
  2. Exception 
# few in built exception name:
  0. AttributeError
  1. TypeError
  2. NameError
  3. ZeroDivisionError
# raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
# assert ('linux' in sys.platform), "This code runs on Linux only."
 Example: 
     try:
        raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
     except (TypeError, ZeroDivisionError):
     except:
        print('----- Exception occur ----')
     finally:
        print('finally block get called')
# Create custom Exception: Programs may name their own exceptions by creating a new exception class (see Classes for more about 
                          #Python classes). Exceptions should typically be derived from the Exception class, either directly or 
                          # indirectly.
      #simplest Example: 
       class myException(Exception):
              pass
       raise myException("this is my custom exception error message")

============================== lambda expression / funtional programming ============== #
-> problem with procedural programming: we know what it is to be done but not who is responsilbe for it.. where OOP focus on. 
#  anonymous functions in python are called lambda functions.
#syntax:
        lambda arguments: expression
#Lambda functions can have any number of arguments but only one expression.
#Example: 
   double = lambda x: x * 2
   Output: 10
   print(double(5))
# function is object only in python. we can assign function to ref and pass it anywhere we need.
   def display():
          pass
   ref = display
   #now we can pass this function anywhere we need and process(ref()) at that location.
----- Clousre concept
# normally a local argument or variable within a function dies when the function call is over.
# a inner function is defined within another function's block scope..
# A variable defined by the outer function should be available to the inner function.
# outer function's variable can be access by the inner function but outer function can't access the innner variable.
# code example of nested function :
   >>> def multiply(oparam):
   	   def to(iparam):
	   	   val= oparam*iparam
		      print(f'multiply of {oparam} and {iparam} is:{val}')
	      return to
   >>> multiply(2)(3)   #is equal to x=multiple(2) -> and then x(3)
       multiply of 2 and 3 is:6
#Closure: The inner function will have access to the variables in the outer function scope, even after the outer function has 
          #returned.
        # this closure concept is achieved by python __closure__ attribute in it.
        #And value of __closure__ is tuple which is immutable.
# __closure__: this(Closure) refer to values needed by the function but are taken from the surrounding scope. 
          #When Python compiles a nested function, it notes any variables that it references but are only defined in a parent 
          # function (not globals) in the code objects for both the nested function and the parent scope.

#printing the value which is being refered by __closure__ atribute of function:
    #Example:
      >>> x = multiply(2)     # x hold the inner function 'to' and innter function is using one variable 'oparam' from outer func
      >>> len(x.__closure__)  # so len of x.__closure__ is one as only one value from multiply is being used in 'to' func
      >>> x.__closure__[0].cell_contents   ## will have 2 as 2 has been pass in statement: x = multiply(2)
                              # x.__closure__[0] points or act a pointer to the location where oparam value is stored.

======================== decorator ===================
# A decroator is a function 
  #it takes a function as paramter
  #it warps the logic by additing functionality
  #it returns a new wrapper functionality
  example:
      >>> def my_decorator(fn):
               def inner(x,y):
                  print('cross cutting before')
                  fn(x,y)
                  print('cross cutting after')
               return inner
      >>> @my_decorator
          def myfunc(x,y):
          print(f'this is myfunc whose value -x:{x}.. y:{y}')
      >>> myfunc(3,5)
          cross cutting before
          this is myfunc whose value -x:3.. y:5
          cross cutting after  
     
================================ Shallow copy and Deep copy ================
# In Python, there are two ways to create copies and used by import copy :
  1. Deep copy     # copy.deepcopy(li1)  
  2. Shallow copy  # copy.copy(li1)  


===================== others ======================
Opertor overloading: python support operator overloading.
       #we can create a new definition for an existing operator.
       #each operator is identified by a special name...
         m1+m2  internally converted to m1.__add__(m2)
         #if this function is available in m1 then it will work else will give error
       #'-'  internally converted to __sub__() ... 
       # '==' internally converted to __eq__() ... 
       # '<=' internally converted to __le__() .. 
       # 'len' internally converted to __len__()    
       # 'str' internally converted to __str__() ....in the same all all operator interally converted to some function naame..
#so if we know what actually function internally getting converted to then we can override the existing behaviour of all the 
  # operator or function.
# Q) which operator is best to use... 'is' or '=='
Ans: '==' is better thatn 'is' as we can override the  default behaviour of '==' while can't for the 'is' operator.

             




