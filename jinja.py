"""
workspace内のj2ファイルをレンダリングする。標準出力に出るのでいい感じにファイル出力してください。
"""

import argparse
import sys
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

class RTG:
    d: dict
    def __init__(self, data) -> None:
        self.d = data

    def get_name(self):
        return self.d["speed"]

    def get_source(self):
        return self.d["speed"]

    def get_shift(self):
        return 0

    def get_icon_width(self):
        return 1024
    
    def single_icon(self):
        return False

class RTGRoad(RTG):
    pass

class RTGTexture(RTG):
    def get_name(self):
        return self.d["source"]+self.d["color"]

    def get_source(self):
        return self.d["source"]

    def get_shift(self):
        match self.d["color"]:
            case 0:
                return 0
            case 1:
                return 209
            case 2:
                return 145
            case 3:
                return 41
            case _:
                return 0


    def get_icon_width(self):
        return 256

    def single_icon(self):
        return True

class Dat:
    name: str
    d: dict

    def __init__(self, data) -> None:
        self.d = data

    def get_full_name(self):
        return f"{self.name} {self.d["speed"]} {self.d["system_type"]}{self.d["layout"]}"

    def get_system_type(self):
        match self.d["system_type"]:
            case "G":
                return 0
            case "E":
                return 1

    def get_waytype(self):
        return "road"

    def get_topspeed(self):
        return self.d["speed"]

    def get_cost(self):
        return self.d["speed"] * 50 * (1 if self.d["system_type"] == "G" else 5)

    def get_maintenance(self):
        return self.d["speed"] * (1 if self.d["system_type"] == "G" else 5)

    def get_icon_index(self):
        match self.d["layout"]:
            case "F":
                return 0
            case "C":
                return 1
            case "B":
                return 2
            case "S":
                return 3
            case _:
                return 0

    def get_image_path(self):
        return self.d["speed"]

    def get_images(self):
        return [
            ["image", "ns", self.get_image_path(), 0,2,-64,-96],
            ["image", "ew", self.get_image_path(), 0,3,-64,-96],
            ["image", "s", self.get_image_path(), 0,5,-64,-96],
            ["image", "w", self.get_image_path(), 0,6,-64,-96],
            ["image", "n", self.get_image_path(), 0,7,-64,-96],
            ["image", "e", self.get_image_path(), 0,8,-64,-96],
            ["image", "-", self.get_image_path(), 0,9,-64,-96],
            ["imageup", "12", self.get_image_path(), 1,0,-64,-88],
            ["imageup", "9", self.get_image_path(), 1,1,-64,-88],
            ["imageup", "3", self.get_image_path(), 1,2,-64,-88],
            ["imageup", "6", self.get_image_path(), 1,3,-64,-88],
            ["imageup2", "12", self.get_image_path(), 1,5,-64,-80],
            ["imageup2", "9", self.get_image_path(), 1,6,-64,-80],
            ["imageup2", "3", self.get_image_path(), 1,7,-64,-80],
            ["imageup2", "6", self.get_image_path(), 1,8,-64,-80],
            ["diagonal", "sw", self.get_image_path(), self.get_sw_nw_y(),0,-64,-96],
            ["diagonal", "nw", self.get_image_path(), self.get_sw_nw_y(),1,-64,-96],
            ["diagonal", "ne", self.get_image_path(), self.get_ne_se_y(),2,-64,-96],
            ["diagonal", "se", self.get_image_path(), self.get_ne_se_y(),3,-64,-96],
            ["image", "sw", self.get_image_path(), self.get_sw_nw_y(), 0, -64, -96],
            ["image", "nw", self.get_image_path(), self.get_sw_nw_y(), 1, -64, -96],
            ["image", "ne", self.get_image_path(), self.get_ne_se_y(), 2, -64, -96],
            ["image", "se", self.get_image_path(), self.get_ne_se_y(), 3, -64, -96],
            ["image", "new", self.get_image_path(), 4,0,-64,-96],
            ["image", "nse", self.get_image_path(), 4,1,-64,-96],
            ["image", "sew", self.get_image_path(), 4,2,-64,-96],
            ["image", "nsw", self.get_image_path(), 4,3,-64,-96],
            ["image", "nsew", self.get_image_path(), 4,4,-64,-96],
        ]

    def get_sw_nw_y(self):
        """
        中央と奥はベース表示
        """
        if self.d["layout"] in ("C", "B"):
            return 2
        return 3

    def get_ne_se_y(self):
        """
        中央と手前はベース表示
        """
        if self.d["layout"] in ("C", "F"):
            return 2
        return 3

    def get_curve_x(self, x: int):
        return x


class DatRTX(Dat):
    name = "RTX"


