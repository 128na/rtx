import itertools
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
    env = Environment(loader=FileSystemLoader("./"), autoescape=select_autoescape())

    with open("./workspace/projects.yml", "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    for prj in data["projects"]:
        template = env.get_template(prj["source"])
        resolvedItems = {
            "items": resolve_class(prj["items"]),
        }
        rendered = template.render(prj.get("meta", {}) | resolvedItems)
        with open(prj["dest"], "w", encoding="utf-8") as file:
            file.write(rendered)
