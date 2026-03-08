from curses import wrapper


def add_line_of_text(stdscr, text, y):
    height, width = stdscr.getmaxyx()
    center_x = width // 2 - len(text) // 2
    stdscr.addstr(y, center_x, text)


def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(False)
    stdscr.keypad(True)

    while True:
        stdscr.clear()

        stdscr.addstr(1, 2, "Press 'q' to exit")

        add_line_of_text(stdscr, "hi my name is eesa", 10)

        key = stdscr.getch()

        if key == ord('q'):
            break

        stdscr.refresh()


wrapper(main)
