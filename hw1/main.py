import taichi as ti

from rasterizer import Rasterizer

ti.init()

shape = (700, 700)

r = Rasterizer(*shape)

gui = ti.GUI("Julia Set", res=shape)

while True:
    gui.set_image(r.frame_buf)
    gui.show()
