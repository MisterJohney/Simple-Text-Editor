import re
from tkinter import filedialog
import yaml
import math

import pygame

from keyboard import Keyboard
from instance import Instance

config = yaml.safe_load(open("config.yaml")) # Could to with with open

resolution = (config["res_x"],config["res_y"])
text_root = [config["text_root_x"], config["text_root_y"]]
text_size = config["text_size"]
line_height = text_size / 2 + 8
k = Keyboard()
instance = Instance();

# pygame setup
pygame.init()
pygame.display.set_caption("The most advanced text editor in the world")
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
font = pygame.font.Font(None, text_size)
running = True

def open_file(file_name):
    try:
        with open(file_name, "r") as f:
            instance.rows = []
            for line in f:
                instance.rows.append(list(line.rstrip()))
            instance.line_pos = len(instance.rows) - 1
            instance.col_pos = len(instance.rows[-1])
        
    except Exception as e:
        print(e)


def browser_open_file():
    return filedialog.askopenfilename(initialdir = "~/projects/python/simple_text_edit/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

def browser_save_file():
    files = [('Text Document', '*.txt'), 
             ('All Files', '*.*')]
    file_name = filedialog.asksaveasfile(mode="w", filetypes = files, defaultextension = files)
    if file_name is None:
        return
    return file_name.name

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        # Keibord input
        elif event.type == pygame.MOUSEBUTTONDOWN:
            continue
            if event.button == 1:
                mouse_pos = event.pos



                line_num = int(mouse_pos[1] / line_height)

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
                text_root[1] -= line_height
            elif event.y == 1:
                text_root[1] += line_height

        elif event.type == pygame.DROPFILE:
            open_file(event.file)

        elif event.type == pygame.KEYDOWN:
            if event.mod & pygame.KMOD_CTRL:
                if event.key == pygame.K_s:
                    # Make this gooder
                    file_name = browser_save_file()
                    with open(file_name, "w") as f:
                        for row in instance.rows:
                            f.write("".join(row))
                            f.write("\n")

                if event.key == pygame.K_o:
                    file_name = browser_open_file()
                    if file_name:
                        open_file(file_name)

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

    font_render_objs = []
    for i, row in enumerate(instance.rows):
        text = "".join(row)
        font_render_objs.append(font.render(text, True, (255, 255, 255)))
    
    # True Rendering starts here
    for i, row in enumerate(font_render_objs):
        screen.blit(row, (0, line_height * i + text_root[1]))

    text_before_cur = instance.rows[instance.line_pos][:instance.col_pos]
    cur_x = "".join(text_before_cur)
    cur_x = font.size(cur_x)[0]
    cur_rect = (cur_x, text_root[1] + line_height*instance.line_pos, 10, line_height)
    pygame.draw.rect(screen, "white", cur_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
