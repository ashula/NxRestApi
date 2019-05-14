#
#   draw_graph(y_list, graph_name)
#       y_list : [y1,y2,y3,...,yn]
#       graph_name : graph file name with .png
#
#   x axis is automatically allocated from the order of y axis values
#      with assumption of linear behavior.
#
#     Ver-0.10, 20190514, initial implementation. (c) tm
#
#
#
import sys
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

#plt.savefig("hoge1.png")


def draw_graph(y_list, graph_name):
    x_list = []
    
    for i in range(len(y_list)):
        x_list.append(i)

    plt.plot(x_list, y_list)

    plt.savefig(graph_name)

    plt.show()

if __name__=='__main__':

    x = [100, 200, 300, 400, 500, 600]
    y1 = [10, 20, 30, 50, 80, 130]
#  y2 = [110, 120, 80, 50, 10, 20]

#  plt.plot(x, y1)
#  plt.plot(x, y2)

#  plt.savefig("hoge1.png")

#  plt.show()

    draw_graph(y1,"test_graph001.png")

