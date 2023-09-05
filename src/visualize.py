import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Page

def draw_distribution(data,table_name):
     value_counts = {}
     for value in data:
          if value in value_counts:
               value_counts[value] += 1
          else:
               value_counts[value] = 1
     value_counts = dict(sorted(value_counts.items()))
     # 提取数据值和频次作为x轴和y轴的值
     x = list(value_counts.keys())
     y = list(value_counts.values())
     c = (
     Bar()
     .add_xaxis(x)
     .add_yaxis("频数", y, 
                    category_gap=0, # 设置柱子之间的间距为0
                    color='#ff8080')
     .set_global_opts(title_opts=opts.TitleOpts(title=table_name))
     )
     return c

