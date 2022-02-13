from dataclasses import dataclass
import taichi as ti


@dataclass
class PosBufId:
    pos_id: int

@dataclass
class IndBufId:
    ind_id: int
    
@ti.data_oriented
class Rasterizer:
    def __init__(self, w: int, h: int):
        self.frame_buf = ti.field(dtype=float, shape=(w, h))
        self.depth_buf = ti.field(dtype=float, shape=(w, h))

    def load_positions(self, positions):
        pass

    def load_indices(self, indices):
        pass

    def set_model(self, m):
        pass

    def set_view(self, v):
        pass

    def set_projection(self, p):
        pass

    def set_pixel(self, point, color):
        pass

    def clear(self, buff):
        pass

    def draw(self, pos_buffer, ind_buffer, type="Line"):
        pass

    def frame_buffer(self):
        pass

    def __get_next_id(self) -> int:
        ans = self.__next_id
        self.__next_id += 1
        return ans