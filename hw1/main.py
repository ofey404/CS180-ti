import taichi as ti

from rasterizer import Rasterizer


def get_model_matrix(rotation_angle):
    pass


def get_view_matrix(eye_pos):
    pass


def get_projection_matrix(eye_fov, aspect_ratio, zNear, zFar):
    pass


def main(argv):
    # imitate `command_line == false`
    ti.init()

    angle = 0
    eye_pos = (0, 0, 5)

    shape = (700, 700)
    r = Rasterizer(*shape)

    pos = ((2, 0, -2), (0, 2, -2), (-2, 0, -2))
    ind = (0, 1, 2)
    pos_id = r.load_positions(pos)
    ind_id = r.load_indices(ind)

    r.set_model(get_model_matrix(angle))
    r.set_view(get_view_matrix(eye_pos))
    r.set_projection(get_projection_matrix(45, 1, 0.1, 50))
    r.draw(pos_id, ind_id)
    gui = ti.GUI("Julia Set", res=shape)

    while gui.running:
        gui.set_image(r.frame_buf)
        gui.show()


if __name__ == "__main__":
    import sys

    main(sys.argv)
