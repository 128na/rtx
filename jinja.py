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
                "types": [30, 50, 120],
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
                30: {"cost": 15000, "maintenance": 300},
                50: {"cost": 25000, "maintenance": 500},
                120: {"cost": 100000, "maintenance": 2000},
            },
            "system_types": {
                "G": {"id": 0, "cost": 1},
                "E": {"id": 1, "cost": 5},
            },
        },
    }
    print(template.render(data))
