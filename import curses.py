import curses

text = """Hello world!
This is a tiny text editor.
Edit me!"""

cursor = 0


def draw(screen):
    screen.clear()

    # Display the cursor
    display = text[:cursor] + "|" + text[cursor:]

    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)

    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
    )

    screen.refresh()


def main(screen):
    global text, cursor

    while True:
        draw(screen)

        key = screen.getch()

        if key == 27:
            break

        # LEFT 
        elif key == curses.KEY_LEFT:
            if cursor > 0:
                cursor -= 1

        # RIGHT
        elif key == curses.KEY_RIGHT:
            if cursor < len(text):
                cursor += 1

        # BACKSPACE
        elif key in (8, 127, curses.KEY_BACKSPACE):
            if cursor > 0:
                text = text[:cursor - 1] + text[cursor:] 
                cursor -= 1

        # ENTER
        elif key == 10:
            first = text[:cursor]
            second = text[cursor:]
            text = first + "\n" + second
            cursor += 1

        # INSERT CHARACTER
        elif 32 <= key <= 126:
            letter = chr(key)

            first = text[:cursor]
            second = text[cursor:]

            text = first + letter + second
            cursor += 1

curses.wrapper(main)

# import curses

# text = """Hello world!
# This is a tiny text editor.
# Edit me!"""

# cursor = 0


# def draw(screen):
#     screen.clear()

#     # Display the cursor
#     display = text[:cursor] + "|" + text[cursor:]

#     for row, line in enumerate(display.split("\n")):
#         screen.addstr(row, 0, line)

#     screen.addstr(
#         len(display.split("\n")) + 1,
#         0,
#         "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
#     )

#     screen.refresh()


# def main(screen):
#     global text, cursor

#     while True:
#         draw(screen)

#         key = screen.getch()

#         if key == 27:
#             break

#         # LEFT
#         elif key == curses.KEY_LEFT:
#             if cursor > 0:
#                 cursor -= 1

#         # RIGHT
#         elif key == curses.KEY_RIGHT:
#             if cursor < len(text):
#                 cursor += 1

#         # BACKSPACE
#         elif key in (8, 127, curses.KEY_BACKSPACE):
#             if cursor > 0:
#                 text = text[:cursor - 1] + text[cursor:]
#                 cursor -= 1

#         # ENTER
#         elif key == 10:
#             text = text[:cursor] + "\n" + text[cursor:]
#             cursor += 1

#         # INSERT CHARACTER
#         elif 32 <= key <= 126:
#             text = text[:cursor] + chr(key) + text[cursor:]
#             cursor += 1


# curses.wrapper(main)


       # # UP ARROW (Bonus)
        # elif key == curses.KEY_UP:
        #     line_start = text.rfind("\n", 0, cursor) + 1
        #     column = cursor - line_start

        #     if line_start > 0:
        #         previous_end = line_start - 1
        #         previous_start = text.rfind("\n", 0, previous_end) + 1
        #         previous_length = previous_end - previous_start

        #         if column > previous_length:
        #             cursor = previous_start + previous_length
        #         else:
        #             cursor = previous_start + column

        # # DOWN ARROW (Bonus)
        # elif key == curses.KEY_DOWN:
        #     line_start = text.rfind("\n", 0, cursor) + 1
        #     column = cursor - line_start

        #     line_end = text.find("\n", cursor)

        #     if line_end != -1:
        #         next_start = line_end + 1

        #         next_end = text.find("\n", next_start)

        #         if next_end == -1:
        #             next_end = len(text)

        #         next_length = next_end - next_start

        #         if column > next_length:
        #             cursor = next_start + next_length
        #         else:
        #             cursor = next_start + column