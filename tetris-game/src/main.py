import curses
from game.board import Board
from game.tetromino import Tetromino
from game.utils import create_new_tetromino

def main(stdscr):
    # Configuración de la pantalla
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    board = Board()
    current_tetromino = create_new_tetromino()

    while True:
        stdscr.clear()
        board.draw(stdscr)
        current_tetromino.draw(stdscr)

        key = stdscr.getch()

        if key == curses.KEY_LEFT:
            current_tetromino.move(-1, 0)
        elif key == curses.KEY_RIGHT:
            current_tetromino.move(1, 0)
        elif key == curses.KEY_DOWN:
            current_tetromino.move(0, 1)
        elif key == curses.KEY_UP:
            current_tetromino.rotate()

        if board.check_collision(current_tetromino):
            board.merge_tetromino(current_tetromino)
            current_tetromino = create_new_tetromino()

        board.clear_lines()

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)