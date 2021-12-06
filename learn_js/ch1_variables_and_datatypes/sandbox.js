//log things to console
alert('Hello World!');
console.log(1);
console.log(2);
console.log(3);

//creating first variables
let age = 25;
let year = 2021;
age = 30;
console.log('Age and Year using let variable declaration.');
console.log('Age:', age, 'Year:', year);

//using the const unchangeable variables
const points = 100;
console.log('const variable:', points);

//older var variable declaration --> will be using let and const
var score = 75;
console.log('older var variable declaration:', score);



console.log(' ')
/////Strings Datatypes/////
console.log('string datatypes'.toUpperCase())

//strings act similarly to python in that they can be concatenated by '+',
//         'string[]' to get a character, and string.length to get length
// other common string methods below
let first_name = 'Captain';
let last_name = 'Price';
let full_name = first_name + ' ' + last_name;
console.log('Full name:', full_name);
console.log('Upper:', full_name.toUpperCase());
console.log('Lower:', full_name.toLowerCase());

let index = full_name.indexOf('P');
console.log("Index of letter 'P':", index);

let email = 'cprice@sas.uk';
console.log('Email:', email);

let lastIndex = email.lastIndexOf('s');
console.log("Last index of 's':", lastIndex);

let sliced = email.slice(0, email.indexOf('@'));
console.log('Sliced string:', sliced);

let substr = email.substr(2, 4);
console.log('Substringed:', substr);

let replacement = email.replace('c', 'j');
console.log('Replacement:', replacement);

///slightly different datatype called template strings
const book_title = 'Foundation';
const book_author = 'Isaac Asimov';
const book_likes = 5546949;
let book;

//concatentation way (old way)
book = 'The book called ' + book_title + ' by ' + book_author + ' has ' + book_likes + ' likes.';
console.log(book);

//template string way
book = `The book called ${book_title} by ${book_author} has ${book_likes} likes.`;
console.log(book);

//creating html templates
let html = `
    <h2>${book_title}</h2>
    <p>By ${book_author}</p>
    <span>This book has ${book_likes} likes </span>
`;
console.log(html);



console.log(' ')
/////Numbers Datatype/////

console.log('number datatypes'.toUpperCase())
let radius = 10;
const pi = 3.14;

// math operators +, -, *, /, **, %
let area = pi * radius ** 2;
console.log('Area of circle:', area);

//order of operations - B I D M A S 
//     (brackets, indices, division, multiplication, addition, subtraction)
let likes = 10;
console.log('Likes:', likes);
likes++;
console.log('Likes:', likes);
likes--;
console.log('Likes:', likes);
likes += 10;
console.log('Likes:', likes);
likes *= 3;
console.log('Likes:', likes);
likes /= 4;
console.log('Likes:', likes);

//NaN - not a number
console.log(5 / 'hello');

//concatenate numbers
let string_num = 'The blog has ' + likes + ' likes.';
console.log(string_num);



console.log(' ')
/////Array Datatypes/////
console.log('array datatypes'.toUpperCase())

let dogs = ['Louie', 'Duke', 'Sola'];
dogs[1] = 'Sandy';
console.log(dogs[1]);
console.log('Array length:', dogs.length)

let randoms = ['Krystal', 'Kyle', 33, 36];
console.log(randoms);

//array methods
let joined = dogs.join('-');
console.log(joined);

let array_index = dogs.indexOf('Sola');
console.log(array_index);

let array_concat = dogs.concat(['Barney', 'Ooba']);
console.log(array_concat);

let array_push = dogs.push('Brody');
console.log(array_push); //returns length of new array
console.log(dogs); //destructive method b/c changes original value

let array_pop = dogs.pop();
console.log(array_pop); //returns value of popped
console.log(dogs); //destructive method b/c changes original value



console.log(' ')
/////Null and Undefined Datatypes/////
console.log('null and undefined datatypes'.toUpperCase())

let carrots;
console.log(carrots, carrots + 3, `the age is ${carrots}`);
carrots = null;
console.log(carrots, carrots + 3, `the age is ${carrots}`);



console.log(' ')
/////Boolean Datatypes/////
console.log('boolean datatypes'.toUpperCase())

// True or False values
console.log('Using email string:', email);
console.log('Using dogs array:', dogs);

let include = email.includes('@');
console.log(include);

include = dogs.includes('Bob');
console.log(include);

//comparison operators
let seeds = 25;
console.log(seeds);
console.log(seeds == 23);
console.log(seeds != 30);
console.log(seeds >= 30);
//loose comparison
console.log('Loose comparisons');
console.log(seeds == '25');
console.log(seeds != '25');
//strict comparison
console.log('Strict comparisons');
console.log(seeds === '25');
console.log(seeds !== '25');



console.log(' ')
/////Type Conversion/////
console.log('conversions of datatypes'.toUpperCase())

let lives = '100';
console.log(typeof lives)
console.log(lives)

lives = Number(lives);
console.log(typeof lives)
console.log(lives + 1);

lives = String(lives);
console.log(typeof lives)
console.log(`Number of lives: ${lives}`);

//truthy and falsey values
let result = Boolean(100);
console.log(result, typeof result) //numbers other than 0  are truthy values

result = Boolean(0)
console.log(result, typeof result) // 0 is falsey value

result = Boolean('0')
console.log(result, typeof result) //all strings that are not empty are truthy

result = Boolean('')
console.log(result, typeof result) //all strings that are not empty are truthy
