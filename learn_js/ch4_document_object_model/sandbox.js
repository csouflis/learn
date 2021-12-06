// grabs 1st p-tag CSS style
//      can grab selectors easily in web-inspector by right-click > copy selector
const para = document.querySelector('div.error');
console.log(para);

// grabs all elements with specified tag
const paras = document.querySelectorAll('p');
console.log(paras);

// forEach arrow function to go through all selected tags in a NodeList
paras.forEach(para => {console.log(para)});

console.log(' ');
//get an element by ID
const title = document.getElementById('page_title');
console.log(title);

//get elements by class name  --> cannot use a forEach on an HTMLCollection
const errors = document.getElementsByClassName('error');
console.log(errors);
console.log(errors[0]);

//get elements by their tag name
const p_tags = document.getElementsByTagName('p');
console.log(p_tags);


console.log(' ');
// use document queries to change content
const one_para = document.querySelector('p');
console.log(one_para.innerHTML);
one_para.innerHTML = 'goodbye world'; //changes text on page


console.log(' ');
const content = document.querySelector('.content');
content.innerHTML += '<h2>THIS IS A NEW H2</h2>'; // can replace/add content 
// cycle through data to display it in certain area
const people = ['jen', 'raul', 'martin'];
people.forEach(person => {
    content.innerHTML += `<p>${person}</p>`
});


console.log(' ');
const link = document.querySelector('a');
console.log(link.getAttribute('href'));
link.setAttribute('href', 'https://www.google.com/imghp');
link.innerHTML = 'google images';

// getting and setting element attribute
const mssg = document.getElementsByClassName('error')[0];
mssg.setAttribute('class', 'success');
mssg.setAttribute('style', 'color:green'); //not good to restyle this way (see below)
console.log(mssg);


//querying style
console.log(' ');
const h3_title = document.querySelector('h3');
console.log(h3_title.style); // returns CSS style properties
console.log(h3_title.style.color);
//better to change style this way because it does not overwrite other styles
h3_title.style.margin = '50px';


//classes & querying
console.log(' ');
console.log(content);
content.classList.remove('content'); // takes away this class and CSS styling
content.classList.add('test'); // takes on the styling of this class with CSS










