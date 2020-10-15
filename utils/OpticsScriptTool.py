import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def laser_formula_cal(power_list,x_list):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_list,power_list,'o',linestyle='--',color='g')
    plt.show()

def laser_formula_cal_reg(power_list,x_list,y_list,formula_line):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    #绿色的虚线为拟合的线条
    ax.plot(power_list, y_list, linestyle='--', color='g')
    #蓝色的实际折线图为功率转换的电压百分数和实际设置的电压百分数折线
    ax.plot(power_list, x_list,linestyle='-',color='b')
    ax.set_title(formula_line)
    plt.show()


def stagt_flatness(file):
    data=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
    label = "Z Height Difference:  "
    max_min_list=[]
    max_min=None
    with open(file,'r') as f:
        header = f.readline()
        if not header.startswith("Position"):
            return False
        for line in f:
            if line.startswith("Top Left"):
                data[0][0] = float(line.strip().split(",")[3])
                max_min_list.append(float(line.strip().split(",")[3]))
            if line.startswith("Top Right"):
                data[0][2] = float(line.strip().split(",")[3])
                max_min_list.append(float(line.strip().split(",")[3]))
            if line.startswith("MaxZ-minZ"):
                max_min = float(line.strip().split(",")[3])

                label += " " +str(1000*max_min)+" (um)"
            if line.startswith("Bottom Left"):
                data[2][0] = float(line.strip().split(",")[3])
                max_min_list.append(float(line.strip().split(",")[3]))
            if line.startswith("Bottom Right"):
                data[2][2] = float(line.strip().split(",")[3])
                max_min_list.append(float(line.strip().split(",")[3]))
            if line.startswith("Center"):
                data[1][1] = float(line.strip().split(",")[3])
                max_min_list.append(float(line.strip().split(",")[3]))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(label)
    # create a mask array for stage
    ######seaborn method for draw a stage heatmap#######
    mask=[
        [0,1,0],
        [1,0,1],
        [0,1,0],
    ]
    myColors = ((0.0, 0.8, 0.0, 1.0), (0.0, 0.8, 0.0, 1.0), (0.0, 0.8, 0.0, 1.0))
    cmap = LinearSegmentedColormap.from_list('Custom', myColors, len(myColors))
    if max_min <= 0.01:
        ax = sns.heatmap(data, cmap=cmap, fmt=".5f", annot=True, linewidths=0.5, ax=ax, mask=mask,
                         annot_kws={'size': 12, 'weight': 'normal', 'color': 'blue'}, )
    else:
        ax = sns.heatmap(data, cmap='RdBu_r', fmt=".5f", annot=True, linewidths=0.5, ax=ax, mask=mask,
                     annot_kws={'size': 12, 'weight': 'normal', 'color': 'blue'}, )  # 数字越大，颜色越绿

    ######seaborn method for draw a stage heatmap#######

    ######matplotlib method for draw a stage heatmap#######
    # maxv=max(max_min_list)
    # minv=min(max_min_list)
    # im=ax.imshow(data, cmap='hot', interpolation='nearest',vmin=minv-0.0001,vmax=maxv+0.0001)
    # for i in range(len(data)):
    #     for j in range(len(data[i])):
    #         text = ax.text(j, i, data[i][j],
    #                        ha="center", va="center", color="b")
    # fig.colorbar(im,pad=0.03)
    ######matplotlib method for draw a stage heatmap#######

    plt.show()



def read_csv(filename):
    mydict = {}
    df = pd.read_csv(filename, header=0, sep=',',index_col=False)
    colnames = ['Row', 'Col', 'AFTarget',
                'Center1', 'Center2', 'Center3', 'Center4',
                'TopLeft1', 'TopLeft2', 'TopLeft3', 'TopLeft4',
                'TopRight1', 'TopRight2', 'TopRight3', 'TopRight4',
                'BottomLeft1', 'BottomLeft2', 'BottomLeft3', 'BottomLeft4',
                'BottomRight1', 'BottomRight2', 'BottomRight3', 'BottomRight4']

    df.columns = colnames
    idmin = df.groupby('Col').idxmin()
    # header = list(idmin.columns)
    for i, j in idmin.iterrows():
        M = []
        for m, n in j.items():
            M.append(str(df['AFTarget'][n]))
        mydict[str(i)] = [float(i) for i in M[2:]]
    return mydict


