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

    def get_rules(self):
        return [
            ["ns", "2.1", "0.2", ["to_n"]],
            ["ew", "2.1", "0.3", ["to_e"]],
            ["s", "0.1", "0.5", ["to_n"]],
            ["w", "0.1", "0.6", ["to_e"]],
            ["n", "0.1", "0.7", ["to_s"]],
            ["e", "0.1", "0.8", ["to_w"]],
            ["-", "0.0", "0.9", ["to_n"]],
            ["up_12", "3.2", "1.0", ["to_n", "to_up"]],
            ["up_9", "3.2", "1.1", ["to_w", "to_up"]],
            ["up_3", "2.2", "1.2", ["to_s", "to_up"]],
            ["up_6", "2.2", "1.3", ["to_e", "to_up"]],
            ["up2_12", "3.2", "1.5", ["to_n", "[to_up, 2]"]],
            ["up2_9", "3.2", "1.6", ["to_w", "[to_up, 2]"]],
            ["up2_3", "2.2", "1.7", ["to_s", "[to_up, 2]"]],
            ["up2_6", "2.2", "1.8", ["to_e", "[to_up, 2]"]],
            ["d_sw", "2.0", "2.0", ["to_e"]],
            ["d_nw", "2.0", "2.1", ["to_s"]],
            ["d_ne", "2.0", "2.2", ["to_w"]],
            ["d_se", "2.0", "2.3", ["to_n"]],
            ["sw", "1.0", "2.5", ["to_e"]],
            ["nw", "1.0", "2.6", ["to_s"]],
            ["ne", "1.0", "2.7", ["to_w"]],
            ["se", "1.0", "2.8", ["to_n"]],
            ["d_edge_sw", "2.0", "3.0", ["to_e"]],
            ["d_edge_nw", "2.0", "3.1", ["to_s"]],
            ["d_edge_ne", "2.0", "3.2", ["to_w"]],
            ["d_edge_se", "2.0", "3.3", ["to_n"]],
            ["edge_sw", "1.0", "3.5", ["to_e"]],
            ["edge_nw", "1.0", "3.6", ["to_s"]],
            ["edge_ne", "1.0", "3.7", ["to_w"]],
            ["edge_se", "1.0", "3.8", ["to_n"]],
            ["new", "1.2", "4.0", ["to_e"]],
            ["nse", "1.2", "4.1", ["to_s"]],
            ["sew", "1.2", "4.2", ["to_w"]],
            ["nsw", "1.2", "4.3", ["to_n"]],
            ["nsew", "1.1", "4.4", ["to_n"]],
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
            }
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

    def get_icons(self):
        match self.d["layout"]:
            case "A":
                return [
                    {
                        "suffix": "",
                        "source": "1.4",
                        "dest": "0.0",
                        "dest_cur": "2.0",
                        "converts": ["to_n"],
                    },
                ]
            case _:
                return [
                    {
                        "suffix": "_f",
                        "source": "1.4",
                        "dest": "0.0",
                        "dest_cur": "2.0",
                        "converts": ["to_n"],
                    },
                    {
                        "suffix": "_c",
                        "source": "1.4",
                        "dest": "0.2",
                        "dest_cur": "2.2",
                        "converts": ["to_n"],
                    },
                    {
                        "suffix": "_b",
                        "source": "1.4",
                        "dest": "0.4",
                        "dest_cur": "2.4",
                        "converts": ["to_n"],
                    },
                    {
                        "suffix": "_s",
                        "source": "1.4",
                        "dest": "0.6",
                        "dest_cur": "2.6",
                        "converts": ["to_n"],
                    },
                ]

    def get_rules(self):
        match self.d["layout"]:
            case "A":
                return [
                    ["ns", "1.4", "0.2", ["to_n"]],
                    ["ew", "1.4", "0.3", ["to_e"]],
                    ["s", "1.4", "0.5", ["to_n"]],
                    ["w", "1.4", "0.6", ["to_e"]],
                    ["n", "1.4", "0.7", ["to_s"]],
                    ["e", "1.4", "0.8", ["to_w"]],
                    ["-", "1.4", "0.9", ["to_n"]],
                    ["up_12", "2.4", "1.0", ["to_n", "to_up"]],
                    ["up_9", "2.4", "1.1", ["to_w", "to_up"]],
                    ["up_3", "3.4", "1.2", ["to_s", "to_up"]],
                    ["up_6", "3.4", "1.3", ["to_e", "to_up"]],
                    ["up2_12", "2.4", "1.5", ["to_n", "[to_up, 2]"]],
                    ["up2_9", "2.4", "1.6", ["to_w", "[to_up, 2]"]],
                    ["up2_3", "3.4", "1.7", ["to_s", "[to_up, 2]"]],
                    ["up2_6", "3.4", "1.8", ["to_e", "[to_up, 2]"]],
                    ["d_sw", "1.4", "2.0", ["to_e"]],
                    ["d_nw", "1.4", "2.1", ["to_s"]],
                    ["d_ne", "1.4", "2.2", ["to_w"]],
                    ["d_se", "1.4", "2.3", ["to_n"]],
                    ["sw", "1.4", "2.5", ["to_e"]],
                    ["nw", "1.4", "2.6", ["to_s"]],
                    ["ne", "1.4", "2.7", ["to_w"]],
                    ["se", "1.4", "2.8", ["to_n"]],
                    ["new", "1.4", "4.0", ["to_e"]],
                    ["nse", "1.4", "4.1", ["to_s"]],
                    ["sew", "1.4", "4.2", ["to_w"]],
                    ["nsw", "1.4", "4.3", ["to_n"]],
                    ["nsew", "1.4", "4.4", ["to_n"]],
                ]
            case "F":
                return [
                    ["ns_f", "1.3", "0.2", ["to_n"]],
                    ["ew_f", "1.3", "0.3", ["to_e"]],
                    ["s", "0.3", "0.5", ["to_n"]],
                    ["w", "0.2", "0.6", ["to_e"]],
                    ["n", "0.2", "0.7", ["to_s"]],
                    ["e", "0.3", "0.8", ["to_w"]],
                    ["-", "1.4", "0.9", ["to_n"]],
                    ["up_12_f", "3.3", "1.0", ["to_n", "to_up"]],
                    ["up_9_f", "3.2", "1.1", ["to_w", "to_up"]],
                    ["up_3_f", "2.2", "1.2", ["to_s", "to_up"]],
                    ["up_6_f", "2.3", "1.3", ["to_e", "to_up"]],
                    ["up2_12_f", "3.3", "1.5", ["to_n", "[to_up, 2]"]],
                    ["up2_9_f", "3.2", "1.6", ["to_w", "[to_up, 2]"]],
                    ["up2_3_f", "2.2", "1.7", ["to_s", "[to_up, 2]"]],
                    ["up2_6_f", "2.3", "1.8", ["to_e", "[to_up, 2]"]],
                    ["d_sw_f", "3.0", "2.0", ["to_e"]],
                    ["d_nw_f", "3.0", "2.1", ["to_s"]],
                    ["d_ne_f", "3.1", "2.2", ["to_w"]],
                    ["d_se_f", "3.1", "2.3", ["to_n"]],
                    ["sw_f", "2.0", "2.5", ["to_e"]],
                    ["nw_f", "2.0", "2.6", ["to_s"]],
                    ["ne_f", "2.1", "2.7", ["to_w"]],
                    ["se_f", "2.1", "2.8", ["to_n"]],
                    ["new_f", "1.3", "4.0", ["to_e"]],
                    ["nse_f", "1.0", "4.1", ["to_s"]],
                    ["sew_f", "1.0", "4.2", ["to_w"]],
                    ["nsw_f", "1.3", "4.3", ["to_n"]],
                    ["nsew_f", "1.1", "4.4", ["to_n"]],
                ]
            case "B":
                return [
                    ["ns_b", "1.2", "0.2", ["to_n"]],
                    ["ew_b", "1.2", "0.3", ["to_e"]],
                    ["s", "0.2", "0.5", ["to_n"]],
                    ["w", "0.3", "0.6", ["to_e"]],
                    ["n", "0.3", "0.7", ["to_s"]],
                    ["e", "0.2", "0.8", ["to_w"]],
                    ["-", "1.4", "0.9", ["to_n"]],
                    ["up_12_b", "3.2", "1.0", ["to_n", "to_up"]],
                    ["up_9_b", "3.3", "1.1", ["to_w", "to_up"]],
                    ["up_3_b", "2.3", "1.2", ["to_s", "to_up"]],
                    ["up_6_b", "2.2", "1.3", ["to_e", "to_up"]],
                    ["up2_12_b", "3.2", "1.5", ["to_n", "[to_up, 2]"]],
                    ["up2_9_b", "3.3", "1.6", ["to_w", "[to_up, 2]"]],
                    ["up2_3_b", "2.3", "1.7", ["to_s", "[to_up, 2]"]],
                    ["up2_6_b", "2.2", "1.8", ["to_e", "[to_up, 2]"]],
                    ["d_sw_b", "3.1", "2.0", ["to_e"]],
                    ["d_nw_b", "3.1", "2.1", ["to_s"]],
                    ["d_ne_b", "3.0", "2.2", ["to_w"]],
                    ["d_se_b", "3.0", "2.3", ["to_n"]],
                    ["sw_b", "2.1", "2.5", ["to_e"]],
                    ["nw_b", "2.1", "2.6", ["to_s"]],
                    ["ne_b", "2.0", "2.7", ["to_w"]],
                    ["se_b", "2.0", "2.8", ["to_n"]],
                    ["new_b", "1.0", "4.0", ["to_e"]],
                    ["nse_b", "1.3", "4.1", ["to_s"]],
                    ["sew_b", "1.3", "4.2", ["to_w"]],
                    ["nsw_b", "1.0", "4.3", ["to_n"]],
                    ["nsew_b", "1.0", "4.4", ["to_n"]],
                ]
            case _:
                return [
                    ["ns_f", "1.3", "0.2", ["to_n"]],
                    ["ns_b", "1.2", "0.2", ["to_n"]],
                    ["ew_f", "1.3", "0.3", ["to_e"]],
                    ["ew_b", "1.2", "0.3", ["to_e"]],
                    ["s", "0.1", "0.5", ["to_n"]],
                    ["w", "0.1", "0.6", ["to_e"]],
                    ["n", "0.1", "0.7", ["to_s"]],
                    ["e", "0.1", "0.8", ["to_w"]],
                    ["-", "1.4", "0.9", ["to_n"]],
                    ["up_12_f", "3.3", "1.0", ["to_n", "to_up"]],
                    ["up_12_b", "3.2", "1.0", ["to_n", "to_up"]],
                    ["up_9_f", "3.2", "1.1", ["to_w", "to_up"]],
                    ["up_9_b", "3.3", "1.1", ["to_w", "to_up"]],
                    ["up_3_f", "2.2", "1.2", ["to_s", "to_up"]],
                    ["up_3_b", "2.3", "1.2", ["to_s", "to_up"]],
                    ["up_6_f", "2.3", "1.3", ["to_e", "to_up"]],
                    ["up_6_b", "2.2", "1.3", ["to_e", "to_up"]],
                    ["up2_12_f", "3.3", "1.5", ["to_n", "[to_up, 2]"]],
                    ["up2_12_b", "3.2", "1.5", ["to_n", "[to_up, 2]"]],
                    ["up2_9_f", "3.2", "1.6", ["to_w", "[to_up, 2]"]],
                    ["up2_9_b", "3.3", "1.6", ["to_w", "[to_up, 2]"]],
                    ["up2_3_f", "2.2", "1.7", ["to_s", "[to_up, 2]"]],
                    ["up2_3_b", "2.3", "1.7", ["to_s", "[to_up, 2]"]],
                    ["up2_6_f", "2.3", "1.8", ["to_e", "[to_up, 2]"]],
                    ["up2_6_b", "2.2", "1.8", ["to_e", "[to_up, 2]"]],
                    ["d_sw_f", "3.0", "2.0", ["to_e"]],
                    ["d_sw_b", "3.1", "2.0", ["to_e"]],
                    ["d_nw_f", "3.0", "2.1", ["to_s"]],
                    ["d_nw_b", "3.1", "2.1", ["to_s"]],
                    ["d_ne_f", "3.1", "2.2", ["to_w"]],
                    ["d_ne_b", "3.0", "2.2", ["to_w"]],
                    ["d_se_f", "3.1", "2.3", ["to_n"]],
                    ["d_se_b", "3.0", "2.3", ["to_n"]],
                    ["sw_f", "2.0", "2.5", ["to_e"]],
                    ["sw_b", "2.1", "2.5", ["to_e"]],
                    ["nw_f", "2.0", "2.6", ["to_s"]],
                    ["nw_b", "2.1", "2.6", ["to_s"]],
                    ["ne_f", "2.1", "2.7", ["to_w"]],
                    ["ne_b", "2.0", "2.7", ["to_w"]],
                    ["se_f", "2.1", "2.8", ["to_n"]],
                    ["se_b", "2.0", "2.8", ["to_n"]],
                    ["new_f", "1.3", "4.0", ["to_e"]],
                    ["new_b", "1.0", "4.0", ["to_e"]],
                    ["nse_f", "1.0", "4.1", ["to_s"]],
                    ["nse_b", "1.3", "4.1", ["to_s"]],
                    ["sew_f", "1.0", "4.2", ["to_w"]],
                    ["sew_b", "1.3", "4.2", ["to_w"]],
                    ["nsw_f", "1.3", "4.3", ["to_n"]],
                    ["nsw_b", "1.0", "4.3", ["to_n"]],
                    ["nsew_f", "1.1", "4.4", ["to_n"]],
                    ["nsew_b", "1.0", "4.4", ["to_n"]],
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
        return False


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
        if self.d["way_type"] == "RO":
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
            [name("image"), "sw", path(), 2, 5, -64, -96],
            [name("image"), "nw", path(), 2, 6, -64, -96],
            [name("image"), "ne", path(), 2, 7, -64, -96],
            [name("image"), "se", path(), 2, 8, -64, -96],
            [name("image"), "new", path(), 4, 0, -64, -96],
            [name("image"), "nse", path(), 4, 1, -64, -96],
            [name("image"), "sew", path(), 4, 2, -64, -96],
            [name("image"), "nsw", path(), 4, 3, -64, -96],
            [name("image"), "nsew", path(), 4, 4, -64, -96],
        ]
