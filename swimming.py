Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> light = true
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    light = true
NameError: name 'true' is not defined
>>> light = Ture
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    light = Ture
NameError: name 'Ture' is not defined
>>> light = True
>>> light = False
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.setting("world_immutable", True)
\
>>> agree = True
>>> print("I agree: " + str(agree))
I agree: True
>>> length = 2
>>> width = 2
>>> length == width
True
>>> length = 4
>>> width =
SyntaxError: invalid syntax
>>> width =1
>>> length == width
False
>>> blockType = mc.getBlock(10, 18, 13)
>>> pos = mc.player.getPos()
>>> x = pos.x
>>> y = pos.y
>>> z = pos.z
>>> blockType = mc.getBlock(x, y, z)
>>> mc.postToChat(blockType == 0)
>>> 
