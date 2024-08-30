class RTG:
    d: dict

    def __init__(self, data) -> None:
        self.d = data

    def get_name(self):
        return self.d["source"]

    def get_icon_source_path(self):
        return f"road/{self.d["source"]}"

    def get_icon_dest_path(self):
        return f"{self.get_name()}_icon"

    def get_icon_rules(self):
        return [
            ["_f", "2.1", "0.0", ["to_n"], "2.1", "2.0", ["to_n"]],
            ["_c", "2.1", "0.2", ["to_n"], "2.1", "2.2", ["to_n"]],
            ["_b", "2.1", "0.4", ["to_n"], "2.1", "2.4", ["to_n"]],
            ["_s", "2.1", "0.6", ["to_n"], "2.1", "2.6", ["to_n"]],
        ]

    def get_icon_before_apply(self):
        return []

    def get_icon_after_apply(self):
        return [
            "merge,../workspace/static/base_icon_4.png",
            "removeTransparent",
            "removeSpecial",
        ]

    def get_before_apply(self):
        return []

    def get_after_apply(self):
        return [
            "merge,../workspace/static/base_road.png",
            "removeTransparent",
            "removeSpecial",
        ]

    def get_source_path(self):
        return f"road/{self.d["source"]}"

    def get_dest_path(self):
        return self.get_name()

    def get_width(self):
        return 512 * 5

    def get_height(self):
        return 512 * 3

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
    def get_name(self):
        return f"road_{self.d["source"]}"


class RTGSurface(RTG):
    def get_name(self):
        return f"surface_{self.d["color"]}{self.d["source"]}{self.d["layout"]}"

    def get_icon_source_path(self):
        return f"surface/{self.d["source"]}{self.d["layout"]}"

    def get_icon_dest_path(self):
        return f"{self.get_name()}_icon"

    def get_icon_rules(self):
        return [["", "2.1", "0.0", ["to_n"], "2.1", "2.0", ["to_n"]]]

    def get_icon_before_apply(self):
        return [
            "merge,../workspace/static/base_icon_single.png",
        ]

    def get_icon_after_apply(self):
        return [
            f"shift,{self.get_shift()}",
            "merge,../workspace/static/base_icon_single_wrap.png",
            "removeSpecial",
        ]

    def get_after_apply(self):
        return [
            f"shift,{self.get_shift()}",
            "merge,../workspace/static/base_road.png",
            "removeSpecial",
        ]

    def get_shift(self):
        match self.d["color"]:
            case 1:
                return 209  # 青
            case 2:
                return 145  # 緑
            case 3:
                return 41  # 黄
            case _:
                return 0

    def get_source_path(self):
        return f"surface/{self.d["source"]}{self.d["layout"]}"

    def get_dest_path(self):
        return self.get_name()


class RTGSidewalkFill(RTG):
    def get_name(self):
        return f"side_{self.d["source"]}"

    def get_icon_source_path(self):
        return f"side/{self.d["source"]}"

    def get_icon_dest_path(self):
        return f"{self.get_name()}A_icon"

    def get_icon_rules(self):
        return [["", "1.4", "0.0", ["to_n"], "1.4", "2.0", ["to_n"]]]

    def get_icon_before_apply(self):
        return [
            "merge,../workspace/static/base_icon_single.png",
        ]

    def get_icon_after_apply(self):
        return [
            "merge,../workspace/static/base_icon_single_wrap.png",
            "removeTransparent",
            "removeSpecial",
        ]

    def get_source_path(self):
        return f"side/{self.d["source"]}"

    def get_dest_path(self):
        return f"{self.get_name()}A"

    def get_rules(self):
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


