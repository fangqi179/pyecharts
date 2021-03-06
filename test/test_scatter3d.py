import random

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Scatter3D


def test_scatter3d_base():
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        for _ in range(80)
    ]
    c = (
        Scatter3D()
        .add("", data)
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color)
        )
    )
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
