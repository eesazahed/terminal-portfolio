from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr("hi")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
