# CSS_test_prep



1. CSS 사용 방법
   1. Inline : 여는 태그 내부에 style='어쩌구저쩌구'
   2. embedding(내부 참조) : head 내부에 style태그 넣음
   3. link file(외부 참조) : <link rel='stylesheet' href='#'>



2. size
   1. px : 디바이스 별로 픽셀의 크기는 제각각
   2. % : 백분율 단위의 상대 단위. 상속된 사이즈나 디폴트 사이즈에 상대적인 사이즈
   3. em : 배수 단위로 상대 단위. " em의 기준은 상속의 영향으로 바뀔 수 있음
   4. rem : r == root. 최상위 요소(html)의 사이즈를 기준으로 삼는다
   5. viewport 단위 : 디바이스마다 다른 크기의 화면을 가지고 있기 때문에 상대적인 단위인 viewport를 기준으로 만든 단위
      - vw : 너비의 1/100
      - vh : 높이의 1/100



3. 색상 표현 단위
   1. HEX : #ffffff
   2. RGB : rgb(0, 0, 0)
   3. RGBA : rgb(0, 0, 0, 0.5)



4. Box model

   > content > padding > border > margin



5. display

   1. block

      - 화면 크기 전체의 가로폭을 차지(width: 100%), block 레벨 요소 내에 inline 레벨 요소를 포함할 수 있음

      - div, h1~h6, p, ol, ul, li, hr, table, form

   2. inline

      - content의 너비만큼 가로폭을 차지

      - ##### <u>width, height, mt, mb 프로퍼티 지정불가, 상하여백은 line-height로 지정</u>

      - span, a, strong, img, br, input, select, textarea, button

   3. inline-block

      - inline 요소 처럼 한 줄에 표시되면서 block에서의 width, height, margin 속성을 모두 지정할 수 있음

   4. ##### none

      - ##### <u>해당 요소를 화면에 표시하지 않는다. (공간조차 사라짐!!!!!!)</u>



6. visibility property

   1. visible (default)

   2. ##### <u>hidden : 해당 요소를 안 보이게 한다 (공간은 존재함!!!!!!)</u>



7. position

   1. static (기본 위치)

      - 기본적인 요소의 배치 순서에 따라 위>아래, 왼>오
      - 부모 요소 내에 자식 요소로서 존재할 때는 부모의 위치를 기준으로 배치 

   2. ##### <u>relative (상대 위치)</u>

      - 기본 위치를 기준으로 좌표 프로퍼티(t, b, l, r)를 사용하여 위치를 이동

   3. ##### <u>absolute (절대 위치)</u>

      - 부모 요소 또는 가장 가까이 있는 조상 요소(static 제외)를 기준으로 좌표 프로퍼티만큼 이동
      - 즉, relative, absolute, fixed 프로퍼티가 선언되어 있는 부모 또는 조상 요소를 기준으로 위치가 결정됨

   4. fixed (고정 위치)

      - 부모 요소와 관계없이 브라우저의 viewport를 기준으로 좌표프로퍼티를 사용하여 위치를 이동
      - 스크롤하더라도 화면에서 사라지지 않고 항상 같은 곳에 위치함



8. selector 우선순위

   1. !important 붙인 속성
   2. html에서 스타일을 직접 지정한 속성
   3. `#id`로 지정한 속성
   4. .클래스 로 지정한 속성
   5. 태그이름으로 지정한 속성
   6. 상위 객체에 의해 상속된 속성

   > 같은 우선순위라면 나중에 선언된 속성이 우선시 됨