---

layout: single
title:  "상속"
categories : study
tag : cpp
toc : true

---

# 상속

### 상속의 정의

상속(inheritance)란 이미 존재하는 클래스로부터 멤버들을 물려 받는 것이다.

이미 존재하는 클래스를 부모클래스라 하고 상속을 받는 클래스를 자식 클래스라 한다. ~~사실 자바 공부 할때도 했고 상속파트는 많이 했는데 이번 기회에 확실히 내 것으로 만들 것이다~~

```c++
class Car
{
    int speed;
};
class SportsCar : public Car
{
    bool turbo;
}
```

다음과 같이 상속을 선언 할 수 있다.

---

### 상속과 생성자/소멸자

자식 클래스의 객체 안에는 부모로부터 상속 받은 멤버들이 존재한다. 이는 자식 클래스 안에 부모 클래스가 있는 것이나 마찬가지여서 __자식 클래스 생성자를 호출 한다면 제일 먼저 부모 클래스의 생성자를 호출__할 것이다.

소멸자 일 경우 이와 역순으로 자식클래스의 소멸자 먼저 호출되고 부모 클래스의 소멸자가 호출된다.



![inheritance](../../images/2022-07-12-inheritance/inheritance.jpg)



---

### 멤버 함수 재정의(Overriding)

#### 다형성

오버라이딩에 들어가기 앞서 __다형성__이라는 개념의 확립이 중요하다.

언어를 습득 한 사람이라면 누구나 인사를 할 수 있을 것이다. 밑에 사진을 보자

![](https://www.phptutorial.net/wp-content/uploads/2021/03/PHP-Polymorphism-Abstract-Class.svg)

영국인, 독일인, 프랑스인은 다들 인사를 하고 있지만 저마다 다른 언어로 자기들 만의 방식으로 하고 있다. 이를 우린 __다형성__ 이라고 부른다.



#### 오버라이딩(Overriding)

```c++
class Person{
public:
    void greet(){
        cout << "인사를 합니다.";
    }
};
class English : public Person{
public:
    void greet(){
        cout << "Hello";
    }
}
```

위의 그림을 보면 자식 클래스가 greet()를 재정의 하는데 객체를 통하여 접근하면 재정의된 함수가 우선권이 있기 때문에 재정의된 greet()가 호출되어 아래와 같이 출력된다.

```
Hello
```



----

### 다중 상속

자바에서는 안되는 다중 상속이다. 말 그대로 두개 이상의 부모 클래스로부터 멤버를 상속받는 것을 의미한다. 다음과 같은 형식을 사용한다.

```c++
class Sub : public Sup1, public Sup2
{
    //정의
}
```

![multiple inheritance](https://www.ibmmainframer.com/static/python/images/multiple_inheritance.png)

#### 다중 상속의 문제점

A와 B라는 부모로부터 다중 상속 받는 C라는 클래스가 있다고 가정하자.

A와 B클래스에서 모두 print() 가 정의 되어 있을때 C는 누구의 print()를 상속 받을 것인가?

```c++
class A {
public:    
    A(){}
    void print(){}
};
class B{
public:
    B(){}
    void print(){}
};
class C : public A, public B{
};

int main(){
    C obj;
    obj.print(); // 어떤 부모의 print()를 참조하는가?
    return 0;
}
```

이를 해결하기 위해 print() 앞에 범위 지정자를 붙여야 한다.

```c++
obj.A::print();
obj.B::print();
```

결론적으로 다중 상속은 복잡하기때문에 사용의 주의를 가해야 한다.





