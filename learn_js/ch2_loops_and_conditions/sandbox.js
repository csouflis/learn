// FOR LOOPS
//   let i = 0  -- initialization of loop variable
//   i < 5  -- condition where true means to run the loop code block, false is to break
//   i++  -- final expression that executes at end of loop code block
console.log('FOR LOOPS');
for(let i = 0; i < 5; i++){
    console.log('in loop:', i);
}
console.log('finished!');

const names = ['mario', 'luigi', 'yoshi', 'peach'];

for(let i = 0; i < names.length; i++){
//  console.log('Name #', i, ':',names[i])
    let html = `<div>${names[i]}</div>`;
    console.log(html);
}


//breaks and continues (and if statements from below)
for(let i = 0; i < names.length; i++){ 
    
    if(names[i]=='luigi'){
        continue;
    }
    
    console.log('Name #', i, ':',names[i]);
    
    if(names[i]=='yoshi'){
        console.log('egged!')
        break;
    }
}





// WHILE LOOPS
console.log('');
console.log('WHILE LOOPS');

let i=0;

while(i<5){
    console.log('in loop:', i);
    i++;
}

i=0;
while(i<names.length){
    console.log(names[i]);
    i++;
}

//do while (does an iteration at least once!)
i = 5;
do{
    console.log('val of i is:', i);
    i++;
} while(i < 5);





// IF STATEMENTS
console.log('');
console.log('IF STATEMENTS');
console.log('if something is true: execute');

const age = 25;
let young;
if(age > 20){
    console.log('you are over 20 years old.')
    young = false;
}

// using ! (not)
if(!young){
    console.log('you are old!')
    
}

//chained if statements
const password = 'p@ssword1234';

if(password.length >= 12){
    console.log('password is mighty strong!')
}
else if(password.length >= 8){
    console.log('password is long enough.')
}
else{
    console.log('password is not long enough.')
}
// and

if(password.length >= 8 && password.includes('@')){
    console.log('best password ever (using &&)')
}

//second part counts as one condition!
if(password.includes('*') || password.length >= 8 && password.includes('@')){
    console.log('okay password (using ||)')
}


//switch statements
const grade = 'B';

switch(grade){
    case 'A':
        console.log('A grade!');
        break;
    case 'B':
        console.log('B grade!');
        break;
    case 'C':
        console.log('C grade!');
        break;
    case 'D':
        console.log('D grade!');
        break;
    case 'E':
        console.log('E grade!');
        break;
    default:
        console.log('Invalid grade');
}

//global and local scopes
const score = 30;

if(true){
    let score = 40;
    let team = 'Lakers';
    console.log(team, score);
}

//cannot access team (would get error)
console.log(score);


