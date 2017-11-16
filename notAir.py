Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> notAir = blockType == 0
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    notAir = blockType == 0
NameError: name 'blockType' is not defined
>>> blockType = 5
>>> notAir = blockType == 0
>>> mc.postToChat("The player is not standing in air: " + str(notAir))
>>> mc.postToChat("The player is not standing in air: " + str(notAir))
>>> mc.postToChat("The player is not standing in air: " + str(notAir))
>>> limit = 100
>>> obsidian = 99
>>> limit > obsidian
True
>>> limit = 100
>>> obsidian = 100
>>> canLift = limit > obsidian
>>> 
>>> canlift
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    canlift
NameError: name 'canlift' is not defined
>>> canLift
False
>>> vanHeight = 8
>>> bridgeHeight = 12
>>> vanHeight < bridgeHeight
True
>>> bridgeHeight = 7
>>> vanHeight < bridgeHeight
False
>>> stickers = 30
>>> people = 30
>>> stickers >= people
True
>>> stickers = 30
>>> people = 31
>>> stickers >= people
False
>>> 
