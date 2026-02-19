import yaml
config = yaml.safe_load(open("config.yaml")) # Could to with with open


class Resolution:
    def __init__(self):
        self.x = config["res_x"]
        self.y = config["res_y"]

class Text():
    def __init__(self):
        self.root_x = config["text_root_x"]
        self.root_y = config["text_root_y"]
        self.size = config["text_size"]
        self.line_height = self.size / 2 + 8
