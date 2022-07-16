---
layout: single
title:  "다형성과 가상함수"
categories : study
tag : cpp
toc : true
---

 # 다형성과 가상함수

## 다형성 

다형성(polymorphism) 이란 하나의 기호를 여러 가지 의미로 사용하는 기술이다.

C++에서 다형성은 다음과 같이 분류된다.

![polymorphism](https://www.learnfk.com/storage/learnfk/learnfk_cpp-polymorphism-cpp-polymorphism.png)



각기 다른 동물들에게 speak라는 명령을 내리면 각각 다른 울음 소리를 낼 것이다. 똑같은 메시지를 보내지만 객체의 타입이 다르면 서로 다른 결과를 얻는 것이 다형성이다.

![](https://codegym.cc/images/article/1771301a-66f1-469c-868a-41809dc18672/original.png)

---

### 상향 형변환(Up-Casting)

다형성은 객체 포인터를 통해 이루어진다. 설명을 위해 몇 가지 클래스가 정의되어 있는데 Animal 클래스에서 상속을 받아서 Dog과 Cow와 Cat 클래스를 정의한다.

![](data:image/jpeg;base64,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V7x1N/g+nKRyOKotGtCaDD+NBAHSbc00hz1BJ3nMfFvyhoAVEngSejvc+oaOfXFjquoJzOnndrJi7nF9jT1gX5yVWIiiig+5/s0w0kZzVUT+215V4oHQo27pOkrP6qJ32wvP91YRfLCWJr4y1zQ5pFiCAWkcxB3rNFFQ+J9zSlNSaigllwufz4HERHmDo72y9TcoWp36xzDdlbRNxSEfz6YWqQOd8dtp9AAHOv0NFbpZPaOaa4fX2bT1TdZtvE/iVAtv4rt9udtwqFTukehOH193T0zRJvErOJUAjccw8a39Vwp7vNjmGi9HWNxWEfyKnZVADkZJfafSQB5qeB+hoojC+6XSOqdRXRS4XPysqGlsR62yWAy9bg2/IrWORrow5rg4EXBBBaRzghSyskREBERAREQEREBERAREQEREBERAREQERYTTNZE573tY0C7nOIDQOck7kGa+E2BJNufmULiPdIjfVGmwullxSblMeylb1ukPJ1jinzgtcaG4hiJz4zXlsZ28DpiWweiR38Xo225HK2S7fxrukUkVVwajZJidQb5YqcZmA7uM8AgC+8jNblC5/eDGcT24jWd7oD/xqY/LEc0km36RxgeYK0wbBKWjpdVS08cDeXK3jOPO473HrJK6CX4HG0d0WosPgy0tMyLZYvteZ3rOO0+jcuyiKKIiICIiAoHRgZe6zpAPOjonfZA34q+UHhAy92LEx59FA/7CxqsJK8REUUREQEREGnimFU9VTaqogjnZzPYHAHnF9x6woqTuezUchkwbEpaLbc08hMlG483GuW35XEOPoX6Citx+et09q6FwZjOGPhbu4VADJSHrcNpZ6LknmVng+NUtZT6ylqY528uVwLh1OG9p6iAt5zQWkEAg7COQqNxjubUMtTr6bWYdONrZaZxZtvfa0bLHltYnnTwizRfnnD8fw394p2YzAP5kIyVoHO5gHGPUAety7mjmnmH1z8kc+qlvYwzDVzh3K2x2OI/pJSxdToiKKIiICIiAiIgIvCucRRSkGxDHEHlvlKneFydK/tuWqvFihuwsGcSPCpRS3C5Olf23JwuTpX9tyw1EcNukq5VK166tigpnSzSshY3xnPeGsH0lT3C5Olf23LmY3hcNa2IVTNeI352Bz3WBLSDuO0WO7duTUU8JpKuYedR3Q5Kqd0OC0Elc4HK6d4MdEw85LrF1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)



객체 포인터도 타입이 맞는 객체만을 가리킬 수 있는데 다음 코드를 보고 생각해보자

```c++
Animal *pa = new Cow();			// 가능한가?
```

위의 문장은 가능한데, 이유는 자식 객체는 부모 객체를 포함하고 있기 때문에 자식 객체는 부모 객체이기도 하기 때문이다. 이러한 포인터 타입의 변환을 __상향 형변환(Up-Casting) __이라고 한다.

하지만, 상향 형변환을 하면 자식 클래스 중에 부모 클래스로부터 상속받은 부분만을 포인터를 통해 사용할 수 있고 나머지는 사용하지 못한다.

다음 아래코드를 보고 생각해보자.

```c++
class Animal{
public:
    void speak() { cout << "Animal speak()"<<endl;}
};

class Dog : public Animal{
public:
    int age;
    void speak(){cout <<"멍멍"<<endl;}
};

int main(){
    Animal *a = new Dog();
    a->speak();
    
    //a->age = 10; //오류!!
    return 0;
}
```

___실행 결과___

```
Animal speak()
```

상향 형변환시 자식 클래스의 멤버 변수는 사용하지 못하고 심지어 상속 오버라이딩 또한 되지 않았다.

그 이유는, C++ 컴파일러가 실제로 가리키는 객체의 자료형을 기준으로 하는게 아닌, 포인터 변수의 자료형을 기준으로 판단하기 때문이다. 즉, 실제로 가리키는 객체인 Dog의 자료형이 아닌 포인터 변수 자료형인 Animal을 기준으로 판단하는 것이다.



그렇다면,  실제로 가리키는 객체에 따라 멤버 함수가 호출되도록 하려면 어떻게 해야할까? 이 문제는 곧 배울 virtual키워드를 함수 앞에 명시해주면 해결 가능하다. 이렇게 virtual 키워드가 붙은 함수를 __가상함수__라고 한다.

---

## 가상 함수

함수 앞에 virtual 키워드를 붙여주어 부모 포인터를 통하여 객체의 멤버 함수를 호출 하도록 하는 방법이다.

아래 코드를 보자

```c++
class Animal{
public:
    virtual void speak() { cout << "Animal speak()"<<endl;}
};

class Dog : public Animal{
public:
    int age;
    void speak(){cout <<"멍멍"<<endl;}
};

int main(){
    Animal *a = new Dog();
    a->speak();
    
    return 0;
}
```

___실행 결과___

```c++
멍멍
```

virtual 키워드는 멤버 함수에만 사용할 수 있는데 멤버 변수에는 사용할 수 없다. 그리고, 부모 클래스에서 virtual로 정의하면 자식 클래스에서는 virtual 키워드를 사용하지 않아도 자동으로 가상 함수가 된다.

---

### 동적 바인딩 VS 정적 바인딩

함수 호출을 함수의 몸체와 연결하는 것을 바인딩(binding)이라고 한다. 바인딩에는 정적 바인딩과 동적 바인딩이 존재하는데 아래 표를 참고 하자.

| 바인딩의 종류 |                 특징                 |  속도  |   대상    |
| :-----------: | :----------------------------------: | :----: | :-------: |
|  정적 바인딩  | 컴파일 시간에 호출 함수가 결정 된다. | 빠르다 | 일반 함수 |
|  동적 바인딩  |  실행 시간에 호출 함수가 결정 된다.  |  늦다  | 가상 함수 |

C++에서 가상 함수가 아니면 모든 함수가 정적 바인딩으로 호출된다.

---

### 참조자와 가상함수

포인터 뿐만 아니라 참조자인 경우에도 다형성이 동작한다.

```C++
class Animal{
public:
    virtual void speak() { cout << "Animal speak()"<<endl;}
};

class Dog : public Animal{
public:
    int age;
    void speak(){cout <<"멍멍"<<endl;}
};

int main(){
    Animal *a = new Dog();
    
    Dog d;
    Animal &a1 = d;
    
    a->speak();
    a1.speak();
    return 0;
}
```

___실행 결과___

```
멍멍
멍멍
```

---

### 가상 소멸자

다형성을 사용하는 과정에서 소멸자를 virtual로 해주지 않으면 부모 클래스 소멸자만 호출되는 문제가 발생한다.

아래의 코드를 살펴보자.

```c++
class Animal {
public:
    ~Animal(){cout << "Animal 소멸자"<< endl;}
};

class Dog : public Animal {
public:
    ~Dog(){cout << "Dog 소멸자"<< endl;}
};

int main(){
    Animal* a = new Dog(); // 상향 형변환
    delete a;
}
```

___실행 결과___

```
Animal 소멸자
```



이와 같은 현상을 해결하기위한 방법은 간단하다. 부모클래스 소멸자에 virtual 키워드만 붙여주면 된다.

```c++
class Animal {
public:
    virtual ~Animal(){cout << "Animal 소멸자"<< endl;}
};

class Dog : public Animal {
public:
    ~Dog(){cout << "Dog 소멸자"<< endl;}
};

int main(){
    Animal* a = new Dog(); // 상향 형변환
    delete a;
}
```

___실행 결과___

```
Dog 소멸자
Animal 소멸자
```

---

### 순수 가상 함수

순수 가상 함수(pure virtual function)는 함수 헤더만 존재하고 함수의 몸체는 없는 함수이다. 다음과 같은 형식을 사용한다.

```c++
virtual 반환형 함수이름(매게변수리스트) = 0;
```

순수 가상 함수를 하나라도 가지고 있는 클래스를 __추상 클래스(abstract class)__라고 하는데 이는 다음 글에서 자세히 다뤄보겠다.