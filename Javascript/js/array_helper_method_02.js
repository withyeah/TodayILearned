// 4. reduce
/* 
    - map 은 배열의 각 요소를 변형한다면, reduce 는 배열 자체를 변형
    - 배열을 '값 하나'로 줄이는 동작(ex 배열의 합, 배열의 평균..)
    - reduce 콜백함수의 첫 번째 매개변수는 '누적값(전 단계의 결과)' 이다.
    - 두 번째 매개변수는 현재 배열요소, 현재 인덱스, 배열 자체 순으로 들어간다.
*/

// 4-1] 총합
const SSAFY = [3, 9, 2, 7,]
const sum = SSAFY.reduce((total, x) => total + x, 0) // (누적값, x) => 누적값 + x, 초기값
console.log(sum) // 21

// 4-2] 평균
const avg = SSAFY.reduce((total, x) => total + x/SSAFY.length, 0)
const avg2 = SSAFY.reduce((total, x) => total + x, 0) / SSAFY.length
console.log(avg, avg2) // 5.25 5.25

// 4-3] 초기값 생략
// 초기값이 생략되면 누적값은 배열의 첫 번째 요소가 초기값이 된다.
// 위와 같은 경우는 x에 두 번째 배열요소부터 들어감
const sum2 = SSAFY.reduce((total, x) => total + x)
console.log(sum2) // 4-1]이랑 동일한 값! 21



// 5. find
/*
    - 첫 번째로 찾은 요소 한 가지만 return 한다.
    - '조건에 맞는 인덱스가 아니라 요소 자체를 원할 때' 사용
    - 배열 검색 헬퍼들 : find, indexOf, lastIndexOf, findIndex, some, every
*/

const USERS = [
    { name: 'Thor' },
    { name: 'Steve Rogers' },
    { name: 'Tony Stark' },
]

const ironMan = USERS.find(function(user) {
    return user.name === 'Tony Stark'
})
console.log(ironMan) // { name: 'Tony Stark' }

// ES5
for (var i = 0; i < USERS.length; i++) {
    if (USERS[i].name === 'Tony Stark') {
        user = USERS[i]
        break // 안해주면 모든 토니 스타크 다 찾음
    }
}
console.log(user) // { name: 'Tony Stark' }

// 5-1] users 중에 admin 권한을 가진 요소를 찾아서 admin 에 저장하자.
const PEOPLE = [
    { id: 1, admin: false },
    { id: 2, admin: false },
    { id: 3, admin: true },
]
const admin = PEOPLE.find(person => person.admin)
console.log(admin) // { id: 3, admin: true }

// 5-2] accounts 중에서 잔액이 12 인 object 를 account 에 저장하자.
const ACCOUNTS = [
    { balance: -10 },
    { balance: 12 },
    { balance: 0 }
]
const account = ACCOUNTS.find(account => account.balance === 12)
console.log(account) // { balance: 12 }


// 6. some & every
/*
    - 기존처럼 대상 배열에서 특정 요소를 뽑거나, 배열을 리턴 하지 않고, 조건에 대해 boolean 값을 리턴
    - some : 조건에 맞는 요소를 찾으면 즉시 검색을 멈추고 true 리턴, 찾지 못하면 false 리턴
    - every : 해당 배열의 모든 요소가 조건에 맞아야 true 리턴, 그렇지 않다면 false 리턴
        > 즉, every 는 조건에 맞지 않는 요소를 찾아야만 검색을 멈추고 false 를 리턴
*/

const arr = [1, 2, 3, 4, 5,]
const even = arr.some(x => x%2 === 0) // 2에서 조건 만족하고 검색 멈춤, true 리턴
console.log(even) // true

// 6-1] 컴퓨터의 램이 16보다 큰 요소가 있는지를 some 과 every 로 비교
const COMPUTERS = [
    { name: 'macbook', ram: 16 },
    { name: 'gram', ram: 8 },
    { name: 'series9', ram: 32 },
]
const everyComputer = COMPUTERS.every(computer => computer.ram > 16)
console.log(everyComputer) // false

const someComputer = COMPUTERS.some(computer => computer.ram > 16)
console.log(someComputer) // true

// 6-2] USERS 배열에서 모두가 hasSubmitted 인지 아닌지를 hasSubmitted 에 저장하라
const STUDENTS = [
    { id: 21, hasSubmitted: true },
    { id: 33, hasSubmitted: false },
    { id: 712, hasSubmitted: true},
]
const hasSubmitted = STUDENTS.every(student => student.hasSubmitted)
console.log(hasSubmitted) // false

// 6-3] REQUESTS 배열에서 각 요청들 중 status 가 pending 인 요청이 있으면, inProgress 변수에 true 를 저장하라.
const REQUESTS = [
    { url: '/photos', status: 'complete' },
    { url: '/albums', status: 'pending' },
    { url: '/users', status: 'failed' },
]
const inProgress = REQUESTS.some(request => request.status === 'pending')
console.log(inProgress) // true