const obj1 = { foo: 'bar', x: 30 }
const obj2 = { foo: 'baz', y: 10 }

const ssafy = { ...ob1 }
// { foo: 'bar', x: 30}
const ssafy2 = { ...ob1, ...ob2 }
// { foo: 'baz', x: 30, y: 10 }