import pygame
import sys
import re

resolution = (1280,720)
cursor_pos = {"line": 0, "col": 0}
rows = [[]]
row_render = []

# pygame setup
pygame.init()
pygame.display.set_caption("Basic text editor")
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
running = True

text_root = (0,0)
text_size = 100
text_spacing = text_size / 2 + 8

font = pygame.font.Font(None, text_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Keibord input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                rows.append([]) # Change this to insert
                cursor_pos["line"] += 1
                cursor_pos["col"] = 0
            elif event.key == pygame.K_BACKSPACE:
                # Deleting a line
                if cursor_pos["col"] == 0 and cursor_pos["line"] != 0:
                    rows.pop(cursor_pos["line"])
                    cursor_pos["line"] -= 1
                    cursor_pos["col"] = len(rows[cursor_pos["line"]])
                elif cursor_pos["col"] == 0 and cursor_pos["line"] == 0:
                    continue
                else:
                    # Deleting a char
                    rows[cursor_pos["line"]].pop(cursor_pos["col"] - 1)
                    cursor_pos["col"] -= 1

            elif re.match(r'^[ -~]+$', event.unicode):
                rows[cursor_pos["line"]].insert(cursor_pos["col"], event.unicode)
                cursor_pos["col"] += 1

            elif event.key == pygame.K_UP:
                if cursor_pos["line"] != 0:
                    cursor_pos["line"] -= 1
                    if cursor_pos["col"] >= len(rows[cursor_pos["line"]]):
                        cursor_pos["col"] = len(rows[cursor_pos["line"]]);
            elif event.key == pygame.K_DOWN:
                if cursor_pos["line"] < len(rows) - 1:
                    cursor_pos["line"] += 1
                    if cursor_pos["col"] >= len(rows[cursor_pos["line"]]):
                        cursor_pos["col"] = len(rows[cursor_pos["line"]]);
            elif event.key == pygame.K_LEFT:
                if cursor_pos["col"] != 0:
                    cursor_pos["col"] -= 1
                else:
                    if cursor_pos["line"] != 0:
                        cursor_pos["line"] -= 1
                        cursor_pos["col"] = len(rows[cursor_pos["line"]])
            elif event.key == pygame.K_RIGHT:
                if cursor_pos["col"] != len(rows[cursor_pos["line"]]):
                    cursor_pos["col"] += 1
                else:
                    if cursor_pos["line"] != len(rows) - 1:
                        cursor_pos["line"] += 1
                        cursor_pos["col"] = 0

        print(cursor_pos)
        # print(rows)

    screen.fill("black")

    row_render = []
    for i, row in enumerate(rows):
        text = "".join(row)
        row_render.append(font.render(text, True, (255, 255, 255)))
    
    # True Rendering starts here
    for i, row in enumerate(row_render):
        screen.blit(row, (0, text_spacing * i))


    cur_before_text = rows[cursor_pos["line"]][:cursor_pos["col"]]
    vis_cur_x = "".join(cur_before_text)
    vis_cur_x = font.size(vis_cur_x)[0]
    pygame.draw.rect(screen, "white", (vis_cur_x,text_spacing*cursor_pos["line"] - 1,10,text_spacing))



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
