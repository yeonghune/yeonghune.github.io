---

layout: single
title:  "합성곱 신경망"
categories : MachineLearning
tag : [Python, MachineLearning]
toc : true

---

## 컨볼루션 레이어 ( Convolution Layer)

### 정의 및 사용 이유

* __컨볼루션 레이어__ : 이미지를 필터를 통해 사이즈를 조정해 Activation Map을 생성

* __사용 이유__ : ___fully connected layer___ 로 영상을 처리할때 Parameter 가 너무 많아져서 Parameter를 줄이면서 양질의 결과가 나오는 ___Convolution layer___ 를 사용한다

  ![Convolution Layer](https://www.researchgate.net/profile/Hiromu-Yakura/publication/323792694/figure/fig1/AS:615019968475136@1523643595196/Outline-of-the-convolutional-layer.png)

---

### Conv2D 레이어

해당 레이어는 주로 영상 처리에 사용되며, 필터가 탑재되어 있다.

아래는 Conv2D 클래스 사용 예제이다.

```python
Conv2D(32,(5,5),padding='valid', input_shape(28,28,1),activation ='relu')
```

* __첫 번째 인자__ : 컨볼루션 필터의 수
* __두 번째 인자__ : 컨볼루션 커널의 행, 열
* __padding__ : 경계처리 방법 (valid 유효한 영역만 출력, same 출력 과 입력 사이즈가 동일)
* __input_shape__ : 샘플 수를 제외한 입력 형태를 정의, 첫 레이어 일때만 정의 ( 흑백 1, RGB 3 )
* __activation__ : 활성화 함수 (relu, sigmoid, softmax)

---

## Max Pooling, Average Pooling

* __정의__ : weight 없이 이미지 사이즈를 줄이는 과정
* __사용 이유__ : Convolution 으로 대체는 가능한데 Parameter가 필요없는 레이어들도 많기에 불필요한 Parameter를 지우기 위해 사용한다.

![](https://www.researchgate.net/publication/333593451/figure/fig2/AS:765890261966848@1559613876098/Illustration-of-Max-Pooling-and-Average-Pooling-Figure-2-above-shows-an-example-of-max.png)

---

## Convolutional Neural Networks

![](https://production-media.paperswithcode.com/method_collections/cnn.jpeg)