def get_best_AF_target(filename):
    mydict = read_csv(filename)
    A_Left, A_Mid, A_Right, C_Left, C_Mid, C_Right, \
    G_Left, G_Mid, G_Right, T_Left, T_Mid, T_Right = [[] for i in range(12)]

    for index, value in mydict.items():
        # print(index,value)
        A_Left.extend([value[4], value[12]])  # Topleft1, Bottomleft1
        A_Mid.extend([value[0]])  # Center1
        A_Right.extend([value[8], value[16]])  # Topright1,Bottomright1

        C_Left.extend([value[5], value[13]])  # Topleft2, Bottomleft2
        C_Mid.extend([value[1]])  # Center2
        C_Right.extend([value[9], value[17]])  # Topright2,Bottomright2

        G_Left.extend([value[6], value[14]])  # Topleft3, Bottomleft3
        G_Mid.extend([value[2]])  # Center3
        G_Right.extend([value[10], value[18]])  # Topright3,Bottomright3

        T_Left.extend([value[7], value[15]])  # Topleft4, Bottomleft4
        T_Mid.extend([value[3]])  # Center4
        T_Right.extend([value[11], value[19]])  # Topright4,Bottomright4

    A_Left_median = np.median(A_Left)
    A_Mid_median = np.median(A_Mid)
    A_Right_median = np.median(A_Right)
    A_diff = abs(A_Left_median - A_Right_median)
    A_best_target = np.median([A_Left_median, A_Mid_median, A_Right_median])

    C_Left_median = np.median(C_Left)
    C_Mid_median = np.median(C_Mid)
    C_Right_median = np.median(C_Right)
    C_diff = abs(C_Left_median - C_Right_median)
    C_best_target = np.median([C_Left_median, C_Mid_median, C_Right_median])

    G_Left_median = np.median(G_Left)
    G_Mid_median = np.median(G_Mid)
    G_Right_median = np.median(G_Right)
    G_diff = abs(G_Left_median - G_Right_median)
    G_best_target = np.median([G_Left_median, G_Mid_median, G_Right_median])

    T_Left_median = np.median(T_Left)
    T_Mid_median = np.median(T_Mid)
    T_Right_median = np.median(T_Right)
    T_diff = abs(T_Left_median - T_Right_median)
    T_best_target = np.median([T_Left_median, T_Mid_median, T_Right_median])

    single_channel_max_diff = np.max([A_diff, C_diff, G_diff, T_diff])

    Multi_channel_best_target = np.median([A_best_target, C_best_target, G_best_target, T_best_target])
    Max_Multi_channel_best_target = np.max([A_best_target, C_best_target, G_best_target, T_best_target])
    Min_Multi_channel_best_target = np.min([A_best_target, C_best_target, G_best_target, T_best_target])
    Multi_channel_max_diff = Max_Multi_channel_best_target - Min_Multi_channel_best_target

    Single_camera_fous_concordance = [['\t\tA', 'C', 'G', 'T'], \
                                      ['Left\t', A_Left_median, C_Left_median, G_Left_median, T_Left_median], \
                                      ['Middle\t', A_Mid_median, C_Mid_median, G_Mid_median, T_Mid_median], \
                                      ['Right\t', A_Right_median, C_Right_median, G_Right_median, T_Right_median], \
                                      ['|Left-Right|', A_diff, C_diff, G_diff, T_diff], \
                                      ['Standard\t','\t|Left-Right|<=1\t      ']]

    All_cameras_focus_concordance = [
        ['\t A ', ' C', ' G', ' T\t'], \
        ['\tBest Focus', A_best_target, C_best_target, G_best_target, T_best_target, 'diff(max-min)\t'], \
        ['\tStandard', '\t\tmax-min<=1\t', '        '+str(Multi_channel_max_diff)+"\t\t"], \
        ['\tBest Focus Signal', '\t\t'+str(Multi_channel_best_target)+"\t\t\t\t"]]

    Best_AF_Target = [Multi_channel_best_target - 2]

    return Single_camera_fous_concordance, All_cameras_focus_concordance, Best_AF_Target, single_channel_max_diff, Multi_channel_max_diff


if __name__ == '__main__':
    file="D:/GUI/MGI Engineering Tools/VerifyStageFlatness20200611_110502.csv"
    stagt_flatness(file)