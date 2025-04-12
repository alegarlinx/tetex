class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.rotation_index = 0
        self.x = 0
        self.y = 0

    def rotate(self):
        self.rotation_index = (self.rotation_index + 1) % len(self.shape)

    def get_current_shape(self):
        return self.shape[self.rotation_index]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def reset_position(self):
        self.x = 0
        self.y = 0