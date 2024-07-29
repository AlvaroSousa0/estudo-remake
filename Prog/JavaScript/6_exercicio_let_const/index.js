const nomeCompleto = 'Alvaro Sousa';
const idade = 18;
const peso = 90;
const altura = 1.81;
let anoNascimento = 2024 - idade
let IMC = peso / altura**2;

console.log(`${nomeCompleto} tem ${idade} anos, nascido em ${anoNascimento}, pesa ${peso}KG e mede ${altura}m, seu IMC é: ${IMC}`);