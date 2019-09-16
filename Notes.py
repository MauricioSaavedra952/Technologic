Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for 1 in range(5);
SyntaxError: invalid syntax
>>> for 1 in range(5):
	print("x")
	
SyntaxError: can't assign to literal
>>> print("x")
x
>>> for 1 in range(5):
	print("x")
	
SyntaxError: can't assign to literal
>>> x=1
>>> print("x")
x
>>> for 1 in range(5):
	1
	
SyntaxError: can't assign to literal
>>> for i in range(5):
	print("x")
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
[DEBUG ON]
>>> x=1
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> x=input("enter a number")
enter a number
>>> 2
2
>>> x=2
>>> if(x==3):
	print("yes")
	else
	
SyntaxError: invalid syntax
>>> if(x==3):
	print("yes")
	else:
		
SyntaxError: invalid syntax
>>> x=int(x)
>>> print(type(x))
<class 'int'>
>>> x=input("enter a number:")
enter a number:5
>>> print("x+1")
x+1
>>> x+1
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x+1
TypeError: can only concatenate str (not "int") to str
>>> 
