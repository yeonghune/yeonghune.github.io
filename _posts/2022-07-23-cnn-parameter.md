---
layout: single
title:  "CNN모델 파라미터 계산"
categories : MachineLearning
tag : [Python, MachineLearning]
toc : true
---

### 예제 코드

Tensorflow 공식 사이트 예제 : https://www.tensorflow.org/tutorials/images/cnn?hl=ko

```PYTHON
model = models.Sequential()
#Convolution Layer
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
#Fully Connected Layer
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
```

### CNN 입출력, 파라미터 계산

| layer               | Input Channel | Filter | Output Channel | Stride | Max Pooling |
| :------------------ | :------------ | :----- | :------------- | :----- | :---------- |
| Convolution Layer 1 | 1             | (3, 3) | 32             | 1      | X           |
| Max Pooling Lyaer 1 | 32            | X      | 32             | 2      | (2, 2)      |
| Convolution Layer 2 | 32            | (3, 3) | 64             | 1      | X           |
| Max Pooling Lyaer 2 | 64            | X      | 64             | 2      | (2, 2)      |
| Convolution Layer 3 | 64            | (3, 3) | 64             | 1      | X           |

---

#### 1. Layer 1의 Shape와 파라미터

Convolution Layer 1개와 Max Pooling Layer 1개가 존재

__1.1 Convolution Layer 1__

* 입력 데이터 Shape : (28,28,1)
* 출력 데이터 Shape : (26,26,32)
* 입력 채널 : 1
* 필터 : (3,3)
* 출력 채널 : 32
* Stride : 1

__1.2 파라미터의 개수__

파라미터 = 커널 높이 X 커널 폭 X 입력 채널 X 출력 채널 + BIAS(필터개수)

Parameter = 3 X 3 X 1 X 32 + 32

__1.3 Max Pooling Layer 1__

* 입력 채널 : 32
* Max Pooling : (2,2)
* 출력 데이터 Shape : (13,13,32)

#### 2. Layer 2의 Shape와 파라미터

Convolution Layer 1개와 Max Pooling Layer 1개가 존재

__2.1 Convolution Layer 2__

* 입력 데이터 Shape : (13,13,32)
* 출력 데이터 Shape : (11,11,64)
* 입력 채널 : 32
* 필터 : (3,3)
* 출력 채널 : 64
* Stride : 1

__2.2 파라미터의 개수__

파라미터 = 커널 높이 X 커널 폭 X 입력 채널 X 출력 채널 + BIAS(필터개수)

Parameter = 3 X 3 X 32 X 64 + 64

__2.3 Max Pooling Layer 2__

* 입력 채널 : 64
* Max Pooling : (2,2)
* 출력 데이터 Shape : (5,5,64)

#### 3. Layer 3의 Shape와 파라미터

Convolution Layer 1개 존재

__3.1 Convolution Layer 3__

* 입력 데이터 Shape : (5,5,64)
* 출력 데이터 Shape : (3,3,64)
* 입력 채널 : 64
* 필터 : (3,3)
* 출력 채널 : 64
* Stride : 1

__3.2 파라미터의 개수__

파라미터 = 커널 높이 X 커널 폭 X 입력 채널 X 출력 채널 + BIAS(필터개수)

Parameter = 3 X 3 X 64 X 64 + 64

#### 4. Flatten Layer의 Shape

Flatten Layer는 CNN의 데이터 타입을 Fully Connected Neural Network의 형태로 변경하는 레이어다. 파라미터는 존재하지않고 Shape만 변경한다.

* 입력 데이터 Shape : (3,3,64)
* 출력 데이터 Shape : (576,1)
* 파라미터 : 0

#### 5. Dense Layer의 Shape

* 입력 데이터 Shape : (576,1)
* 출력 데이터 Shape : (64,1)
* 파라미터 : 36928 ( 576 X 64 + 64(bias))

#### 6. SoftMax Layer의 Shape

* 입력 데이터 Shape : (64,1)
* 출력 데이터 Shape : (10,1)
* 파라미터 : 650 (64 X 10 +10(bias))

---

### 학습에서 배운 것

1. CNN모델에서는 bias 가 붙는다
2. Dense Layer 에도 bias가 붙는다
3. Parameter 구하는 식

---

### 참고자료

* TAEWAN.KIM 블로그(http://taewan.kim/post/cnn/)
* wikipedia (https://ko.wikipedia.org/wiki/%ED%95%A9%EC%84%B1%EA%B3%B1)