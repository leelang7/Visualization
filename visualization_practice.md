## 1. Matplotlib으로 기본 그래프 그리기

Matplotlib을 사용하면 다양한 그래프를 그릴 수 있습니다. 이번 실습에선 스켈레톤 코드의 주석 지시사항에 따라 그래프를 그려봅시다.

------

**그래프 출력 및 설정을 위한 함수/라이브러리**

- `fig, ax = plt.subplots()` : 초기 figure, 축 설정
- `ax.plot(x, y, label, marker, color, linestyle)`: 그래프 그리기
  - `x`: x 데이터 출력
  - `y`: y 데이터 출력
  - `marker`: 데이터 포인트 모양 설정
  - `color`: 데이터 포인트 색깔 설정
  - `linestyle`: 그래프의 선 스타일 설정
- `ax.set_title('name')` : 그래프 제목을 `'name'`으로 설정
- `ax.set_xlabel('name')` : x label의 이름을 `'name'`으로 설정
- `ax.set_ylabel('name')` : y label의 이름을 `'name'`으로 설정
- `ax.set_xlim(start, end)` : x축 범위를 start부터 end까지로 설정
- `ax.set_ylim(start, end)` : y축 범위를 start부터 end까지로 설정
- `ax.legend('loc', shadow, fancybox)` : 그래프 범례 설정
  - `'loc'`: 범례의 위치를 설정합니다.
  - `shadow`: 범례에 그림자 효과를 넣을지 말지를 True 또는 False로 설정합니다. True로 설정할 경우 그림자 효과가 나타납니다.
  - `fancybox`: 범례의 테두리를 둥글게 할지 말지를 True 또는 False로 설정합니다. True로 설정할 경우 범례의 테두리가 둥글게 나타납니다.
- `fig.savefig('name')` : figure를 `'name'`이라는 이름의 파일로 저장

## ***\*실습\**** 

1. 스켈레톤 코드에 있는 주석의 지시사항에 따라 그래프를 설정하고 그려보세요.



