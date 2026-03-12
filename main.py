import re

import pygame

from keyboard import Keyboard
from instance import Instance
from text import Text
from util import Resolution
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

def text_width_before_cur():
    text_before_cur = instance.rows[instance.line_pos][:instance.col_pos]
    cur_x = "".join(text_before_cur)
    return font.size(cur_x)[0]

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        # Keibord input
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                print(mouse_pos)

                line_num = int(mouse_pos[1] / text.line_height) - text.scroll_dist

                if line_num > len(instance.rows):
                    instance.line_pos = len(instance.rows) - 1
                    instance.col_pos = len(instance.rows[-1])
                else:
                    instance.line_pos = line_num

                    current_line = "".join(instance.rows[instance.line_pos])
                    col_width_px = font.size(current_line)[0]
                    if col_width_px <= mouse_pos[0]:
                        instance.col_pos = instance.current_line_length()
                    else:
                        # Damm, this fucking sucks
                        instance.col_pos = int((mouse_pos[0] / col_width_px) * instance.current_line_length())
                        # tmp_col_pos = instance.col_pos
                        instance.col_pos -= 1
                        col_width_m1_char = text_width_before_cur()
                        instance.col_pos += 2
                        col_width_p1_char = text_width_before_cur()
                        instance.col_pos -= 1

                        # while mouse_pos[0] !< col_width_p1_char && mouse_pos[0] !> col_width_m1_char:
                        #     if mouse_pos > col_width_p1_char:
                        #
                        # recalculated_col_width_px = text_width_before_cur()

                        # avg_char_width = int(col_width_px / instance.current_line_length())
                        # instance.col_pos = int(col_width_px / avg_char_width)
                        # text_before_cur = instance.rows[instance.line_pos][:instance.col_pos]
                        # instance.col_pos = 0 # change this in the end 

                        # print("cursor pos:")
                        # print(instance.line_pos, instance.col_pos)
                        # print("text last x pos:")
                        # print(recalculated_col_width_px)
                        # print("Mouse x pos:")
                        # print(mouse_pos[0])


        elif event.type == pygame.MOUSEWHEEL:
            text.scroll(instance, event.y)

        elif event.type == pygame.DROPFILE:
            f.open(event.file, instance)

        elif event.type == pygame.KEYDOWN:
            print(instance.line_pos, instance.col_pos)
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
    cur_rect = (text_width_before_cur(), text.root_y + text.line_height*instance.line_pos, 10, text.line_height)

    # Blinking
    time = pygame.time.get_ticks()
    blink_interval = time // 1000
    if blink_interval % 2:
        pygame.draw.rect(screen, "white", cur_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
