from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader("workspace"), autoescape=select_autoescape())


def pad(value, width, char="_"):
    return str(value).zfill(width).replace("0", char, width - len(str(value)))


env.filters["pad"] = pad


template = env.get_template("dat.j2")

print(template.render({}))
