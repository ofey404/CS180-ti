import taichi as ti

ti.init()

shape = (512, 512)
type = ti.u8
pixels = ti.field(dtype=type, shape=shape)

@ti.kernel
def draw():
    for i, j in pixels:
        pixels[i, j] = i / 512 * 255    # integers between [0, 255] for ti.u8

draw()

# ti.imwrite(pixels, f"export_u8.png")

gui = ti.GUI("Julia Set", res=shape)

while True:
    gui.set_image(pixels)
    gui.show()