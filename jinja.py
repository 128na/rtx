"""
workspace内のj2ファイルをレンダリングする。標準出力に出るのでいい感じにファイル出力してください。
"""

import argparse
from jinja2 import Environment, FileSystemLoader, select_autoescape

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

    data = {
        "project": "RTX",
        "defs": [
            {
                "mode": "road",
                "types": [2080, 3080, 4080],
                "system_types": ["G", "E"],
                "layouts": ["F", "C", "B", "S"],
            },
            {
                "mode": "texture",
                "types": [1, 2, 3, 4, 5, 6],
                "system_types": ["G"],
                "layouts": ["Ti"],
            },
        ],
        "meta": {
            "types": {
                2080: {"cost": 400000, "maintenance": 8000},
                3080: {"cost": 800000, "maintenance": 16000},
                4080: {"cost": 1600000, "maintenance": 32000},
            },
            "system_types": {
                "G": {"id": 0, "cost": 1},
                "E": {"id": 1, "cost": 5},
            },
        },
    }
    print(template.render(data))
