class RTG:
    d: dict

    def __init__(self, data) -> None:
        self.d = data

    def get_name(self):
        return self.d["speed"]

    def get_source_path(self):
        return f"texture_{ self.d["speed"] }"

    def get_dest_path(self):
        return f"texture_{ self.d["speed"] }"

    def get_shift(self):
        return 0

    def get_icon_width(self):
        return self.get_icons().__len__

    def single_icon(self):
        return False

    def get_icons(self):
        return [
            {
                "suffix": "_f",
                "source": "2.1",
                "dest": "0.0",
                "dest_cur": "2.0",
                "converts": ["to_n"],
            },
            {
                "suffix": "_c",
                "source": "2.1",
                "dest": "0.2",
                "dest_cur": "2.2",
                "converts": ["to_n"],
            },
            {
                "suffix": "_b",
                "source": "2.1",
                "dest": "0.4",
                "dest_cur": "2.4",
                "converts": ["to_n"],
            },
            {
                "suffix": "_s",
                "source": "2.1",
                "dest": "0.6",
                "dest_cur": "2.6",
                "converts": ["to_n"],
            },
        ]


class RTGRoad(RTG):
    pass


class RTGTexture(RTG):
    def get_name(self):
        return self.d["source"] + self.d["color"]

    def get_source_path(self):
        return f"texture_{ self.d["source"] }"

    def get_dest_path(self):
        return f"texture_{ self.get_name() }"

    def get_shift(self):
        match self.d["color"]:
            case 0:
                return 0  # 赤
            case 1:
                return 209  # 青
            case 2:
                return 145  # 緑
            case 3:
                return 41  # 黄
            case _:
                return 0

    def get_icons(self):
        return [
            {
                "suffix": "",
                "source": "2.1",
                "dest": "0.0",
                "dest_cur": "2.0",
                "converts": ["to_n"],
            },
        ]


class RTGSidewalk(RTG):
    def get_name(self):
        return self.d["source"]

    def get_source_path(self):
        return f"sidewalk_{ self.get_name() }"

    def get_dest_path(self):
        return f"sidewalk_{ self.get_name() }_{ self.d["layout"] }"

    def is_full_tile(self):
        return self.d["layout"] == "A"

    def get_source_location(self, loc: str):
        if self.is_full_tile():
            return "0.0"
        return loc

    def get_icons(self):
        return [
            {
                "suffix": "",
                "source": "0.0",
                "dest": "0.0",
                "dest_cur": "2.0",
                "converts": ["to_n"],
            },
        ]


class Merge:
    def __init__(self, data) -> None:
        self.d = data

    def get_source_path(self):
        return f"texture_{ self.d["source"] }"

    def get_dest_path(self):
        return f"texture_{ self.d["source"] }"

    def is_texture(self):
        return False


class MergeRoad(Merge):
    pass


class MergeTexture(Merge):
    def get_name(self):
        return self.d["source"] + self.d["color"]

    def get_source_path(self):
        return f"texture_{ self.get_name() }"

    def get_dest_path(self):
        return f"texture_{ self.get_name() }"

    def is_texture(self):
        return True


class MergeSidewalk(Merge):
    def get_name(self):
        return f"{ self.d["source"] }_{ self.d["layout"] }"

    def get_source_path(self):
        return f"sidewalk_{ self.get_name() }"

    def get_dest_path(self):
        return f"sidewalk_{ self.get_name() }"

    def is_texture(self):
        return True

