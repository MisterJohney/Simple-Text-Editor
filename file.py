from tkinter import filedialog

class File:
    def __init__(self):
        pass

    def open(self, file_name, instance):
        try:
            with open(file_name, "r") as f:
                instance.rows = []
                for line in f:
                    instance.rows.append(list(line.rstrip()))
                instance.line_pos = len(instance.rows) - 1
                instance.col_pos = len(instance.rows[-1])
            
        except Exception as e:
            print(e)


    def browser_open(self):
        return filedialog.askopenfilename(initialdir = "~/projects/python/simple_text_edit/",
                                              title = "Select a File",
                                              filetypes = (("Text files",
                                                            "*.txt*"),
                                                           ("all files",
                                                            "*.*")))

    def browser_save(self):
        files = [('Text Document', '*.txt'), 
                 ('All Files', '*.*')]
        file_name = filedialog.asksaveasfile(mode="w", filetypes = files, defaultextension = files)
        if file_name is None:
            return
        return file_name.name
