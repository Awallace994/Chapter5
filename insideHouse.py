Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> 
>>> buildX = 1
>>> buildY = 2
>>> buildZ = 3
>>> width = 10
>>> height = 5
>>> length = 6
>>> 
>>> pos = mc.player.getTilePos()
>>> 
>>> x = pos.x
>>> y = pos.y
>>> z = pos.z
>>> 
>>> inside = buildX < x < buildX + width and
SyntaxError: invalid syntax
>>> 
