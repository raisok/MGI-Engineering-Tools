import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def get_category(file):
    cate_list=[]
    with open(file,'r') as f:
        if not f.readline().startswith("#Flowcell"):
            return cate_list
        for line in f:
            if line.startswith("#"):
                continue
            else:
                if line.startswith("fovname") or line.startswith("ImageNumber") or line.startswith("Read1Length") or line.startswith("Read2Length") or line.startswith("BarcodeLength") or line.startswith("BarcodePosition"):
                    continue
                try:
                    arr = line.split(",")
                    cate_list.append(arr[0])
                except Exception:
                    cate_list= []
                    return cate_list
    return cate_list

def getqc_draw_data(file,category):
    chip_file_name = os.path.basename(file)
    sequence_flag = None
    with open(file,'r') as f:
        for line in f:
            if line.startswith("#"):
                if line.startswith("#Flowcell"):
                    sequence_flag = line.strip().split(",")[1]
                elif line.startswith("#Cycle"):
                    sequence_flag = sequence_flag+"\nCycleNumber: "+line.strip().split(",")[1]
                elif line.startswith("#DateTime"):
                    sequence_flag = sequence_flag + "\nDateTime: " + line.strip().split(",")[1]
                else:
                    continue
            else:
                arr = line.split(",")
                if arr[0] == category:
                    q30 = [float(i) for i in arr[1:]]
                    max_value = max(q30)
                    min_value = min(q30)
                    lower_q = np.quantile(q30, 0.50, interpolation='lower')
                    to_arr = np.array(q30).reshape(40,40)
                    pyecharts_heatmap(to_arr,chip_file_name,category,max_value,min_value,lower_q,sequence_flag)
                    # draw_heatmap(to_arr,chip_file_name,category,max_value,min_value,lower_q,sequence_flag)


def draw_heatmap(arr,chip_name,type,max_value,min_value,lower_q,sequence_flag):
    #使用seaborn进行画图
    f, ax = plt.subplots(figsize=(12, 12))
    # ax.set_title(chip_name+"\n"+type, fontsize=10, fontweight="bold") #设置标题
    ax.set_ylabel(type, fontsize=4)

    # f.suptitle("My Title")  #设置子标题
    ax.text(x=0.5, y=1.05, s=sequence_flag, fontsize=10, alpha=0.75, ha='center', fontweight="bold",
            va='bottom', transform=ax.transAxes)
    ax.text(x=0.5, y=1.01, s=type, fontsize=10, alpha=0.75, ha='center',fontweight="bold",
            va='bottom', transform=ax.transAxes)

    #ax = sns.heatmap(arr, fmt="d", cmap='RdYlGn_r', ax=ax)
    #sns.color_palette("Blues")
    cmap1 = sns.diverging_palette(20, 133, sep=100,as_cmap=True)
    # cmap2 = sns.color_palette("Greens")
    if type == "CycQ30":
        ax = sns.heatmap(arr, cmap=cmap1,fmt=".3f",annot=True,linewidths=0.5, ax=ax,vmax=0.8,vmin=0.4,annot_kws={'size':4,'weight':'normal', 'color':'#253D24'},) #数字越大，颜色越绿
    else:
        ax = sns.heatmap(arr, cmap=cmap1,annot=False,linewidths=0.5, ax=ax,vmax=max_value,vmin=lower_q,annot_kws={'size':4,'weight':'normal', 'color':'#253D24'},)
    #ax = sns.heatmap(arr, cmap='RdYlGn', linewidths=0.5, ax=ax, annot=True)  # 数字越大，颜色越绿,加数值
    #ax = sns.heatmap(arr, cmap='RdYlGn_r', linewidths=0.5, ax=ax,vmin=0, vmax=1)  # 数字越大，颜色越红 同时设置颜色范围
    # plt.savefig("test3.pdf") #保存图片
    plt.show()
    plt.close()

def draw_heatmap_v2(arr):
    #使用matplotlib进行画图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ax.imshow(arr, cmap=plt.get_cmap('hot'))
    plt.colorbar(im, shrink=0.5, ticks=[-1, 0, 1])
    plt.show()

from pyecharts import options as opts
from pyecharts.charts import HeatMap


def pyecharts_heatmap(to_arr,chip_file_name,category,max_value,min_value,lower_q,sequence_flag):

    values = [[i, j, round(to_arr[i][j],3)] for i in range(40) for j in range(40)]
    print(values)
    c = (
        HeatMap(init_opts=opts.InitOpts(width="1200px",height="800px"))
            .add_xaxis([i for i in range(1,41)])
            .add_yaxis(
            category,
            [i for i in range(1,41)],
            values,
            label_opts=opts.LabelOpts(is_show=False, position="inside"),

        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title=sequence_flag),

            visualmap_opts=opts.VisualMapOpts(is_show=True, min_=min_value, max_=max_value,
                                              item_height=30,item_width=15,
                                              ),
        )
            .render("heatmap_with_label_show.html")
    )
    import webbrowser
    webbrowser.open("file:///D:/GUI/MGI Engineering Tools/utils/heatmap_with_label_show.html")

if __name__ == '__main__':

    # file="D:/华大智造/Metric Tools/Metrics Sample/Metrics Sample/QCMetrics/E100003268L01C007QC.csv"
    file = "../123.csv"
    getqc_draw_data(file,"CycQ30")
