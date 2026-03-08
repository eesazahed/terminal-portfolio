from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(3, 0, "hi")
    stdscr.addstr(5, 0, "eesa")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
