---
layout: single
title:  "[머신러닝]Resnet 모델 정리"
categories : MachineLearning
tag : [Python, MachineLearning]
toc : true
---

### 소개

ResNet 등장 이전 모델등은 __Layer 가 깊어질 수록 성능이 떨어지는__ 현상이 있었다. 이는 gradient vanishing 때문이다. 이를 해결하기 위해 ResNet은 Skip Connection을 이용한 residual learning 을 이용해 Layer 가 깊어지면 성능이 떨어지는 문제를 해결했다.

---

### Residual Block

![Residual Network](https://d2l.ai/_images/residual-block.svg)

좌) Plane Layer 우) Residual block

__기존방식(Plane Layer) __ 은 전 레이어의 Output인 y를 그대로 학습하는것이다.

__Residual Block__ 은 전 레이어의 Ouput을 남겨두고 학습시키고 전 레이어의 output을 더한다. 지름길을 통해 전레이어의 output을 출력에 더해주기만 하면 되어 파라미터가 따로 필요없어 덧셈연산만 추가된다 이를 ___identity mapping___이라고 한다.

---

### VGG 모델과의 비교

![](https://cdn-5f733ed3c1ac190fbc56ef88.closte.com/wp-content/uploads/2017/04/resnet.png)

---

### 사용법

```python
from keras.applications import ResNet50

tf.keras.applications.ResNet50(
    include_top=True, weights='imagenet', input_tensor=None, input_shape=None,
    pooling=None, classes=1000, **kwargs
)
```

