from PIL import Image, ImageTk

from HeroClass import*

batman = Hero("BATMAN")
batman.setPower("Strength", 10, 0.95)
batman.setPower("Tech", 60, 0.4)
batman.setPower('Batarang', 40, 0.7)
batman.setPower('Upper cut', 25, 0.9)
batman.color = 'Black'

joker = Hero("JOKER")
joker.setPower("Dogs", 30, 0.6)
joker.setPower("Acid Gun", 50, 0.5)
joker.setPower('Poison', 20, 0.8)
joker.setPower('Sneak', 15, 1.0)
joker.color = 'Green'

superman = Hero('SUPERMAN')
superman.setPower('Heat vision', 40, 0.6)
superman.setPower('Super strength', 50, 0.7)
superman.setPower('Flying punch', 30, 0.75)
superman.setPower('Super breath', 20, 0.8)
superman.color = 'red'

bane = Hero('BANE')
bane.setPower('Charge', 35, .9)
bane.setPower('Throw', 25, 1)
bane.setPower('Bane Bomb', 70, 0.3)
bane.setPower('Merc Elbow', 35, .9)
bane.color = 'grey'

aquaman = Hero('AQUAMAN')
aquaman.setPower('Trident Slash', 20, 0.9)
aquaman.setPower('Shark attack', 55, 0.6)
aquaman.setPower('Atlantean rage', 70, 0.5)
aquaman.setPower('Tidal wave', 40, 0.75)
aquaman.color = 'teal'

darkseid = Hero('DARKSEID')
darkseid.setPower('Omega Blast', 50, 0.65)
darkseid.setPower('Flying knee', 35, 0.8)
darkseid.setPower('Dark lord', 45, 0.5)
darkseid.setPower('Dark matter', 15, 1.0)
darkseid.color = 'black'

fighters = [batman, joker, superman, bane, aquaman, darkseid]
