"""
workspace内のj2ファイルをレンダリングする。標準出力に出るのでいい感じにファイル出力してください。
"""

import itertools
import argparse
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

import j2class


def resolve_class(defs: list):
    resolved = []
    for d in defs:
        pattern = d.get("pattern")
        keys = pattern.keys()
        combinations = itertools.product(*pattern.values())
        matrix = [dict(zip(keys, combo)) for combo in combinations]
        for m in matrix:
            resolved.append(getattr(j2class, d.get("className"))(m))
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
