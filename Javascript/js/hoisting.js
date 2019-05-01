// // let 블록스코프 예제
// {
//     let x = 'lucio'
//     console.log(x) // 루시우
//     {
//         let x = 'bastion'
//         console.log(x) // 바스티온 
//     }
//     console.log(x) // 루시우
// }
// // console.log(x) // reference error (선언된 적 없음)
// console.log(typeof x) // undefined

// // 전역변수의 오염
// {
//     var x = 'lucio'
//     console.log(x) // 루시우
//     {
//         var x = 'bastion'
//         console.log(x) // 바스티온 
//     }
//     console.log(x) // 바스티온
// }


// let foo
// let bar = undefined

// foo // undefined
// bar // undefined
// baz // ReferenceError: baz is not defined


// y 
// var y = 1
// y 
// // JS가 이해한 코드
// var y 
// y       // undefined
// y = 1   // 1
// y       // 1

if (x !== 1) {
    console.log(y)
    var y = 3
    if (y === 3) {
        var x = 1
    }
    console.log(y)
}
if (x === 1) {
    console.log(y)
}

// var 로 변수를 선언하면 JS는 같은 변수를 여러번 정의하더라도 무시한다
var x = 1
if (x === 1) {
    var x = 2
    console.log(x)  // 2
}
console.log(x)      // 2

// function hoisting
// ssafy 함수가 선언되기 전에 ssafy() 로 호출된 형태
// ssafy()
// function ssafy() {
//     console.log('hoisting!!')
// }

ssafy()
let ssafy = function () {
    console.log('hoisting!!')
}