let varA = 'A';
let varB = 'B';
let varC = 'C';
let temp = varA 

varA = varB;
varB = varC;
varC = temp;


let varUM = '1';
let varDOIS = '2';
let varTRES = '3';

[varUM, varDOIS, varTRES] = [varDOIS, varTRES, varUM]

console.log(varA, varB, varC);
console.log(varUM, varDOIS, varTRES)