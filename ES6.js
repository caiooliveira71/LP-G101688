const vetor = [10,20,30,40,50]

console.log('Listando todos os elementos do vetor:')
console.log(vetor)

console.log('\nMultiplicando todos os elementos do vetor por 2:')
const dobrador = vetor.map(n => n *2)
console.log(dobrador)

console.log('\nFiltrando elementos impares:')
vetor.push(1)
vetor.push(3)
const impares = vetor.filter(n => n % 2 == 1)
console.log(impares)

console.log('\nFiltrando elementos impares:')
const pares = vetor.filter(n => n % 2 == 0)
console.log(pares)

console.log('\nFiltrando elementos negativos:')
vetor.push(-30)
vetor.push(-40)
const negativos = vetor.filter(n => n < 0)
console.log(negativos)

console.log('\nSomando todos os elementos do vetor:')
const total = vetor.reduce((soma, atual) => soma + atual, 0)
console.log(total)