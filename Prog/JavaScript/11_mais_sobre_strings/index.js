let string = "\"É uma string\\\"";

console.log(string);

console.log(string[13]);

console.log(string.concat(' somente isso'));
console.log(string,'somente isso');
console.log(`${string} somente isso`);

console.log(string.indexOf('\\', 10));

// console.log(string.match(/[a-z]/g));

console.log(string.replace('uma', 'outra'));