class DatGTX(Dat):
    name = "GTX"

    def get_images(self):
        """
        直角カーブは曲線
        """
        images = super().get_images()
        images[19:23] = [
            ["image", "sw", self.get_image_path(), self.get_sw_nw_y() , 5 ,-64,-96],
            ["image", "nw", self.get_image_path(), self.get_sw_nw_y() , 6 ,-64,-96],
            ["image", "ne", self.get_image_path(), self.get_ne_se_y() , 7 ,-64,-96],
            ["image", "se", self.get_image_path(), self.get_ne_se_y() , 8 ,-64,-96],
        ]
        return images


class DatTi(Dat):
    name = "Ti"
    def get_full_name(self):
        return f"{self.name} {self.get_name()} {self.d["layout"]}"

    def get_name(self):
        match self.d["speed"]:
            case 3000:
                return self.d["texture"]
            case 6000:
                return self.d["texture"]+50
            case _:
                return self.d["texture"]

    def get_system_type(self):
        return 0

    def get_waytype(self):
        return "tram_track"

    def get_topspeed(self):
        return self.d["speed"]

    def get_cost(self):
        return 5000

    def get_maintenance(self):
        return 100

    def get_icon_index(self):
        return 0

    def get_image_path(self):
        """
        方角によっては左右が反転する
        """
        if self.d["layout"] == "B":
            return self.d["texture"]+10
        return self.d["texture"]

    def flip(self):
        if self.d["layout"] == "F":
            return self.d["texture"]+10
        return self.d["texture"]

    def get_images(self):
        return [
            ["image", "ns", self.get_image_path(), 0,2,-64,-96],
            ["image", "ew", self.get_image_path(), 0,3,-64,-96],
            ["image", "s", self.get_image_path(), 0,5,-64,-96],
            ["image", "w", self.get_image_path(), 0,6,-64,-96],
            ["image", "n", self.flip(), 0,7,-64,-96],
            ["image", "e", self.flip(), 0,8,-64,-96],
            ["image", "-", self.get_image_path(), 0,9,-64,-96],
            ["imageup", "12", self.get_image_path(), 1,0,-64,-88],
            ["imageup", "9", self.get_image_path(), 1,1,-64,-88],
            ["imageup", "3", self.get_image_path(), 1,2,-64,-88],
            ["imageup", "6", self.get_image_path(), 1,3,-64,-88],
            ["imageup2", "12", self.get_image_path(), 1,5,-64,-80],
            ["imageup2", "9", self.get_image_path(), 1,6,-64,-80],
            ["imageup2", "3", self.get_image_path(), 1,7,-64,-80],
            ["imageup2", "6", self.get_image_path(), 1,8,-64,-80],
            ["diagonal", "sw", self.get_image_path(), 2, 0,-64,-96],
            ["diagonal", "nw", self.get_image_path(), 2, 1,-64,-96],
            ["diagonal", "ne", self.flip(), 2, 2,-64,-96],
            ["diagonal", "se", self.flip(), 2, 3,-64,-96],
            ["image", "sw", self.get_image_path(), 2, self.get_curve_x(0), -64, -96],
            ["image", "nw", self.get_image_path(), 2, self.get_curve_x(1), -64, -96],
            ["image", "ne", self.flip(), 2, self.get_curve_x(2), -64, -96],
            ["image", "se", self.flip(), 2, self.get_curve_x(3), -64, -96],
            ["image", "new", self.get_image_path(), 4,0,-64,-96],
            ["image", "nse", self.get_image_path(), 4,1,-64,-96],
            ["image", "sew", self.get_image_path(), 4,2,-64,-96],
            ["image", "nsw", self.get_image_path(), 4,3,-64,-96],
            ["image", "nsew", self.get_image_path(), 4,4,-64,-96],
        ]


    def get_curve_x(self, x: int):
        """
        直角カーブは曲線
        """
        return x if self.d["speed"] == 6000 else x+5



import itertools


def resolve_class(defs: list):
    resolved = []
    for d in defs:
        pattern = d.get("pattern")
        keys = pattern.keys()
        combinations = itertools.product(*pattern.values())
        matrix = [dict(zip(keys, combo)) for combo in combinations]
        for m in matrix:
            resolved.append(getattr(sys.modules[__name__], d.get("className"))(m))
    return resolved


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="jinjaテンプレートをレンダリングする")
    parser.add_argument("file_name", help="ファイルのパス")
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader("workspace"), autoescape=select_autoescape()
    )

    def pad(value, width, char="_"):
        """
        指定文字で字詰めする
        """
        return str(value).zfill(width).replace("0", char, width - len(str(value)))

    env.filters["pad"] = pad

    template = env.get_template(args.file_name)

    with open("./workspace/projects.yml", "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    meta = {
        "meta": {
            "system_types": {
                "G": {"id": 0, "cost": 1},
                "E": {"id": 1, "cost": 5},
            },
        },
        "rtgs": resolve_class(data["rtgs"]),
        "dats": resolve_class(data["dats"]),
    }
    print(template.render(data | meta))
