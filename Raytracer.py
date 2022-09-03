from gl import Raytracer, V3
from figures import *
from lights import *
from texture import Texture

width = 820
height = 1024

# Materiales
snow = Material(diffuse=(0.90, 1, 1))
intensewhite = Material(diffuse=(1, 1, 1))
blackstone = Material(diffuse=(0.1, 0.1, 0.1))
graystone = Material(diffuse=(0.4, 0.4, 0.4))
carrot = Material(diffuse=(1, 0.5, 0))


rtx = Raytracer(width, height)

rtx.lights.append(AmbientLight())
rtx.lights.append(DirectionalLight(direction=(-1, -1, -1)))

rtx.background = Texture("background.bmp")
rtx.glClearBackground()

# -----------------------BODY------------------------------------
rtx.scene.append(Sphere(V3(0, 2.8, -10), 1.2, snow))
rtx.scene.append(Sphere(V3(0, 0.5, -10), 1.6, snow))
rtx.scene.append(Sphere(V3(0, -2.5, -10), 2, snow))

# -----------------------BOTONES------------------------------------
rtx.scene.append(Sphere(V3(0, 0.75, -8.7), 0.5, blackstone))
rtx.scene.append(Sphere(V3(0, -0.75, -8.7), 0.5, blackstone))
rtx.scene.append(Sphere(V3(0, -2.1, -8.2), 0.5, blackstone))

# -----------------------FACE------------------------------------
# nose
rtx.scene.append(Sphere(V3(0, 2.7, -8.8), 0.3, carrot))
# eyes
rtx.scene.append(Sphere(V3(0.3, 3.2, -9), 0.17, intensewhite))
rtx.scene.append(Sphere(V3(0.3, 3.2, -8.9), 0.08, blackstone))
rtx.scene.append(Sphere(V3(-0.3, 3.2, -9), 0.17, intensewhite))
rtx.scene.append(Sphere(V3(-0.3, 3.2, -8.9), 0.08, blackstone))
# mouth
rtx.scene.append(Sphere(V3(0.5, 2.5, -9), 0.14, graystone))
rtx.scene.append(Sphere(V3(0.2, 2.3, -9), 0.14, graystone))
rtx.scene.append(Sphere(V3(-0.2, 2.3, -9), 0.14, graystone))
rtx.scene.append(Sphere(V3(-0.5, 2.5, -9), 0.14, graystone))


rtx.glRender()

rtx.glFinish("output.bmp")
