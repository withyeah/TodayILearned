# 효율성 테스트 통과, 시간복잡도

##### 20190208

> 프로그래머스 > 코딩테스트연습 > 해쉬 > 완주하지 못한 선수
>
> [문제 보러가기](https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3)
>
> - <u>문제 설명</u>
>   - 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
>
>  마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
>
> - <u>제한사항</u>
>   - 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
>   - completion의 길이는 participant의 길이보다 1 작습니다.
>   - 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
>   - 참가자 중에는 동명이인이 있을 수 있습니다.
>
> - <u>입출력 예</u>
>
> | Participant                             | Completion                       | return |
> | --------------------------------------- | -------------------------------- | ------ |
> | [leo, kiki, eden]                       | [eden, kiki]                     | leo    |
> | [marina, josipa, nikola, vinko, filipa] | [josipa, filipa, marina, nikola] | vinko  |
> | [mislav, stanko, mislav, ana]           | [stanko, ana, mislav]            | mislav |
>



## Problem

정확성 테스트는 전부 통과했는데 효율성 테스트는 시간초과로 전부 0점

- 원래 코드

```python
def solution(participant, completion):
    for person in completion:
        participant.remove(person)
    return ''.join(participant)
```

> remove() 의 시간복잡도는 O(n)인데 for문을 도니까 O(n*n)이 됨 > 시간초과



## Solution

remove() 를 사용하지 않고 for 문 한 번만 돌도록!

동명이인을 고려해야 한다.

두 리스트를 sort 해준 후 

completion의 길이 만큼 돌면서 

각 리스트의 index번째 요소를 비교한다.

만약 다르다면, participant에는 있지만 completion에는 없는 이름! > 리턴

completion 길이만큼 돌았는데 모두 같다면 participant의 마지막 이름을 리턴

(완주하지 못한 선수는 1명이라고 명시되어있기 때문)

- 수정 코드

```python
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
```



## TIL

메소드 별 시간복잡도를 고려해야 한다