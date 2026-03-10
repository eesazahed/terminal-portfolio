import curses
from curses import wrapper
import webbrowser


def main(stdscr):
    def add_line_of_text(y, text, color=1):
        height, width = stdscr.getmaxyx()
        center_x = 0
        if len(text) < width:
            center_x = width // 2 - len(text) // 2
        stdscr.addstr(y, center_x, text, curses.color_pair(color))

    stdscr.clear()
    stdscr.nodelay(False)
    stdscr.keypad(True)

    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)

    curses.init_pair(1, - 1, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)

    menu = [
        ("GitHub", "https://github.com/eesazahed"),
        ("LinkedIn", "https://www.linkedin.com/in/eszhd"),
    ]

    selected = 0

    while True:
        stdscr.clear()

        stdscr.addstr(1, 2, "Press 'q' to exit")

        add_line_of_text(10, "hi my name is eesa", 2)
        add_line_of_text(
            12, "i am a high school senior and i like software development")

        height, width = stdscr.getmaxyx()

        start_y = 14
        for index, item in enumerate(menu):
            url_title = item[0]

            x = width // 2 - len(url_title) // 2
            y = start_y + index

            if index == selected:
                stdscr.addstr(y, x, url_title, curses.color_pair(2)
                              | curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, url_title, curses.color_pair(1))

        stdscr.refresh()
        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == curses.KEY_UP:
            selected -= 1
        elif key == curses.KEY_DOWN:
            selected += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            webbrowser.open(menu[selected][1])

        selected = max(0, min(selected, len(menu) - 1))


wrapper(main)
