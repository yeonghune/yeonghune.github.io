---
layout: single
title:  "덧셈 곱셈 연산없이 곱셉 수행"
categories : CodingTest
tag : [cpp]
toc : false
---

# 문제

덧셈 곱셈 연산없이 곱셉 수행 하여라

입력 예시 1 : 2 5	출력 : 10

입력 예시 2 : 3 2	출력 : 6

입력 예시 3 : 7 5	출력 : 35

## 알고리즘

아래 그림을 참고하자.

<img src="../../images/2022-07-26-Coding-test1/KakaoTalk_20220726_173747293.jpg" alt="KakaoTalk_20220726_173747293" style="zoom:33%;" />

7 x 5은 위 그림과 같이 비트에서도 수행 할 수 있다.

설명을 위해 7을 x로 5를 y로 치환하겠다.

1. y의 마지막 비트가 1일시 Sum 변수에 x를 합 함
2. 논립 연산자는 불가능한 캐리를 수행 해준다.

---

## 코드

```c++
#include <iostream>
using namespace std;

int Multiply(int x, int y);
int Add(int x, int y);

int main(){
	int x,y;
	cin >> x >> y;
	cout << Multiply(x,y)<< endl;
	
	return 0;
}

int Multiply(int x, int y){
	int sum = 0;
	while(y){
		if(y & 1)
			sum = Add(sum, x);
		x <<= 1;
		y >>= 1;
	}
	return sum;
}

int Add(int x, int y){
	while(y){
		int carry = x & y;
		x = x ^ y;
		y = carry << 1;
	}
	return x;
}
		
```

