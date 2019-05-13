## JS/Vue 과목평가 가이드

> 뷰 10문제 JS 15문제

- 뚱이짤 : === vs ==
- 이벤트 리스너 1문제 마크다운에 상세설명한 이유가 있다(객관식)
- 주관식은 좀 어려울 수 있음(디렉티브 같은 게 좀 나오겠죠 여러개! 빈칸에 디렉티브 채우기)
- 주관식 하나는 차근차근 보면 풀 수 있다 (?)
- 어메이징한 자바스크립트의 세계 (시험에는 안 나올듯)
  - type of NaN // "number"
  - NaN === NaN // false
  - 1 + '1' // "11"
  - 1 * '1' // 1
- type 다 찍어보기 (주노쌤 마크다운**)
  - typeof undefined // "undefined"
  - typeof null // "object"
- axios - promise 객체 반환
  - 파이썬이랑 완전히 다르게 동작 (block, nonblock)
- arrow function vs function - this
- 자바스크립트 - 싱글쓰레드임에도 멀티쓰레드처럼 보이는 이유는 non-blocking 때문
- var 안나옴
- Array helper method 무조건 보세요
  - `for of` 콜백은 아니지만(함수를 넘기지 않음) 알아둬라(?)
  - forEach , filter, map , (reduce) 보세요
  - find는 안봐도 됨
- computed / watch : watch는 데이터 변화를 그냥 지켜보는 거, 변하면 특정 함수를 실행
- computed / method : computed 는 캐싱(계산값을 저장해서 변수처럼 사용), method 는 매번 계산
- (주노쌤마크다운 - 인터폴레이션에서 사용 가능한 것들) : 자바스크립트 표현식
- appendChild는 노드만 인자로 받을 수 있습니다. (스트링은 appendChild 하지 못함)
- (JSON은 문자열! JS object처럼 표현되었을 뿐 object가 아니다)
- (arrow function case by case / return문 한 줄일 때, 인자가 없을 때, 인자가 하나일 때)
- 호이스팅 안나옴
- 이벤트 리스너에서 function / arrow function 에서 각각 this 를 찍으면 완전히 다른 걸 가리킴 **코드 상에 this 없는 경우에는 상관없다 / 낚시 문제로 나올 예정 (전국공통자료 function.pdf 보세요)
- 메서드 안에서의 콜백함수에서는 무조건 arrow function - 함수 안의 함수에서 `this` 는 window를 가리키기 때문