import re

import pygame

from keyboard import Keyboard
from instance import Instance
from util import Resolution, Text
from file import File

k = Keyboard()
f = File()
instance = Instance()
text = Text()

# pygame setup
pygame.init()
pygame.display.set_caption("The most advanced text editor in the world")
screen = pygame.display.set_mode((Resolution().x, Resolution().y))
clock = pygame.time.Clock()
font = pygame.font.Font(None, text.size)
running = True

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        # Keibord input
        elif event.type == pygame.MOUSEBUTTONDOWN:
            continue
            if event.button == 1:
                mouse_pos = event.pos

                line_num = int(mouse_pos[1] / text.line_height)

                if line_num < len(instance.rows):
                    instance.line_pos = line_num
                else:
                    instance.line_pos = len(instance.rows) - 1
                    instance.col_pos = len(instance.rows[-1])

                # current_line = "".join(instance.rows[line_num])
                # col_len = font.size(current_line)[0]
                # if col_len < mouse_pos[0]:
                #     instance.col_pos = len(current_line)
                # else:
                #     instance.col_pos = 0 # change this in the end 

                print(instance.line_pos, instance.col_pos)


        elif event.type == pygame.MOUSEWHEEL:
            if event.y == -1:
                text.root_y -= text.line_height
            elif event.y == 1:
                text.root_y += text.line_height

        elif event.type == pygame.DROPFILE:
            f.open(event.file, instance)

        elif event.type == pygame.KEYDOWN:
            if event.mod & pygame.KMOD_CTRL:
                if event.key == pygame.K_s:
                    # Make this gooder
                    file_name = f.browser_save()
                    with open(file_name, "w") as f:
                        for row in instance.rows:
                            f.write("".join(row))
                            f.write("\n")

                if event.key == pygame.K_o:
                    file_name = f.browser_open()
                    if file_name:
                        f.open(file_name, instance)

            if event.key == pygame.K_RETURN:
                k.new_line(instance)
            elif event.key == pygame.K_BACKSPACE:
                k.delete_line(instance)
            #elif event.unicode.isprintable(): # Prints ghost chars for shift, alt, etc.
            elif re.match(r'^[ -~]+$', event.unicode):
                k.insert_char(instance, event.unicode)
            elif event.key == pygame.K_TAB:
                for i in range(4):
                    k.insert_char(instance, " ")
            elif event.key == pygame.K_UP:
                k.up(instance)
            elif event.key == pygame.K_DOWN:
                k.down(instance)
            elif event.key == pygame.K_LEFT:
                k.left(instance)
            elif event.key == pygame.K_RIGHT:
                k.right(instance)

    screen.fill("black")

    # Render and blit every line one by one
    font_render_objs = []
    for i, row in enumerate(instance.rows):
        char_line = "".join(row)
        font_render_objs.append(font.render(char_line, True, (255, 255, 255)))
    
    for i, row in enumerate(font_render_objs):
        screen.blit(row, (0, text.line_height * i + text.root_y))

    # Cursor rendering
    text_before_cur = instance.rows[instance.line_pos][:instance.col_pos]
    cur_x = "".join(text_before_cur)
    cur_x = font.size(cur_x)[0]
    cur_rect = (cur_x, text.root_y + text.line_height*instance.line_pos, 10, text.line_height)
    pygame.draw.rect(screen, "white", cur_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
