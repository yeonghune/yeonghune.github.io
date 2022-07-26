---
layout: single
title:  "정수를 받아 비트로 변환 후 1인 개수 구하기"
categories : CodingTest
tag : [cpp]
toc : false
---

# 문제

입력한 수를 비트화 했을 때 각 자리의 수가 1인 개수를 구하라.

입력 예시 1 : 10	출력 : 2

입력 예시 2 : 12	출력 : 2

입력 예시 3 : 15	출력 : 4

## 알고리즘

아래 그림을 참고하자.

![알고리즘 설명](../../images/2022-07-26-Coding-test/알고리즘 설명-16588225857512.jpg)

10 진수 20은 비트로 환산 시 10100이다.

10 진수 19는 비트로 환산 시 10011이다.

이 두 수를 논리 곱을 취해주면 10000 인데 마지막 1인 비트가 소거된다.

논리 합 연산 시 Count 하는 변수를 1 씩 추가 해주는 알고리즘을 사용한다.

---

## 코드

```c++
#include <iostream>
using namespace std;

int BitsCount(unsigned int);

int main(){
	int n;
	cin >> n;
	
	cout << BitsCount(n);
	
	return 0;
}

int BitsCount(unsigned int x){
	int cnt = 0;
	while(x){
		x = x & (x-1);
		cnt += 1;
	}
	return cnt;
}
```



