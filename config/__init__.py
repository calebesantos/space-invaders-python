from pygame import display, image

from . import colors

SCREEN = display.set_mode((800,600))

FONT = "assets/fonts/space_invaders.ttf"

IMG_NAMES = ["ship", "ship", "mystery",
             "enemy1_1", "enemy1_2", "enemy2_1", "enemy2_2",
             "enemy3_1", "enemy3_2", "explosionblue",
             "explosiongreen", "explosionpurple", "laser", "enemylaser"]

def loadImage(name):
    return image.load("assets/images/{}.png".format(name)).convert_alpha()

IMAGES = {name: loadImage(name) for name in IMG_NAMES}

TIME_PER_UPDATE = 16.0  #Milliseconds

ORIGINAL_CAPTION = "Space invaders"
