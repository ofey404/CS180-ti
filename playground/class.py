# https://docs.taichi.graphics/lang/articles/advanced/odop#data-oriented-classes
import taichi as ti

@ti.data_oriented
class Painter():
    def __init__(self, n) -> None:
        self.pixels = ti.field(dtype=float, shape=(n * 2, n))

    @ti.kernel
    def paint(self, t: float):
        for i, j in self.pixels:  # Parallelized over all pixels
            c = ti.Vector([-0.8, ti.cos(t) * 0.2])
            z = ti.Vector([i / n - 1, j / n - 0.5]) * 2
            iterations = 0
            while z.norm() < 20 and iterations < 50:
                z = complex_sqr(z) + c
                iterations += 1
            self.pixels[i, j] = 1 - iterations * 0.02
            
@ti.func
def complex_sqr(z):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])

ti.init()

n = 320
p = Painter(n)

gui = ti.GUI("Julia Set", res=(n * 2, n))

for i in range(1000000):
    p.paint(i * 0.03)
    gui.set_image(p.pixels)
    gui.show()