class Dat:
    name: str
    d: dict

    def __init__(self, data) -> None:
        self.d = data

    def is_way_obj(self):
        return False

    def get_obj(self):
        return "way"

    def get_full_name(self):
        return f"{
            self.name} {
            self.d["speed"]} {
            self.d["system_type"]}{
                self.d["layout"]}"

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
        return f"texture_{ self.d["speed"] }"

    def get_images(self):

        return [
            ["image", "ns", self.get_image_path(), 0, 2, -64, -96],
            ["image", "ew", self.get_image_path(), 0, 3, -64, -96],
            ["image", "s", self.get_image_path(), 0, 5, -64, -96],
            ["image", "w", self.get_image_path(), 0, 6, -64, -96],
            ["image", "n", self.get_image_path(), 0, 7, -64, -96],
            ["image", "e", self.get_image_path(), 0, 8, -64, -96],
            ["image", "-", self.get_image_path(), 0, 9, -64, -96],
            ["imageup", "12", self.get_image_path(), 1, 0, -64, -88],
            ["imageup", "9", self.get_image_path(), 1, 1, -64, -88],
            ["imageup", "3", self.get_image_path(), 1, 2, -64, -88],
            ["imageup", "6", self.get_image_path(), 1, 3, -64, -88],
            ["imageup2", "12", self.get_image_path(), 1, 5, -64, -80],
            ["imageup2", "9", self.get_image_path(), 1, 6, -64, -80],
            ["imageup2", "3", self.get_image_path(), 1, 7, -64, -80],
            ["imageup2", "6", self.get_image_path(), 1, 8, -64, -80],
            ["diagonal", "sw", self.get_image_path(), self.get_sw_nw_y(), 0, -64, -96],
            ["diagonal", "nw", self.get_image_path(), self.get_sw_nw_y(), 1, -64, -96],
            ["diagonal", "ne", self.get_image_path(), self.get_ne_se_y(), 2, -64, -96],
            ["diagonal", "se", self.get_image_path(), self.get_ne_se_y(), 3, -64, -96],
            ["image", "sw", self.get_image_path(), self.get_sw_nw_y(), 0, -64, -96],
            ["image", "nw", self.get_image_path(), self.get_sw_nw_y(), 1, -64, -96],
            ["image", "ne", self.get_image_path(), self.get_ne_se_y(), 2, -64, -96],
            ["image", "se", self.get_image_path(), self.get_ne_se_y(), 3, -64, -96],
            ["image", "new", self.get_image_path(), 4, 0, -64, -96],
            ["image", "nse", self.get_image_path(), 4, 1, -64, -96],
            ["image", "sew", self.get_image_path(), 4, 2, -64, -96],
            ["image", "nsw", self.get_image_path(), 4, 3, -64, -96],
            ["image", "nsew", self.get_image_path(), 4, 4, -64, -96],
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
            ["image", "sw", self.get_image_path(), self.get_sw_nw_y(), 5, -64, -96],
            ["image", "nw", self.get_image_path(), self.get_sw_nw_y(), 6, -64, -96],
            ["image", "ne", self.get_image_path(), self.get_ne_se_y(), 7, -64, -96],
            ["image", "se", self.get_image_path(), self.get_ne_se_y(), 8, -64, -96],
        ]
        return images


class DatTi(Dat):
    name = "Ti"

    def is_way_obj(self):
        return self.d["way_type"] != "T"

    def get_waytype(self):
        if self.is_way_obj():
            return "road"
        return "tram_track"

    def get_obj(self):
        if self.is_way_obj():
            return "way-object"
        return "way"
        
    def get_full_name(self):
        return f"{self.name} {self.get_name()}{self.d["way_type"]}"

    def get_name(self):
        match self.d["speed"]:
            case 3000:
                return self.d["texture"]
            case 6000:
                return self.d["texture"] + 50
            case _:
                return self.d["texture"]

    def get_system_type(self):
        return 0

    def get_topspeed(self):
        return self.d["speed"]

    def get_cost(self):
        return 5000

    def get_maintenance(self):
        return 100

    def get_icon_index(self):
        return 0

    def get_image_path(self):
        return f"texture_{ self.d["texture"] }"

    def get_image_name(self, name):
        if self.is_way_obj():
            return f"back{name}"
        return name

    def get_images(self):
        name = self.get_image_name
        path = self.get_image_path
        return [
            [name("image"), "ns", path(), 0, 2, -64, -96],
            [name("image"), "ew", path(), 0, 3, -64, -96],
            [name("image"), "s", path(), 0, 5, -64, -96],
            [name("image"), "w", path(), 0, 6, -64, -96],
            [name("image"), "n", path(), 0, 7, -64, -96],
            [name("image"), "e", path(), 0, 8, -64, -96],
            [name("image"), "-", path(), 0, 9, -64, -96],
            [name("imageup"), "12", path(), 1, 0, -64, -88],
            [name("imageup"), "9", path(), 1, 1, -64, -88],
            [name("imageup"), "3", path(), 1, 2, -64, -88],
            [name("imageup"), "6", path(), 1, 3, -64, -88],
            [name("imageup2"), "12", path(), 1, 5, -64, -80],
            [name("imageup2"), "9", path(), 1, 6, -64, -80],
            [name("imageup2"), "3", path(), 1, 7, -64, -80],
            [name("imageup2"), "6", path(), 1, 8, -64, -80],
            [name("diagonal"), "sw", path(), 2, 0, -64, -96],
            [name("diagonal"), "nw", path(), 2, 1, -64, -96],
            [name("diagonal"), "ne", path(), 2, 2, -64, -96],
            [name("diagonal"), "se", path(), 2, 3, -64, -96],
            [name("image"), "sw", path(), 2, self.get_curve_x(0), -64, -96],
            [name("image"), "nw", path(), 2, self.get_curve_x(1), -64, -96],
            [name("image"), "ne", path(), 2, self.get_curve_x(2), -64, -96],
            [name("image"), "se", path(), 2, self.get_curve_x(3), -64, -96],
            [name("image"), "new", path(), 4, 0, -64, -96],
            [name("image"), "nse", path(), 4, 1, -64, -96],
            [name("image"), "sew", path(), 4, 2, -64, -96],
            [name("image"), "nsw", path(), 4, 3, -64, -96],
            [name("image"), "nsew", path(), 4, 4, -64, -96],
        ]

    def get_curve_x(self, x: int):
        """
        直角カーブは曲線
        """
        return x if self.d["speed"] == 6000 else x + 5


