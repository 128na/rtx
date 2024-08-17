from jinja2 import Environment, FileSystemLoader, select_autoescape
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="jinjaテンプレートをレンダリングする")
    parser.add_argument("file_name", help="ファイルのパス")
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader("workspace"), autoescape=select_autoescape()
    )

    def pad(value, width, char="_"):
        return str(value).zfill(width).replace("0", char, width - len(str(value)))

    env.filters["pad"] = pad

    template = env.get_template(args.file_name)

    data = {
        "project": "RTX",
        "defs": [
            {
                "mode": "road",
                "types": [80, 120, 160],
                "system_types": ["G", "E"],
                "layouts": ["F", "C", "B", "S"],
            },
            {
                "mode": "texture",
                "types": [1, 2, 3, 4, 5],
                "system_types": ["G"],
                "layouts": ["Ti"],
            },
        ],
        "meta": {
            "types": {
                80: {"cost": 40000, "maintenance": 800},
                120: {"cost": 60000, "maintenance": 1200},
                160: {"cost": 80000, "maintenance": 1600},
            },
            "system_types": {
                "G": {"id": 0, "cost": 1},
                "E": {"id": 1, "cost": 5},
            },
        },
    }
    print(template.render(data))
