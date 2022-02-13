import taichi as ti
from itertools import cycle

ti.init()

shape = (512, 512)
type = ti.u8
pixels = ti.field(dtype=type, shape=shape)

@ti.kernel
def draw(grayscale_base: int):
    for i, j in pixels:
        pixels[i, j] = i / 512 * grayscale_base    # integers between [0, 255] for ti.u8


# ti.imwrite(pixels, f"export_u8.png")

gui = ti.GUI("Julia Set", res=shape)

grayscale_palette = cycle((255, 127, 63, 31, 15, 7, 3, 1))
grayscale_base = grayscale_palette.__next__()

while gui.running:
    if gui.get_event(ti.GUI.PRESS):
        grayscale_base = grayscale_palette.__next__()
        print("get_event, grayscale_base = {}".format(grayscale_base))
    draw(grayscale_base)
    gui.set_image(pixels)
    gui.show()