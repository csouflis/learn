// Functions are an object datatype

console.log('FUNCTIONS');



//function expression (storing a function inside a vairable)
const speak = function(){
    console.log('Expressed function as an object');
};

greet();
speak();

//function declaration 
function greet(){
    console.log('Hoisted declaration');
}

console.log('Hoisting works with functions declarations, but not function expression because the variable of function has not yet been declared');
console.log('')


//arguments and parameters
const hello = function(name = 'jacob'){
    console.log(`hello ${name}`);
};

//passing in arguments
hello('john');

//returning values
const calc_circle_Area = function(radius){
    return 3.14 * radius**2;
};

small_circle_area = calc_circle_Area(5);
console.log(small_circle_area);

console.log('');

// arrow function
const calc_sqr_area = (length, width) => length*width;

console.log(calc_sqr_area(5,3))

console.log('');

//callbacks and foreach
let people = ['ronna', 'irene', 'jimbo', 'fedori', 'climp', 'westward'];

//callback function for foreach below
const logPerson = (person, index) => console.log(`${index} - Hello ${person}`);

people.forEach(logPerson);


console.log('');
//connect to ul block in html
const ul = document.querySelector('.people');
let html = ``;

people.forEach((person) =>{
    html += `<li style="color:purple">${person}</li>`;
});

console.log(html)
ul.innerHTML = html;
