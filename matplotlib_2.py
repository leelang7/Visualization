import numpy as np
import matplotlib.pyplot as plt
import csv

def main():
    
    data_x = []
    data_y = []
    
    with open('./data/data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data_x.append(float(row[0]))
            data_y.append(float(row[1]))
    
    # 2x2개의 그래프를 그릴 수 있는 초기 figure와 축을 설정합니다.
    fig, axes = None
    
    """
    Scatter 그래프 그리기
    """
    
    colors = np.random.randint(0,100,500)
    
    # figure의 (0,0) 위치에 scatter 그래프를 그립니다.
    # x 데이터는 data_x, y 데이터는 data_y, 데이터 포인트의 색깔은 colors, 사이즈는 2, 투명도는 0.7로 설정합니다.
    None
    
    """
    Bar 그래프 그리기
    """
    
    bar_x = np.arange(10)
    
    # figure의 (0,1) 위치에 Bar 그래프를 그립니다.
    # x 데이터는 bar_x, y 데이터는 bar_x**2로 설정합니다.
    None
    
    """
    Multi-Bar 그래프 그리기
    """
    
    x = np.array([3,2,1])
    y = np.array([2,3,2])
    z = np.array([1,3,4])
    data1 =  [x, y, z]

    x_ax =  np.arange(3)
    
    for i in x_ax:
        # figure의 (1,0) 위치에 Bar 그래프를 그립니다.
        # x 데이터는 x_ax, y 데이터는 각각 x,y,z로 설정합니다.
        axes[None].bar(None, None, bottom=np.sum(data1[:i], axis=0))
        
    # figure의 (1,0) 위치에서 x축 데이터를 병렬적으로 설정합니다.
    None
    # figure의 (1,0) 위치에서 x축 label을 'A', 'B', 'C'로 설정합니다.
    None
    
    """
    Histogram 그래프 그리기
    """
    
    data = np.array(data_x)
    
    # figure의 (1,1) 위치에 Histogram 그래프를 그립니다.
    # 입력될 데이터는 data, Histogram 표현시 분할되는 개수는 50으로 설정합니다.
    None
    
    # figure를 저장합니다.
    fig.savefig("plot.png")

if __name__ == '__main__':
    main()
