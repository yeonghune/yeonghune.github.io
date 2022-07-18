---
layout: single
title:  "cpp 학습(정적변수)"
categories : cpp
tag : cpp
toc : true
---

# 정적 변수,함수 와 싱글톤 디자인

### 정적 변수

```c++
class Point{
	int x;
	int y;
	static int count;	//선언 
	
public:
	Point(){cout << ++count; }
	~Point(){cout << --count;}
};

int Point::count = 0;	//정의

int main(){
	Point p1, p2, p3;
	return 0;
} 
```

정적 변수는 컴파일 과정에서 실행되고 **각 클래스 마다 하나만 생성된다.**

따라서 p1,p2,p3가 하나의 정적 변수를 공유하는데 count와 같이 생성된 객체의 수를 확인 하는데 사용할 수 있다.

정적 변수의 초기화는 전역 변수와 비슷하게 클래스 외부에서 수행한다.


![image-20220710181950015](..\..\images\2022-07-09-cpp(static)\image-20220710181950015.png)



### 정적 함수

```c++
class Circle{
	int x, y;
	int radius;
	
public:
	static int count; //정적 변수
	Circle() : x(0), y(0), radius(0){
		count++;
	}
	Circle(int x,int y, int r) :x(x),y(y),radius(r){
		count ++;
	}
	// 정적 멤버 함수
	static int getCount(){
		return count;
	} 
};

int Circle::count = 0;
```

다음 예제와 같이 정적 멤버 함수를 정의할 수 있다. 헌데 주의사항이 있다.

- 일반 멤버 변수들은 사용 할 수 없고 정적 변수와 지역 변수만을 사용 할 수 있다.
- 정적 멤버 함수에서 일반 멤버 함수를 호출하면 오류가 발생한다.
- 정적 함수에서 정적 함수를 호출하는 것은 가능하다.
- this 포인터를 사용 할 수 없다.(this가 가르키는 객체가 없기 때문)

정적 멤버 함수는 객체가 생성되지 않은 상태에서 호출되는 멤버 함수이므로 위와 같은 주의사항이 생겨난다.

------------

### 정적 상수

```c++
const static int MAX_CIRCLES = 300;
```

위와 같이 초기화 가능하고 각각 객체 안에 저장되지 않고 객체를 통틀어 하나만 존재하기 때문에 메모리 절약이 가능하며 많이 쓰인다.

---

### 싱글톤 패턴

##### 클래스로부터 오직 한 개의 객체만 생성되도록 하는 방법

```c++
class Car{
private:
	Car(){}
	static Car* instance;
public:
	static Car* getinstance();
};

Car* Car::getinstance()
{
	if(instance ==nullptr)
		return instance;
	else
	{
		instance = new Car();
		return instance;
	}
}

Car* Car::instance = nullptr;

int main(){
	Car* c = Car::getinstance();
    return 0;
} 
```

한 클래스에서 오직 한개의 객체만 생성하기 위해 고안된 디자인 패턴이다.

정적변수와 정적 함수에 대해 공부하기 좋은 예제다.



