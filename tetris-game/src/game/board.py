class Board:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def draw(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))

    def check_collision(self, tetromino, offset):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    board_x = x + tetromino.x + offset[0]
                    board_y = y + tetromino.y + offset[1]
                    if board_x < 0 or board_x >= self.width or board_y >= self.height:
                        return True
                    if board_y >= 0 and self.board[board_y][board_x]:
                        return True
        return False

    def merge_tetromino(self, tetromino):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[tetromino.y + y][tetromino.x + x] = 1

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(row)]
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [0 for _ in range(self.width)])