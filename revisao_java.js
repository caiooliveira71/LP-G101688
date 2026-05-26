// CRIANDO UM VETOR
const vetorNumero = [10,20,30,40,50]

console.log('Exibindo todos os elementos:')
console.log(vetorNumero)

console.log('\nExibindo apenas o primeiro elemento:')
console.log(vetorNumero[0])

console.log('\nExibindo apenas o segundo elemento:')
console.log(vetorNumero[1])

console.log('\nExibindo apenas o terceiro elemento:')
console.log(vetorNumero[2])

console.log('\nExibindo apenas o quarto elemento:')
console.log(vetorNumero[3])

console.log('\nAdicionando um elemento no final do vetor:')
vetorNumero.push(60)
console.log(vetorNumero)

console.log('\nAdicionando um elemento no inicio do vetor:')
vetorNumero.unshift(60)
console.log(vetorNumero)

console.log('\nRemovendo o elemento final do vetor:')
vetorNumero.pop()
console.log(vetorNumero)

console.log('\nAdicionando um elemento no final do vetor:')
vetorNumero.shift()
console.log(vetorNumero)
