## 데이터 요약 정보 및 통계값 샆펴보기
### 데이터를 불러왔다면 데이터에 포함된 대략 적인 데이터 분석을 할줄 알아야 한다.
## head() 와 tail() 을 통해서 해당 데이터의 맨위 그룹과 아래그룹을 볼수 있다.

import seaborn as sns
df=sns.load_dataset('titanic')
print(df.head())
print(df.shape)