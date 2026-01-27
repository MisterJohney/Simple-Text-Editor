import pygame
import sys
import re

# pygame setup
pygame.init()
pygame.display.set_caption("Basic text editor")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

text_root = (0,0)
text_size = 100
text_spacing = text_size / 2 + 8

font = pygame.font.Font(None, text_size)
rows = [[]]
row_render = []
cursor_pos = {"line": 0, "col": 0}

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
                    cursor_pos["col"] = len(rows[cursor_pos["line"]]) -1
                if cursor_pos["col"] == 0 and cursor_pos["line"] == 0:
                    continue
                    # Deleting a char
                else:
                    rows[cursor_pos["line"]] = rows[cursor_pos["line"]][:-1]
                    cursor_pos["col"] = cursor_pos["col"] - 1

            elif re.match(r'^[ -~]+$', event.unicode):
                rows[cursor_pos["line"]].append(event.unicode)
                cursor_pos["col"] += 1

        print(cursor_pos)
        print(rows)


    row_render = []
    for row in rows:
        text = "".join(row)
        row_render.append(font.render(text, True, (255, 255, 255)))
    
    # True Rendering starts here
    screen.fill("black")
    i = 0
    for row in row_render:
        screen.blit(row, (0, text_spacing * i))
        i +=1 


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
