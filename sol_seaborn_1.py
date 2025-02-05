# Seaborn 라이브러리 import 하기 
import seaborn as sns 
import matplotlib.pyplot as plt 

# seaborn의 load_dataset을 사용하여 tips (팁 가격) 데이터 불러오기
df = sns.load_dataset('tips') 

# 전체 데이터에서 처음 5개의 row 데이터 표시 (내용 확인)
# 데이터에 대한 정보를 알고 싶은 경우, 주석을 풀어 확인
# df.head() 
# x축에 해당되는 데이터로 total_bill series를 x_data으로 저장 

x_data = df["total_bill"]

# y축에 해당되는 데이터로 tip series를 y_data으로 저장 
y_data = df["tip"]

# regplot함수의 출력물을 sns_plot으로 저장
# line의 색은 red로 설정
sns_plot = sns.regplot(x=x_data, y=y_data, color='red')
fig = sns_plot.get_figure()
fig.savefig("plot3.png")