- ***\*이 실습은 제출이 없는 실습입니다. 자유롭게 값을 바꾸며 출력 결과를 확인해보세요.\****
- **주석의 지시사항에 따라 그려지는 그래프는 다음과 같습니다.**![image_output.png](https://cdn-api.elice.io/api-attachment/attachment/710dc479a44349b8a5d0263dac054ab4/image_output.png)



## 2. **Matplotlib으로 다양한 그래프 그리기**

Matplotlib을 통해 다양한 형태의 그래프도 그릴 수 있습니다. 이번 실습에선 Matplotlib을 사용해 Scatter, Bar, Multi-Bar, Histogram 그래프를 그려봅시다.

------

**다양한 그래프를 그리기 위한 함수/라이브러리**

`fig, axes = plt.subplots(a,b)` : a * b개의 그래프를 그릴 수 있는 초기 figure와 축 설정

### **Scatter**

- `axes[a,b].scatter(x, y, c, s, alpha)`
  : figure의 (a,b) 위치에 x, y 데이터의 scatter 그래프 그리기
  - `x` : x축 데이터
  - `y` : y축 데이터
  - `c` : 데이터 포인트의 색깔 설정
  - `s` : 데이터 포인트의 크기 설정
  - `alpha` : 데이터 포인트의 투명도 설정

### **Bar**

- `axes[a,b].bar(x,y)` : figure의 (a,b) 위치에 x, y 데이터를 bar 그래프로 출력

### **Multi-Bar**

- `axes[a,b].set_xticks(x_axis)` : figure의 (a,b) 위치에서 x축(`x_axis`) 데이터를 병렬적으로 설정 (여러개의 데이터를 한 막대그래프에 나타낼때 사용)
- `axes[a,b].set_xticklabels(['a', 'b'])` : x축 label을 ‘a’, ‘b’로 설정

### **Histogram**

- `axes[a,b].hist(data, bins)` : figure의 (a,b) 위치에 `data`를 Histogram 그래프로 그리기
  - `data` : 입력될 데이터
  - `bins` : Histogram 표현시 분할되는 개수 설정 (막대의 갯수)

## ***\*실습\**** 

1. 스켈레톤 코드에 있는 주석의 지시사항에 따라 그래프를 설정하고 그려보세요.



- ***\*이 실습은 제출이 없는 실습입니다. 자유롭게 값을 바꾸며 출력 결과를 확인해보세요.\****
- ***\*주석의 지시사항에 따라 그려지는 그래프는 다음과 같습니다.\****![image_output (1).png](https://cdn-api.elice.io/api-attachment/attachment/c951c087e5be4cc6a8f0a82787d69b34/image_output%20%281%29.png)



## 3. Seaborn regplot 그리기

Seaborn 라이브러리는 Matplotlib 라이브러리에서 제공하는 시각화 기법만큼 다양한 시각화 기법들을 제공합니다.

이번 실습에선 seaborn에서 제공하는 "tips" 데이터를 불러온 후, 총 가격에 해당되는 "total_bill" 데이터와 팁 가격에 해당되는 "tip" 데이터의 분포 및 선형 관계를 `regplot()` 함수를 사용하여 출력해 보겠습니다.

------

***\*데이터 시각화를 위한 Seaborn 함수/라이브러리\****

- `load_dataset('name')` : 데이터 이름이 `'name'`에 해당하는 데이터를 출력
- `regplot(x, y, color)` : 데이터 산점도를 출력 및 분포를 근사하는 선도 함께 출력
- - `x` : x축에 해당되는 데이터
  - `y` : y축에 해당되는 데이터
  - `color` : line의 색 설정 (문자열)

## ***\*실습\**** 

1. seaborn의 `load_dataset`을 사용하여 `tips` (팁 가격) 데이터 불러와 `df`에 저장합니다.
2. x축에 해당되는 데이터로 `df`의 `total_bill` 컬럼을 `x_data`에 저장합니다.
3. y축에 해당되는 데이터로 `df`의 `tip` 컬럼을 `y_data`에 저장합니다.
4. `regplot` 함수의 결과물을 `sns_plot` 으로 저장합니다.



- ***\*이 실습은 제출이 없는 실습입니다. 자유롭게 값을 바꾸며 출력 결과를 확인해보세요.\****
- ***\*주석의 지시사항에 따라 그려지는 그래프는 다음과 같습니다.\****![image_output (3).png](https://cdn-api.elice.io/api-attachment/attachment/2872c098fa77417bb1363cbd2c9deda7/image_output%20%283%29.png)



## 4. Seaborn countplot, jointplot 그리기

이번 실습에선 도수 분포를 나타내는 `countplot()` 함수, 그리고 산점도와 도수 분포를 모두 나타내는 `jointplot()` 함수를 사용하여 Seaborn에서의 `tips` 데이터를 시각화해 봅시다.

------

***\*countplot과 jointplot을 활용하기 위한 함수/라이브러리\****

- `countplot('x', data=df)`
  : 데이터 명에 해당하는 각 카테고리 값 별 빈도수를 표시하는 막대 그래프를 출력
- - `'x'`: 데이터 `df`에서 x 축의 데이터로 활용할 컬럼 이름 (문자열)
  - `data`: 시각화를 할 데이터(데이터프레임 형태)
- `jointplot('x', 'y', data=df, kind='scatter')`
  : 데이터 산점도와 히스토그램을 함께 출력
- - `'x` : 데이터 `df`에서 x축으로 할 컬럼 이름 (문자열)
  - `'y'` : 데이터 `df`에서 y축으로 할 컬럼 이름 (문자열)
  - `data` : 시각화를 할 데이터(데이터프레임 형태)
  - `kind` : 차트 종류 (문자열, 기본은 'scatter')

## ***\*실습\**** 

1. `countplot()` 함수의 출력물을 `sns_plot_size`으로 저장합니다. (x축을 "size" 컬럼으로 하여 "size"에 대한 countplot을 그림)
2. `jointplot()` 함수의 출력물을 `g`로 저장합니다. (x축은 "total_bill", y축은 "tip", 차트의 종류는 "resid"으로 하여 "total_bill"과 "tips"간의 산점도와 도수분포표를 나타내는 jointplot을 그림)



- ***\*이 실습은 제출이 없는 실습입니다. 자유롭게 값을 바꾸며 출력 결과를 확인해보세요.\****
- ***\*주석의 지시사항에 따라 그려지는 그래프는 다음과 같습니다.\****![image_output (5).png](https://cdn-api.elice.io/api-attachment/attachment/cec3bd82a55f4f90aef9cfe7c139961b/image_output%20%285%29.png)![image_output (4).png](https://cdn-api.elice.io/api-attachment/attachment/15fe20ff8d0b4f77a0a69247cc181161/image_output%20%284%29.png)