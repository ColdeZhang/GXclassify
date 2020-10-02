from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.globals import SymbolType

c1 = (
    Liquid()
    .add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-Diamond"))
    .render("liquid_shape_diamond")
)

c2 = (
    Liquid()
    .add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-Diamond"))
    .render("liquid_shape_diamond")
)

grid = Grid().add(c1, grid_opts=opts.GridOpts()).add(c2, grid_opts=opts.GridOpts())
grid.render("multiple_liquid.html")