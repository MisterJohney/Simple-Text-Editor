import pygame
import sys
import re

class Cursor:
    def __init__(self):
        self.line_pos = 0
        self.col_pos = 0

resolution = (1280,720)
rows = [[]]
c = Cursor()

text_root = (0,0)
text_size = 50
line_height = text_size / 2 + 8

# pygame setup
pygame.init()
pygame.display.set_caption("The most advanced text editor in the world")
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
running = True


font = pygame.font.Font(None, text_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Keibord input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                row = rows[c.line_pos]
                rows[c.line_pos] = row[:c.col_pos]
                c.line_pos += 1
                rows.insert(c.line_pos, row[c.col_pos:])
                c.col_pos = 0
            elif event.key == pygame.K_BACKSPACE:
                # Deleting a line
                if c.col_pos == 0 and c.line_pos == 0:
                    continue
                elif c.col_pos == 0 and c.line_pos != 0:
                    row = rows[c.line_pos]
                    rows.pop(c.line_pos)
                    c.line_pos -= 1
                    c.col_pos = len(rows[c.line_pos])
                    for i, item in enumerate(row):
                        rows[c.line_pos].insert(c.col_pos + i, row[i])
                else:
                    # Deleting a char
                    rows[c.line_pos].pop(c.col_pos - 1)
                    c.col_pos -= 1

                #elif event.unicode.isprintable(): # Prints ghost chars for shift, alt, etc.
            elif re.match(r'^[ -~]+$', event.unicode):
                rows[c.line_pos].insert(c.col_pos, event.unicode)
                c.col_pos += 1

            # Cursor nav
            elif event.key == pygame.K_UP:
                if c.line_pos != 0:
                    c.line_pos -= 1
                    if c.col_pos >= len(rows[c.line_pos]):
                        c.col_pos = len(rows[c.line_pos])
            elif event.key == pygame.K_DOWN:
                if c.line_pos < len(rows) - 1:
                    c.line_pos += 1
                    if c.col_pos >= len(rows[c.line_pos]):
                        c.col_pos = len(rows[c.line_pos])
            elif event.key == pygame.K_LEFT:
                if c.col_pos != 0:
                    c.col_pos -= 1
                else:
                    if c.line_pos != 0:
                        c.line_pos -= 1
                        c.col_pos = len(rows[c.line_pos])
            elif event.key == pygame.K_RIGHT:
                if c.col_pos != len(rows[c.line_pos]):
                    c.col_pos += 1
                else:
                    if c.line_pos != len(rows) - 1:
                        c.line_pos += 1
                        c.col_pos = 0



    screen.fill("black")

    row_render = []
    for i, row in enumerate(rows):
        text = "".join(row)
        row_render.append(font.render(text, True, (255, 255, 255)))
    
    # True Rendering starts here
    for i, row in enumerate(row_render):
        screen.blit(row, (0, line_height * i))

    text_before_cur = rows[c.line_pos][:c.col_pos]
    cur_x = "".join(text_before_cur)
    cur_x = font.size(cur_x)[0]
    cur_rect = (cur_x, line_height*c.line_pos, 10, line_height)
    pygame.draw.rect(screen, "white", cur_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