class DatTiSingle(DatTi):
    def get_full_name(self):
        return f"{self.name} {self.get_name()} {self.d["layout"]}{self.d["way_type"]}"

    def get_image_path(self):
        """
        方角によっては左右が反転する
        """
        if self.d["layout"] == "B":
            return f"texture_{self.d["texture"] + 10}"
        return f"texture_{self.d["texture"]}"

    def flip(self):
        if self.d["layout"] == "F":
            return f"texture_{self.d["texture"] + 10}"
        return f"texture_{self.d["texture"]}"

    def get_images(self):
        name = self.get_image_name
        path = self.get_image_path
        images = super().get_images()
        images[4:6] = [
            [name("image"), "n", self.flip(), 0, 7, -64, -96],
            [name("image"), "e", self.flip(), 0, 8, -64, -96],
        ]
        images[15:23] = [
            [name("diagonal"), "sw", path(), 2, 0, -64, -96],
            [name("diagonal"), "nw", path(), 2, 1, -64, -96],
            [name("diagonal"), "ne", self.flip(), 2, 2, -64, -96],
            [name("diagonal"), "se", self.flip(), 2, 3, -64, -96],
            [name("image"), "sw", path(), 2, self.get_curve_x(0), -64, -96],
            [name("image"), "nw", path(), 2, self.get_curve_x(1), -64, -96],
            [name("image"), "ne", self.flip(), 2, self.get_curve_x(2), -64, -96],
            [name("image"), "se", self.flip(), 2, self.get_curve_x(3), -64, -96],
        ]
        return images


class DatFX(DatTi):
    name = "FX"

    def is_way_obj(self):
        return self.d["layout"] != "A"

    def get_waytype(self):
        if self.is_way_obj():
            return "road"
        return "water"

    def get_obj(self):
        if self.is_way_obj():
            return "way-object"
        return "way"

    def get_full_name(self):
        return f"{ self.name } { self.d["texture"] } { self.d["layout"] }"

    def get_image_path(self):
        return f"sidewalk_{ self.d["texture"] }_{ self.d["layout"] }"

    def get_image_name(self, name):
        if self.is_way_obj():
            return f"back{name}"
        return name

    def get_images(self):
        name = self.get_image_name
        path = self.get_image_path
        return [
            [name("image"), "ns", path(), 0, 2, -64, -96],
            [name("image"), "ew", path(), 0, 3, -64, -96],
            [name("image"), "s", path(), 0, 5, -64, -96],
            [name("image"), "w", path(), 0, 6, -64, -96],
            [name("image"), "n", path(), 0, 7, -64, -96],
            [name("image"), "e", path(), 0, 8, -64, -96],
            [name("image"), "-", path(), 0, 9, -64, -96],
            [name("imageup"), "12", path(), 1, 0, -64, -88],
            [name("imageup"), "9", path(), 1, 1, -64, -88],
            [name("imageup"), "3", path(), 1, 2, -64, -88],
            [name("imageup"), "6", path(), 1, 3, -64, -88],
            [name("imageup2"), "12", path(), 1, 5, -64, -80],
            [name("imageup2"), "9", path(), 1, 6, -64, -80],
            [name("imageup2"), "3", path(), 1, 7, -64, -80],
            [name("imageup2"), "6", path(), 1, 8, -64, -80],
            [name("diagonal"), "sw", path(), 2, 0, -64, -96],
            [name("diagonal"), "nw", path(), 2, 1, -64, -96],
            [name("diagonal"), "ne", path(), 2, 2, -64, -96],
            [name("diagonal"), "se", path(), 2, 3, -64, -96],
            [name("image"), "sw", path(), self.get_sw_nw_y(), 5, -64, -96],
            [name("image"), "nw", path(), self.get_sw_nw_y(), 6, -64, -96],
            [name("image"), "ne", path(), self.get_ne_se_y(), 7, -64, -96],
            [name("image"), "se", path(), self.get_ne_se_y(), 8, -64, -96],
            [name("image"), "new", path(), 4, 0, -64, -96],
            [name("image"), "nse", path(), 4, 1, -64, -96],
            [name("image"), "sew", path(), 4, 2, -64, -96],
            [name("image"), "nsw", path(), 4, 3, -64, -96],
            [name("image"), "nsew", path(), 4, 4, -64, -96],
        ]
