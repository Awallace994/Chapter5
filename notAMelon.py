Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> 
>>> x = 10
>>> y = 11
>>> z = 12
>>> melon = 103
>>> block = mc.getBlock(x, y, z)
>>> 
>>> noMelon = # Check the block is not a melon
SyntaxError: invalid syntax
>>> 
>>> noMelon = 12
>>> mc.postToChat("You will need to get some food: " + str(noMelon))
>>> True and not False or False
True
>>> True and True or False
True
>>> True or False
True
>>> wolves = input("Enter the number of wolves: ")
Enter the number of wolves: 
>>> enoughWolves = wolves > 10 and wolves < 20
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    enoughWolves = wolves > 10 and wolves < 20
TypeError: unorderable types: str() > int()
>>> print("Enough wolves " + str(enoughWolves))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print("Enough wolves " + str(enoughWolves))
NameError: name 'enoughWolves' is not defined
>>> enoughWolves = 10
>>> print("Enough wolves " + str(enoughWolves))
Enough wolves 10
>>> 
>>> wolves = input("Enter the number of wolves: ")
Enter the number of wolves: 
>>> enoughWolves = 10 < wolves < 20
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    enoughWolves = 10 < wolves < 20
TypeError: unorderable types: int() < str()
>>> 
>>> print("Enough wolves " + str(enoughWolves))
Enough wolves 10
\
>>> wolves = input("Enter the number of wolves: ")
Enter the number of wolves: 
>>> enoughWolves = 10 <= wolves <= 20
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    enoughWolves = 10 <= wolves <= 20
TypeError: unorderable types: int() <= str()
>>> print("Enough wolves: " + str(enoughWolves))
Enough wolves: 10
>>> 
