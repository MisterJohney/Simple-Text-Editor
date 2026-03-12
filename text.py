import yaml
config = yaml.safe_load(open("config.yaml")) # Could to with with open

class Text():
    def __init__(self):
        self.size = config["text_size"]
        self.line_height = self.size / 2 + 8
        self.scroll_dist = 0
        self.root_x = config["text_root_x"]
        self.root_y = config["text_root_y"]

    def scroll(self, instance, direction):
        if direction == -1:
            self.scroll_dist -= 1
        else:
            if self.scroll_dist < 0:
                self.scroll_dist += 1


        self.root_y = config["text_root_y"] + self.scroll_dist * self.line_height

