import curses
from curses import wrapper


def main(stdscr):
    def add_line_of_text(text, y, color=1):
        height, width = stdscr.getmaxyx()
        center_x = width // 2 - len(text) // 2
        stdscr.addstr(y, center_x, text, curses.color_pair(color))

    stdscr.clear()
    stdscr.nodelay(False)
    stdscr.keypad(True)

    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, - 1, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)

    while True:
        stdscr.clear()

        stdscr.addstr(1, 2, "Press 'q' to exit")

        add_line_of_text("hi my name is eesa", 10, 2)
        add_line_of_text

        key = stdscr.getch()

        if key == ord('q'):
            break

        stdscr.refresh()


wrapper(main)
