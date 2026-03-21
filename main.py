import curses
from curses import wrapper
import webbrowser
import requests
import time
import textwrap


def main(stdscr):
    def safe_addstr(y, x, text, attr=curses.color_pair(1)):
        height, width = stdscr.getmaxyx()
        if y < 0 or y >= height:
            return
        if x < 0:
            text = text[-x:]
            x = 0
        if x + len(text) > width:
            text = text[:max(0, width - x)]
        if text:
            stdscr.addstr(y, x, text, attr)

    def add_text_block(y_start, lines, max_padding=20, attr=curses.color_pair(1)):
        height, width = stdscr.getmaxyx()
        if not lines:
            return 0

        longest = max(len(line) for line in lines)
        padding = min(max_padding, max(0, (width - longest) // 2))
        available_width = max(10, width - 2 * padding)

        total_lines = 0
        for line in lines:
            wrapped = textwrap.wrap(line, available_width)
            for wline in wrapped:
                safe_addstr(y_start + total_lines, padding, wline, attr)
                total_lines += 1

        return total_lines

    stdscr.clear()
    stdscr.nodelay(True)
    stdscr.keypad(True)

    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)

    curses.init_pair(1, -1, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)

    try:
        repo_count = requests.get(
            "https://api.github.com/users/eesazahed").json().get("public_repos", 0)
    except Exception:
        repo_count = 0

    menu = [
        ("personal site", "https://eesa.zahed.ca"),
        (f"github ({repo_count} public repos)",
         "https://github.com/eesazahed?tab=repositories"),
        ("linkedin", "https://www.linkedin.com/in/eszhd"),
    ]

    selected = 0
    marquee_text = " Welcome to my terminal portfolio! "
    marquee_pos = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        display_text = marquee_text[marquee_pos:] + marquee_text[:marquee_pos]
        center_x = max(0, width // 2 - len(display_text) // 2)
        safe_addstr(4, center_x, display_text[:width], curses.color_pair(2))
        marquee_pos = (marquee_pos + 1) % len(marquee_text)

        safe_addstr(1, 2, "Press 'q' to exit")

        main_padding = 16

        y = 8
        block_lines = [
            "hi my name is eesa",
            "i am a high school senior and i like software development.",
            "i have been coding for quite a while now i guess."
        ]
        y += add_text_block(y, block_lines)

        start_y = y + 2
        for index, item in enumerate(menu):
            url_title = item[0]
            x = width // 2 - len(url_title) // 2
            y_pos = start_y + index
            if index == selected:
                safe_addstr(y_pos, x, url_title,
                            curses.color_pair(2) | curses.A_REVERSE)
            else:
                safe_addstr(y_pos, x, url_title, 1)

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
        time.sleep(0.1)


wrapper(main)
