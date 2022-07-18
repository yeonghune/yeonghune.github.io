---
layout: single
title:  "추상클래스와 인터페이스"
categories : cpp
tag : cpp
toc : true
---

# 추상 클래스와 인터페이스

## 추상 클래스(abstract class)

추상 클래스는 다른 형식의 기반 클래스로만 사용할 수 있고 개체를 생성할 수 없는 클래스를 말한다. 이러한 추상 클래스는 객체 지향 프로그래밍에서 중요한 특징인 다형성을 가진 함수의 집합을 정의할 수 있게 해준다. 순수 가상 함수를 한 개 이상 정의한 추상클래스로 부터 파생된 클래스는 반드시 이 가상 함수를 재정의 해야 한다.



```c++
class Animal 
{
public:
	virtual void speak() = 0; //순수 가상 함수
};

class Dog : public Animal {
public:
	int age;
	void speak() { cout << "멍멍" << endl; } //반드시 재정의 할것
};

int main() {
	Animal* a = new Dog();
	a->speak();

	return 0;
}
```

위에 코드에서 Animal을 상속받는 Dog 클래스는 부모의 speak() 을 반드시 재정의 해야 한다.  

그리고 추상클래스 로는 객체 생성이 불가능 하다!!

---

### abstract 키워드

원래 추상 클래스는 기본 class 형식에서 순수 가상 함수를 포함한 것으로 기본 class 와 구분하는 법 이 딱히 없었지만 abstract 키워드가 생겨 보다 더 쉽게 구별할 수 있도록 가독성을 높여 주었다.

```c++
class Animal abstract 
{
public:
	virtual void speak() = 0; //순수 가상 함수
};

class Dog : public Animal {
public:
	int age;
	void speak() { cout << "멍멍" << endl; } //반드시 재정의 할것
};
```

abstract 키워드가 있고 없음에 차이는 없지만 구별 해 주는 좋은 방법이다! 하지만, 순수 가상 함수가 없으면 abstract 키워드를 붙여도 추상 클래스가 되는 것은 아니다.

---

## 인터페이스

모든 함수가 순수 가상 함수로 구성된 클래스이고 본인만의 멤버 변수를 갖지 않는 것이 인터페이스이다.

```c++
class IAnimal  {
public:
	virtual void speak() = 0; //순수 가상 함수
	virtual ~Animal() {} //가상 소멸자
};
```



### 인터페이스의 주의사항

* 인터페이스를 상속 받은 클래스는 반드시 인터페이스 안에 모든 함수를 오버라이딩 해야 한다. 
* 본인 만의 멤버변수나 구현된 멤버 함수를 갖지 않는다.
* 추상 클래스와 마찬가지로 본인의 객체를 갖지 못한다.
* 관습적으로 인터페이스 앞에는 대문자 I 를 붙여준다.

---

### 인터페이스의 다른 표현법(__interface)

```c++
__interface Animal  {
public:
	virtual void speak();
};

class Dog : public Animal {
public:
	int age;
	void speak() { cout << "멍멍" << endl; }
};
```

#### __interface의 주의사항

* 순수 가상 함수로 선언을 해주지 않아도 순수 가상 함수로 인식된다.
* class는 기본 접근자가 private인 반면에 interface는 public 이다.
* 생성자, 소멸자 또는 연사자를 포함할 수 없다.
* 정적 메소드를 포함 할 수 없다.
* interface 의 모든 가상 함수를 오버라이딩 하지 않는 다면 상속 받은 클래스가 추상 함수화 되어서 객체 생성이 불가능하다.

