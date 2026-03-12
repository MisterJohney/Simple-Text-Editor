import yaml
config = yaml.safe_load(open("config.yaml")) # Could to with with open


class Resolution:
    def __init__(self):
        self.x = config["res_x"]
        self.y = config["res_y"]
