# Javascript Fundamental

Most information sythenized from https://javascript.info/

JavaScript runs in a browser on client-side. HTML has script tags that loads and executes the Javascript using the browsers engine. 
JavaScript can also run server side using tools like Node.

## Variables

- let twoWords = 'Austin Hackett'
- CONST TWO_WORDS = 'AUSTIN HACKETT

## Data Types

- Javascript is dynamically typed 
- Specific Data Types
  - Number = Float/Integer/etc. 
  - BigInt = Number with a n at the end
  - String = Character types that come with helper methods.
  - Boolean = True/False
  - Null = represents Nothing
  - Undefined = Value has nothing assigned to it
  - Object = Data/Methods
  - Symbol = 

## Arithmetic
- Typical arithmetic, nothing super special. See Programming fundamentals.

## Comparisons
- Nothing that needs to be noted on how things compare besides the low.
  - A number 0, an empty string "", null, undefined, and NaN all become false. Because of that they are called “falsy” values.

## Conditionals
- Nothing special, see Fundamenetals
  - Teneranay operations = ``` (isMember ? '$2.00' : '$10.00'); ```

## Loops
- Nothing special. See Fundamenetals

## Switch Statements 
- Nothing special. See Fundamentals.

## Functions
```
function showMessage(hello) {
    console.log(hello)
  return hello
}
```

- Functions can have local variables and access outer variables.
- Short hand Function expressions can also be defined using arrow functions
```
let sum = (a, b) => {  // the curly brace opens a multiline function
  let result = a + b;
  return result; // if we use curly braces, then we need an explicit "return"
};
```
- Can pass indefinite variables with ...args or access through arguments[]
- Spread Syntax can be used with objects as well with ...
- Scope in JS is defined by Lexical Environments (the local scope of a specifi code block). If a variable referenced is not found, it will travel up the Lexical chain to find the variable.
- Thats why we have Closures, a function that encaspulates another function that we assign to a variable. The outer function typically stores a value that the inner function can continually reference.

## Data Types
- Lots of transferrable fundamental knowledge here. Will add specifics when I see fit.

## Protypes
### Potypal Inhereitance
- In JavaScript, all objects have a hidden [[Prototype]] property that’s either another object or null.
- We can use obj.__proto__ to access it (a historical getter/setter, there are other ways, to be covered soon).
- The object referenced by [[Prototype]] is called a “prototype”.
- If we want to read a property of obj or call a method, and it doesn’t exist, then JavaScript tries to find it in the prototype.
- Write/delete operations act directly on the object, they don’t use the prototype (assuming it’s a data property, not a setter).
- If we call obj.method(), and the method is taken from the prototype, this still references obj. So methods always work with the current object even if they are inherited.
- The for..in loop iterates over both its own and its inherited properties. All other key/value-getting methods only operate on the object itself.

```
let animal = {
  eats: true
};
let rabbit = {
  jumps: true
};

rabbit.__proto__ = animal; // (*)

// we can find both properties in rabbit now:
alert( rabbit.eats ); // true (**)
alert( rabbit.jumps ); // true
```
### F.prototype
- The F.prototype property (don’t mistake it for [[Prototype]]) sets [[Prototype]] of new objects when new F() is called.
- The value of F.prototype should be either an object or null: other values won’t work.
- The "prototype" property only has such a special effect when set on a constructor function, and invoked with new.

### Modern Prototypes
- Object.create(proto, [descriptors]) – creates an empty object with a given proto as [[Prototype]] (can be null) and optional property descriptors.
- Object.getPrototypeOf(obj) – returns the [[Prototype]] of obj (same as __proto__ getter).
- Object.setPrototypeOf(obj, proto) – sets the [[Prototype]] of obj to proto (same as __proto__ setter)

## Classes
### Basic Structure
```
class MyClass {
  prop = value; // property

  constructor(...) { // constructor
    // ...
  }

  method(...) {} // method

  get something(...) {} // getter method
  set something(...) {} // setter method

  [Symbol.iterator]() {} // method with computed name (symbol here)
  // ...
}
```
### Inheritance
```
class Animal {
  constructor(name) {
    this.speed = 0;
    this.name = name;
  }
  run(speed) {
    this.speed = speed;
    alert(`${this.name} runs with speed ${this.speed}.`);
  }
  stop() {
    this.speed = 0;
    alert(`${this.name} stands still.`);
  }
}

let animal = new Animal("My animal");

class Rabbit extends Animal {
  hide() {
    alert(`${this.name} hides!`);
  }
    stop() {
    super.stop(); // call parent stop
    this.hide(); // and then hide
  }
}

let rabbit = new Rabbit("White Rabbit");

rabbit.run(5); // White Rabbit runs with speed 5.
rabbit.hide(); // White Rabbit hides!
```

## Promises
- The ability to execute code on execution of a previous function that runs async
```
function loadScript(src) {
  return new Promise(function(resolve, reject) {
    let script = document.createElement('script');
    script.src = src;

    script.onload = () => resolve(script);
    script.onerror = () => reject(new Error(`Script load error for ${src}`));

    document.head.append(script);
  });
}

let promise = loadScript("https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.11/lodash.js");

promise.then(
  script => alert(`${script.src} is loaded!`),
  error => alert(`Error: ${error.message}`)
);

promise.then(script => alert('Another handler...'));
```

### Promise Chaining
```
function loadJson(url) {
  return fetch(url)
    .then(response => response.json());
}

function loadGithubUser(name) {
  return fetch(`https://api.github.com/users/${name}`)
    .then(response => response.json());
}

function showAvatar(githubUser) {
  return new Promise(function(resolve, reject) {
    let img = document.createElement('img');
    img.src = githubUser.avatar_url;
    img.className = "promise-avatar-example";
    document.body.append(img);

    setTimeout(() => {
      img.remove();
      resolve(githubUser);
    }, 3000);
  });
}

// Use them:
loadJson('/article/promise-chaining/user.json')
  .then(user => loadGithubUser(user.name))
  .then(showAvatar)
  .then(githubUser => alert(`Finished showing ${githubUser.name}`));
  // ...
```
### Other Promise API
- Proceeds only if all to finish
```
Promise.all([
  new Promise(resolve => setTimeout(() => resolve(1), 3000)), // 1
  new Promise(resolve => setTimeout(() => resolve(2), 2000)), // 2
  new Promise(resolve => setTimeout(() => resolve(3), 1000))  // 3
]).then(alert); // 1,2,3 when promises are ready: each promise contributes an array member
```
- Proceeds no matter how many finish
```
let urls = [
  'https://api.github.com/users/iliakan',
  'https://api.github.com/users/remy',
  'https://no-such-url'
];

Promise.allSettled(urls.map(url => fetch(url)))
  .then(results => { // (*)
    results.forEach((result, num) => {
      if (result.status == "fulfilled") {
        alert(`${urls[num]}: ${result.value.status}`);
      }
      if (result.status == "rejected") {
        alert(`${urls[num]}: ${result.reason}`);
      }
    });
  });
```
- Proceeds on first finish
```
Promise.race([
  new Promise((resolve, reject) => setTimeout(() => resolve(1), 1000)),
  new Promise((resolve, reject) => setTimeout(() => reject(new Error("Whoops!")), 2000)),
  new Promise((resolve, reject) => setTimeout(() => resolve(3), 3000))
]).then(alert); // 1
```
### Async/Await
```
async function f() {

  try {
    let response = await fetch('/no-user-here');
    let user = await response.json();
  } catch(err) {
    // catches errors both in fetch and response.json
    alert(err);
  }
}

f();
```