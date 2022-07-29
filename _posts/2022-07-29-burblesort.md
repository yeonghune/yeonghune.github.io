---
layout: single
title:  "[알고리즘]버블 정렬(Burble Sort)"
categories : Algorithm
tag : [CPP, Algorithm]
toc : true
---

__버블 정렬(burble sort)__ 또는 거품 정렬 이라고 하며 양 옆의 인접한 원소를 검사하여 정렬하는 방법이다.

### __특징__

> 1.  소스 코드가 쉽고 단순하다.
> 2. 시간 복잡도 :  O(n^2)
> 3. 하나 하나 수작업으로 안정적이지만 속도가 느리다.

### 시각적 설명

![bubble-sort](../../images/2022-07-29-burblesort/bubble-sort.gif)

위에 그림과 같이 우측의 원소와 비교해 나가면서 정렬 하는 것이다.

### 소스 코드

```c++
void burblesort(int list[], int n){
   int temp;
   for(int i = n-1; i>0; i--){
      for(int j = 0 ; j < i ; j ++){
         if(list[j] > list[j+1]) 
            SWAP(list[j],list[j+1],temp);
      }
      printArray(list, n);
   }
}
```



