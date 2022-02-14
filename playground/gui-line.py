import taichi as ti
import numpy as np

ti.init()

X=np.array(((0, 0),))
Y=np.array(((100, 100),))

shape = (300, 300)

pixels = ti.field(dtype=ti.u8, shape=shape)

gui = ti.GUI("Julia Set", res=shape)
while gui.running:
    gui.set_image(pixels)
    gui.lines(begin=X, end=Y, radius=20, color=0x068587)
    gui.show()
