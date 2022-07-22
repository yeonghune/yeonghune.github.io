---
layout: single
title:  "합성곱 신경망 모델 구현"
categories : MachineLearning
tag : [Python, MachineLearning]
toc : true
---

## 손글씨 원, 사각형, 삼각형 분류

### 라이브 러리들 

```
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
```

### 데이터 전처리


```python

np.random.seed(3)

train_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    '/content/drive/MyDrive/handwriting_shape/train',
    target_size=(24,24),
    batch_size = 3,
    class_mode='categorical'
)

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
    '/content/drive/MyDrive/handwriting_shape/test',
    target_size=(24,24),
    batch_size = 3,
    class_mode='categorical'
)
```

### 모델구성

```python
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation = 'relu', input_shape=(24,24,3)))
model.add(Conv2D(64,(3,3),activation = 'relu'))
#model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(3,activation='softmax'))
```

### 모델 컴파일


```python
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
```

### 모델 학습


```python
model.fit_generator(train_generator,steps_per_epoch=15,epochs=50,validation_data=test_generator,validation_steps=5)
```


    Epoch 49/50
    15/15 [==============================] - 1s 43ms/step - loss: 5.2955e-06 - accuracy: 1.0000 - val_loss: 0.2440 - val_accuracy: 0.9333
    Epoch 50/50
    15/15 [==============================] - 1s 36ms/step - loss: 4.9405e-06 - accuracy: 1.0000 - val_loss: 0.2473 - val_accuracy: 0.9333

### 모델 평가


```python
print("--Evaluate--")
score= model.evaluate_generator(test_generator, steps=5)
print(score)
```

    --Evaluate--
    [0.24732321500778198, 0.9333333373069763]

### 모델 예측


```python
print("--predict")
output = model.predict_generator(test_generator, steps=5)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
print(test_generator.class_indices)
for i in range( len(output)):
    print(np.argmax(output[i]))
```

    --predict
    {'circle': 0, 'rectangle': 1, 'triangle': 2}
    0
    0
    2
    0
    2
    2
    1
    1
    2
    1
    1
    0
    0
    2
    1

---

### 데이터들

![image-20220721151252149](../../images/CNN_model_test/image-20220721151252149.png)
