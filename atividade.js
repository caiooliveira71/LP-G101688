// CALCULE A MEDIA ARITMETICA DO VETOR ABAIXO:
// UTILIZI OS RECURSOS DO ES6

notas = [10,10,10]

console.log("\nExibindo media aritmedica do vetor:")
const soma = notas.reduce((soma, atual) => soma + atual / 3, 0)
console.log(soma)