class RTGSidewalk(RTGSidewalkFill):
    def get_name(self):
        return f"side_{self.d["source"]}{self.d["layout"]}"

    def get_icon_source_path(self):
        return f"side/{self.d["source"]}"

    def get_icon_dest_path(self):
        return f"{self.get_name()}_icon"

    def get_icon_rules(self):
        return [
            ["_f", "1.4", "0.0", ["to_n"], "1.4", "2.0", ["to_n"]],
            ["_c", "1.4", "0.2", ["to_n"], "1.4", "2.2", ["to_n"]],
            ["_b", "1.4", "0.4", ["to_n"], "1.4", "2.4", ["to_n"]],
            ["_s", "1.4", "0.6", ["to_n"], "1.4", "2.6", ["to_n"]],
        ]

    def get_icon_after_apply(self):
        return [
            "merge,../workspace/static/base_icon_4.png",
            "removeTransparent",
            "removeSpecial",
        ]

    def get_source_path(self):
        return f"side/{self.d["source"]}"

    def get_dest_path(self):
        return self.get_name()

    def get_rules(self):
        match self.d["layout"]:
            case "F":
                return [
                    ["ns_f", "1.3", "0.2", ["to_n"]],
                    ["ew_f", "1.3", "0.3", ["to_e"]],
                    ["s", "0.3", "0.5", ["to_n"]],
                    ["w", "0.3", "0.6", ["to_e"]],
                    ["n", "0.2", "0.7", ["to_s"]],
                    ["e", "0.2", "0.8", ["to_w"]],
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
                    ["w", "0.2", "0.6", ["to_e"]],
                    ["n", "0.3", "0.7", ["to_s"]],
                    ["e", "0.3", "0.8", ["to_w"]],
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

class RTGETC(RTG):
    def get_rules(self):
        return [
            [0, 0, 'to_s', 'to_w'],
            [1, 1, 'to_s', 'to_w'],
            [1, 2, 'to_n', 'to_e'],
            [2, 3, 'to_s', 'to_w'],
            [2, 4, 'to_n', 'to_e'],
            [3, 5, 'to_s', 'to_w'],
            [3, 6, 'to_n', 'to_e'],

        ]


class Dat:
    series: str
    d: dict

    def __init__(self, data) -> None:
        self.d = data

    def get_obj(self):
        return "way"

    def get_full_name(self):
        return (
            f"{self.series} {self.d["speed"]} {self.d["system_type"]}{self.d["layout"]}"
        )

    def get_waytype(self):
        return "road"

    def is_way_obj(self):
        return False

    def get_system_type(self):
        match self.d["system_type"]:
            case "G":
                return 0
            case "E":
                return 1

    def get_topspeed(self):
        return self.d["speed"]

    def get_cost(self):
        return self.d["speed"] * 50 * (1 if self.d["system_type"] == "G" else 5)

    def get_maintenance(self):
        return self.d["speed"] * (1 if self.d["system_type"] == "G" else 5)

    def get_intro_year(self):
        return 1900

    def get_intro_month(self):
        return 1

    def get_retire_year(self):
        return 2999

    def get_retire_month(self):
        return 1

    def get_image_path(self):
        return f"road_{self.d["speed"]}"

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

    def get_icon(self):
        return f"{self.get_image_path()}_icon.0.{self.get_icon_index()},-48,-70"

    def get_cursor(self):
        return f"{self.get_image_path()}_icon.1.{self.get_icon_index()},0,-12"

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

    def get_images(self):
        p = self.get_image_path()
        return [
            f"image[ns]={p}.0.2,-64,-96",
            f"image[ew]={p}.0.3,-64,-96",
            f"image[s]={p}.0.5,-64,-96",
            f"image[w]={p}.0.6,-64,-96",
            f"image[n]={p}.0.7,-64,-96",
            f"image[e]={p}.0.8,-64,-96",
            f"image[-]={p}.0.9,-64,-96",
            f"imageup[12]={p}.1.0,-64,-88",
            f"imageup[9]={p}.1.1,-64,-88",
            f"imageup[3]={p}.1.2,-64,-88",
            f"imageup[6]={p}.1.3,-64,-88",
            f"imageup2[12]={p}.1.5,-64,-80",
            f"imageup2[9]={p}.1.6,-64,-80",
            f"imageup2[3]={p}.1.7,-64,-80",
            f"imageup2[6]={p}.1.8,-64,-80",
            f"diagonal[sw]={p}.{self.get_sw_nw_y()}.0,-64,-96",
            f"diagonal[nw]={p}.{self.get_sw_nw_y()}.1,-64,-96",
            f"diagonal[ne]={p}.{self.get_ne_se_y()}.2,-64,-96",
            f"diagonal[se]={p}.{self.get_ne_se_y()}.3,-64,-96",
            f"image[sw]={p}.{self.get_sw_nw_y()}.0,-64,-96",
            f"image[nw]={p}.{self.get_sw_nw_y()}.1,-64,-96",
            f"image[ne]={p}.{self.get_ne_se_y()}.2,-64,-96",
            f"image[se]={p}.{self.get_ne_se_y()}.3,-64,-96",
            f"image[new]={p}.4.0,-64,-96",
            f"image[nse]={p}.4.1,-64,-96",
            f"image[sew]={p}.4.2,-64,-96",
            f"image[nsw]={p}.4.3,-64,-96",
            f"image[nsew]={p}.4.4,-64,-96",
        ]


class DatRTX(Dat):
    series = "RTX"


class DatGTX(Dat):
    series = "GTX"

    def get_images(self):
        """
        直角カーブは曲線
        """
        p = self.get_image_path()
        images = super().get_images()
        images[19:23] = [
            f"image[sw]={p}.{self.get_sw_nw_y()}.5,-64,-96",
            f"image[nw]={p}.{self.get_sw_nw_y()}.6,-64,-96",
            f"image[ne]={p}.{self.get_ne_se_y()}.7,-64,-96",
            f"image[se]={p}.{self.get_ne_se_y()}.8,-64,-96",
        ]
        return images


class DatTi(Dat):
    series = "Ti"

    def get_obj(self):
        if self.is_way_obj():
            return "way-object"
        return "way"

    def get_full_name(self):
        return f"{self.series} {self.d["speed"]} {self.d["color"]}{self.d["source"]}D{self.d["way_type"]}"

    def get_waytype(self):
        if self.d["way_type"] == "Ro":
            return "road"
        return "tram_track"

    def is_way_obj(self):
        return self.d["way_type"] != "T"

    def get_system_type(self):
        return 0

    def get_topspeed(self):
        return self.d["speed"]

    def get_cost(self):
        return 5000

    def get_maintenance(self):
        return 100

    def get_image_path(self):
        return f"surface_{self.d["color"]}{self.d["source"]}D"

    def get_icon_index(self):
        return 0

    def get_image_prefix(self):
        if self.is_way_obj():
            return "back"
        return ""

    def get_images(self):
        p = self.get_image_prefix()
        path = self.get_image_path()
        return [
            f"{p}image[ns]={path}.0.2,-64,-96",
            f"{p}image[ew]={path}.0.3,-64,-96",
            f"{p}image[s]={path}.0.5,-64,-96",
            f"{p}image[w]={path}.0.6,-64,-96",
            f"{p}image[n]={path}.0.7,-64,-96",
            f"{p}image[e]={path}.0.8,-64,-96",
            f"{p}image[-]={path}.0.9,-64,-96",
            f"{p}imageup[12]={path}.1.0,-64,-88",
            f"{p}imageup[9]={path}.1.1,-64,-88",
            f"{p}imageup[3]={path}.1.2,-64,-88",
            f"{p}imageup[6]={path}.1.3,-64,-88",
            f"{p}imageup2[12]={path}.1.5,-64,-80",
            f"{p}imageup2[9]={path}.1.6,-64,-80",
            f"{p}imageup2[3]={path}.1.7,-64,-80",
            f"{p}imageup2[6]={path}.1.8,-64,-80",
            f"{p}diagonal[sw]={path}.2.0,-64,-96",
            f"{p}diagonal[nw]={path}.2.1,-64,-96",
            f"{p}diagonal[ne]={path}.2.2,-64,-96",
            f"{p}diagonal[se]={path}.2.3,-64,-96",
            f"{p}image[sw]={path}.2.{self.get_curve_x(0)},-64,-96",
            f"{p}image[nw]={path}.2.{self.get_curve_x(1)},-64,-96",
            f"{p}image[ne]={path}.2.{self.get_curve_x(2)},-64,-96",
            f"{p}image[se]={path}.2.{self.get_curve_x(3)},-64,-96",
            f"{p}image[new]={path}.4.0,-64,-96",
            f"{p}image[nse]={path}.4.1,-64,-96",
            f"{p}image[sew]={path}.4.2,-64,-96",
            f"{p}image[nsw]={path}.4.3,-64,-96",
            f"{p}image[nsew]={path}.4.4,-64,-96",
        ]

    def get_curve_x(self, x: int):
        """
        低速道路の直角カーブは曲線
        """
        return x if self.d["speed"] == 6000 else x + 5


class DatTiSingle(DatTi):
    def get_full_name(self):
        return f"{self.series} {self.d["speed"]} {self.d["color"]}{self.d["source"]}{self.d["layout"]}{self.d["way_type"]}"

    def get_image_path(self):
        return f"surface_{self.d["color"]}{self.d["source"]}{self.d["layout"]}"

    def flip(self):
        """
        方角によっては左右が反転する
        """
        if self.d["layout"] == "B":
            return f"surface_{self.d["color"]}{self.d["source"]}F"
        return f"surface_{self.d["color"]}{self.d["source"]}B"

    def get_images(self):
        p = self.get_image_prefix()
        path = self.get_image_path()
        flip = self.flip()
        return [
            f"{p}image[ns]={flip}.0.2,-64,-96",
            f"{p}image[ew]={flip}.0.3,-64,-96",
            f"{p}image[s]={flip}.0.5,-64,-96",
            f"{p}image[w]={flip}.0.6,-64,-96",
            f"{p}image[n]={path}.0.7,-64,-96",
            f"{p}image[e]={path}.0.8,-64,-96",
            f"{p}image[-]={flip}.0.9,-64,-96",
            f"{p}imageup[12]={path}.1.0,-64,-88",
            f"{p}imageup[9]={path}.1.1,-64,-88",
            f"{p}imageup[3]={flip}.1.2,-64,-88",
            f"{p}imageup[6]={flip}.1.3,-64,-88",
            f"{p}imageup2[12]={path}.1.5,-64,-80",
            f"{p}imageup2[9]={path}.1.6,-64,-80",
            f"{p}imageup2[3]={flip}.1.7,-64,-80",
            f"{p}imageup2[6]={flip}.1.8,-64,-80",
            f"{p}diagonal[sw]={flip}.2.0,-64,-96",
            f"{p}diagonal[nw]={flip}.2.1,-64,-96",
            f"{p}diagonal[ne]={path}.2.2,-64,-96",
            f"{p}diagonal[se]={path}.2.3,-64,-96",
            f"{p}image[sw]={flip}.2.{self.get_curve_x(0)},-64,-96",
            f"{p}image[nw]={flip}.2.{self.get_curve_x(1)},-64,-96",
            f"{p}image[ne]={path}.2.{self.get_curve_x(2)},-64,-96",
            f"{p}image[se]={path}.2.{self.get_curve_x(3)},-64,-96",
            f"{p}image[new]={flip}.4.0,-64,-96",
            f"{p}image[nse]={path}.4.1,-64,-96",
            f"{p}image[sew]={path}.4.2,-64,-96",
            f"{p}image[nsw]={flip}.4.3,-64,-96",
            f"{p}image[nsew]={flip}.4.4,-64,-96",
        ]


class DatFX(DatTi):
    series = "FX"

    def is_way_obj(self):
        return self.d["layout"] != "A"

    def get_waytype(self):
        if self.is_way_obj():
            return "road"
        return "water"

    def get_full_name(self):
        return f"{self.series} {self.d["source"]}{self.d["layout"]}"

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
        return f"side_{self.d["source"]}{self.d["layout"]}"

    def get_images(self):
        p = self.get_image_prefix()
        path = self.get_image_path()
        return [
            f"{p}image[ns]={path}.0.2,-64,-96",
            f"{p}image[ew]={path}.0.3,-64,-96",
            f"{p}image[s]={path}.0.5,-64,-96",
            f"{p}image[w]={path}.0.6,-64,-96",
            f"{p}image[n]={path}.0.7,-64,-96",
            f"{p}image[e]={path}.0.8,-64,-96",
            f"{p}image[-]={path}.0.9,-64,-96",
            f"{p}imageup[12]={path}.1.0,-64,-88",
            f"{p}imageup[9]={path}.1.1,-64,-88",
            f"{p}imageup[3]={path}.1.2,-64,-88",
            f"{p}imageup[6]={path}.1.3,-64,-88",
            f"{p}imageup2[12]={path}.1.5,-64,-80",
            f"{p}imageup2[9]={path}.1.6,-64,-80",
            f"{p}imageup2[3]={path}.1.7,-64,-80",
            f"{p}imageup2[6]={path}.1.8,-64,-80",
            f"{p}diagonal[sw]={path}.2.0,-64,-96",
            f"{p}diagonal[nw]={path}.2.1,-64,-96",
            f"{p}diagonal[ne]={path}.2.2,-64,-96",
            f"{p}diagonal[se]={path}.2.3,-64,-96",
            f"{p}image[sw]={path}.2.5,-64,-96",
            f"{p}image[nw]={path}.2.6,-64,-96",
            f"{p}image[ne]={path}.2.7,-64,-96",
            f"{p}image[se]={path}.2.8,-64,-96",
            f"{p}image[new]={path}.4.0,-64,-96",
            f"{p}image[nse]={path}.4.1,-64,-96",
            f"{p}image[sew]={path}.4.2,-64,-96",
            f"{p}image[nsw]={path}.4.3,-64,-96",
            f"{p}image[nsew]={path}.4.4,-64,-96",
        ]
    

class DatETC(Dat):
    series: str = "ETC"
    d: dict

    def __init__(self, data) -> None:
        self.d = data

    def get_name(self):
        return "etc"

    def get_obj(self):
        if self.is_way_obj():
            return "way-object"
        return "way"

    def get_full_name(self):
        return f"{self.series} {self.d["layout"]}{self.d["way_type"]}"

    def get_waytype(self):
        if self.d["way_type"] == "Ro":
            return "road"
        return "tram_track"

    def is_way_obj(self):
        return self.d["way_type"] != "T"


    def get_system_type(self):
        return 0

    def get_topspeed(self):
        return 4000

    def get_cost(self):
        return 5000

    def get_maintenance(self):
        return 100

    def get_image_path(self):
        return "etc"

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

    def get_icon(self):
        return f"{self.get_image_path()}.0.{self.d['layout']},-48,-70"

    def get_cursor(self):
        return f"{self.get_image_path()}.1.{self.d['layout']},0,-12"

    def get_image_prefix(self):
        if self.is_way_obj():
            return "back"
        return ""
    def get_images(self):
        p = self.get_image_prefix()
        path = self.get_image_path()
        l = self.d['layout']
        return [
            f"{p}image[ns]={path}.2.{l},-64,-96",
            f"{p}image[ew]={path}.3.{l},-64,-96",
            f"{p}image[s]={path}.2.{l},-64,-96",
            f"{p}image[w]={path}.3.{l},-64,-96",
            f"{p}image[n]={path}.2.{l},-64,-96",
            f"{p}image[e]={path}.3.{l},-64,-96",
            f"{p}image[-]={path}.0.7,-64,-96",
            f"{p}imageup[12]={path}.0.7,-64,-96",
            f"{p}imageup[9]={path}.0.7,-64,-96",
            f"{p}imageup[3]={path}.0.7,-64,-96",
            f"{p}imageup[6]={path}.0.7,-64,-96",
            f"{p}imageup2[12]={path}.0.7,-64,-96",
            f"{p}imageup2[9]={path}.0.7,-64,-96",
            f"{p}imageup2[3]={path}.0.7,-64,-96",
            f"{p}imageup2[6]={path}.0.7,-64,-96",
            f"{p}diagonal[sw]={path}.0.7,-64,-96",
            f"{p}diagonal[nw]={path}.0.7,-64,-96",
            f"{p}diagonal[ne]={path}.0.7,-64,-96",
            f"{p}diagonal[se]={path}.0.7,-64,-96",
            f"{p}image[sw]={path}.0.7,-64,-96",
            f"{p}image[nw]={path}.0.7,-64,-96",
            f"{p}image[ne]={path}.0.7,-64,-96",
            f"{p}image[se]={path}.0.7,-64,-96",
            f"{p}image[new]={path}.0.7,-64,-96",
            f"{p}image[nse]={path}.0.7,-64,-96",
            f"{p}image[sew]={path}.0.7,-64,-96",
            f"{p}image[nsw]={path}.0.7,-64,-96",
            f"{p}image[nsew]={path}.0.7,-64,-96",
        ]
