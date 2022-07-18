---
layout: single
title:  "비트 연산을 이용한 문제 풀이"
categories : CodingTest
tag : cpp
toc : true
---

# 비트 연산을 이용한 문제 풀이

### 문제

### ![Codingtest](../../images/2022-07-18-codingtestcpp1/Codingtest-16581418927351.png)

### 코드

---

```c++
#include <iostream>
using namespace std;

int main() {   
    unsigned int a[9];
    a[0] = 0b000100;
    a[1] = 0b001000;
    a[2] = 0b001100;
    a[3] = 0b010000;
    a[4] = 0b010100;
    a[5] = 0b011000;
    a[6] = 0b011100;
    a[7] = 0b100000;
    a[8] = 0b100100;
	
    int A, B,two=0,one=0;
    cin >> A >> B;
    A = A - 1;
    B = B - 1;

    for (int i= 1; i<= 6;i++){
        int bit1 = a[A] & (1<<i); // i 번째의 비트를 찾아냄
        int bit2 = a[B] & (1<<i);
        if (bit1 == bit2 && bit1 != 0) two += 1;
        if (bit1 || bit2) one += 1;
    }
    cout << two << endl;
    cout << one;

    return 0;
}
```

---

### 문제 풀이

우선, 해당 문제를 볼 때 배열보다 비트로 접근 하는 방법을 취했다.

1. 배열에 각 층의 값을 2진수로 저장한다.
2. 입력된 층의 값들을 비트 단위로 변수에 저장하고 비교한다.

---

### 문제에서 배울점

비트 연산 관련 문제를 소홀히 해왔는데 처음으로 제대로 공부했던 것 같고 단순 보면 배열로 생각하기 쉽지만 비트로 풀면 쉽게 풀리는 문제도 있다는 점을 깨달았다.