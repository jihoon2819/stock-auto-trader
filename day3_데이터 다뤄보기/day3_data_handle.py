## 데이터 요약 정보 및 통계값 샆펴보기
### 데이터를 불러왔다면 데이터에 포함된 대략 적인 데이터 분석을 할줄 알아야 한다.
## head() 와 tail() 을 통해서 해당 데이터의 맨위 그룹과 아래그룹을 볼수 있다.

import seaborn as sns
df=sns.load_dataset('titanic')
print(df.head())
print(df.shape)
##df.shape 열과 행의 개수를 알려준다.
df.info()
##df.info()는 데이터 프레임의 기본정보를 알수 있다
##df['속성명'].counts()는 고유값의 종류와 개수를 확인할수 있다.
##또한values_counts().sort_index를 활용해서 메서드의 인덱스를 구할수 있다
## values_count(normalize=True)를 쓰면 정규화된 값을 봋수 있다

## mean을 통해서 산술평균 값을 구할수 있ㄷ.
## min은 최소
## max는 최대값이다.


## 결측치 처리하기
## 결측치 조회
df.head().isnull
df.head().notnull
## is null 은 결측값이면 tur 아니면 false이다.
## notnull 은 결측값이면 false 아니면 true이다
df.dropna()
##dropna()는 데이터에 결츨치가 있으면 그행을 전부 삭제하는 것이다.
##dropna(subset=['결측치탐지할 속성'],axis=0,thresh=몇개 이상 있을시 삭제 할것인가 숫자가 들어간다)

##결측치 대체하기
##df['대체해야하는 값이 있는 속성'].fillna(대체되서 들어갈 값,inplace=True)

##인덱스 다루기
##df.set_index('인덱스로 삼고싶은 속성',inplace=True)
##reset_index()를 통해서 되 돌릴수 있다

##새로운 열 만들기 
##df['새로만들고 싶은 속성']=df['lpg']*df['km']

##데이터 프레임 합치기
##concat() axis를 통해서 행기준 혹은 열기준으로 합칠수있고 2개으ㅟ 경우가 해당해야 합쳐지는 join속성에 inner조인도 있다

## merge
## 기준이되는 열이나 인덱스를 기준으로 데이터 프레임을 합치는것을 말한다. sql의 조인과 유사하다.

## join
## mergeㅎ람수를 기반으로 반들어져 사용방법이 거의 비슷하다 하지만 두데이터 프레임의 행인덱스를 기준으로 데이터를 결합한다. 

## apply를 통해서 함수 적용 가능
#def mm_to_cm(num):
#    return num/10
#
#result=df['cm'].apply(mm_to_cm)
