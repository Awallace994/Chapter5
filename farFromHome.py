Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = minecraft.create
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    mc = minecraft.create
NameError: name 'minecraft' is not defined
>>> mc = minecraft.create()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    mc = minecraft.create()
NameError: name 'minecraft' is not defined
>>> mc = Minecraft.create()
>>> import math
>>> homeX = 10
>>> homeZ = 10
>>> pos = mc.player.getTilePos()
>>> x = pos.x
>>> z = pos.z
>>> distance = math.sqrt((homeX - x) ** 2 + (homeZ -z) ** 2)
>>> mc.postToChat(distance)
>>> age = 21
>>> ownsCar = True
>>> age > 18 and ownsCar == True
True
>>> age = 25
>>> ownsCar = False
>>> age > 18 and ownsCar == True
False
>>> catColor = input("What color is the cat?")
What color is the cat?
>>> myCatNow = catColor == "black" or catColor == "orange"
>>> print("Adopt this cat: " + str(myCatNow))
Adopt this cat: False
>>> hungry = False
>>> sleeppy = True
>>> timeForBed = not hungry and sleeppy
>>> print(timeForBed)
True
>>> 
>>> 
