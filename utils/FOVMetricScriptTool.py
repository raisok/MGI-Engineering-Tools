import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from matplotlib.colors import LightSource
from matplotlib import cm
import logging
logging.basicConfig(level=logging.INFO)

def getfov_draw_data(file):
    if os.path.exists(file):
        df = pd.read_csv(file,sep=",",header=0)
        logging.info("Read Fov File success")
        return df
    else:
        logging.info("Read Fov File failed")
        return False


def get_fov_category(file):
    with open(file,'r') as f:
        line = f.readline()
        logging.info(line)
        if not line.startswith("SlideID"):
            cate_list=[]
        else:
            cate_list = ["X Pos [um]","Y Pos [um]",
                             "Z Pos [um]","AF Signal",
                             "AF Sum","AF Diff"
                             ]
    return cate_list

def draw_terrain2d(file,category):
    logging.info("2d plot "+category + " is running")
    df = getfov_draw_data(file)

    Z = [float(i) for i in df[category][30:]]
    logging.info(Z)
    arr = np.array(Z).reshape(40, 40)
    #plt.imshow(arr, cmap='viridis')
    plt.imshow(arr, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.show()

def draw_terrain3d(file,category):
    logging.info("3d plot "+category + " is running")
    df = getfov_draw_data(file)

    X = [int(i) - 1 for i in df['Row'][30:]]
    Y = [int(i) - 1 for i in df['Row'][30:]]
    Z = [float(i) for i in df[category][30:]]
    xpos_arr = np.array(X).reshape(40, 40)
    ypos_arr = np.array(Y).reshape(40, 40)
    zpos_arr = np.array(Z).reshape(40, 40)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ls = LightSource(270, 45)
    rgb = ls.shade(zpos_arr, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
    # ax.plot_surface(xpos_arr , ypos_arr, zpos_arr, cmap='autumn',
    #                 rstride = 1, cstride = 1, facecolors = rgb,
    #                 linewidth = 0, antialiased = False, shade = False
    # )
    ax.plot_surface(xpos_arr , ypos_arr, zpos_arr,
                    rstride = 1, cstride = 1, facecolors = rgb,
                    linewidth = 0, antialiased = False, shade = False
    )
    ax.set_xlabel("X label")
    ax.set_ylabel("Y label")
    ax.set_zlabel("Z label")
    plt.show()

def draw_ypos(file,category):
    logging.info("3d plot " + category + " is running")
    df = getfov_draw_data(file)

def draw_xpos(file,category):
    pass

def draw_xpos_transposed(file,category):
    pass


if __name__ == '__main__':
    file="D:/华大智造/Metric Tools/Metrics Sample/Metrics Sample/FOVMetrics/E100003268.L1.S007.csv"
    # df = get_draw_data(file)
    draw_terrain3d(file,"Z Pos [um]")
