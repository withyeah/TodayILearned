# HTML 정리

_과목평가 대비

20190222 금요일



### 1. Self-closing element

> 닫는 태그가 없는 태그도 존재한다 ex) <img>



### 2. 속성 (Attribute)

> 태그에는 속성이 지정될 수 있다
>
> id, class, style은 태그와 상관없이 모두 사용 가능하다



### 3. Semantic tag

> 컨텐츠의 의미를 설명하는 태그
>
> - header
> - nav
> - aside
> - section : 문서의 일반적인 구분으로 컨텐츠의 그룹을 표현하며, 일반적으로 h1~h6 요소를 가짐
> - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
> - footer
>
> *non semantic요소 : div, span 등
>
> > 개발자 및 사용자 뿐만 아니라 검색엔진 (구글, 네이버)등에 의미 있는 정보의 그룹을 태그로 표현하여 단순히 보여주기 위한 것을 넘어서 <u>의미를 가지는 태그들을 활용</u>하기 위한 노력



### 4. others

> `<video>` : autoplay
>
> `<table>` 
>
> ```html
> <table>
>     <tr>
>     	<th>Firstname</th>
>         <th>Lastname</th>
>     </tr>
>     <tr>
>     	<td>Jill</td>
>         <td>Smith</td>
>     </tr>
>     <tr>
>     	<td>Eve</td>
>         <td>Jackson</td>
>     </tr>
> </table>
> ```
>
> > - colspan='2' 가로로 두 칸 차지
> > - rowspan='2' 세로로 두 칸 차지
>
> `<input>` 
>
> > - input type : text, radio, submit...
> > - action
> > - target : `_self`(default) / `_blank` 
> > - method : get / post
> > - fieldset : group related data in a form
> > - form attribute
> >   - value='abc' : initial value
> >   - readonly
> >   - disabled
> >   - size : input field 자체의 사이즈
> >   - maxlength : input 내용의 최대 길이
> > - input attribute
> >   - autofocus
> >   - placeholder
> >   - required