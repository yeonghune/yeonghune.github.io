---
layout: single
title:  "로지스틱 회귀"
categories : study
tag : Python, MachineLearning
toc : true
---


# 타이타닉 속 생존 확률

남들 다 해본 타이타닉 속 생존 확률 찾기 나도 해본다!!

![titanic](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdLrUgB%2Fbtq4SbEnL9Q%2FzI9kWCpbEhLzH46pPMfz7k%2Fimg.jpg)

------

### 데이터 전처리


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('https://web.stanford.edu/class/archive/cs/
                      cs109/cs109.1166/stuff/titanic.csv')
```

#### 데이터 속에 null 값이 있는지 확인


```python
print(dataset.isna().sum())
```


    Survived                   0
    Pclass                     0
    Name                       0
    Sex                        0
    Age                        0
    Siblings/Spouses Aboard    0
    Parents/Children Aboard    0
    Fare                       0
    dtype: int64

### 타겟 설정 및 값 정리


```python
target = dataset['Survived']

dataset.drop(labels=['Name', 'Survived'], axis=1, inplace=True)
# axis 0 - 행방향 1 - 열방향
# inplace 변경 값을 저장할때 사용한다. 
#다시말 해 변수 초기화를 안해줘도 된다는 뜻

dataset['Sex'] = dataset['Sex'].map({'male':0,'female':1})

dataset
```

이름과 생존 을 drop 시켜주고 생존은 'target'으로 재지정한다.
성별은 남겨서 0, 1로 mapping 한다

-----

### train셋 test셋 나누기


```python
train_input, test_input, train_target, test_target =
train_test_split(dataset, target, random_state=42)

classifier = LogisticRegression()
classifier.fit(train_input,train_target)

```

### 가중치


```python
print(dataset.head(0))
print(classifier.coef_)
```

    Columns: [Pclass, Sex, Age, Siblings/Spouses Aboard, Parents/Children Aboard, Fare]
    array([[-1.10871884,  2.72399589, -0.04075159, -0.40154101, -0.09129951,
             0.00334793]])

분석결과 성별과 PClass가 사망에 큰 영향을 끼쳤다고 예상된다<br>
Pclass는 음수이지만, ~~높은 등급일수록 숫자가 낮으므로~~  음수더라도 절대 값을 취해서 고려할 필요가 있다.

-----------

### 나는 생존 할 수 있을까?


```python
pred = classifier.predict([[3, 0, 21.0, 1, 0, 8]]) 
#나에 해당하는 값 삽입

if(pred[0] == 0): # 0 사망 1 생존
    print('사망')
else:
    print('생존')
```

    사망

### 생존 확률

```python
pred = classifier.predict_proba([[3, 0, 21.0, 1, 0, 8]])
print(pred)
```

```
[[0.9067364 0.0932636]]
생존 확률 : 약 10%
사망 확률 : 약 90%
```

암울합니다...
