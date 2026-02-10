Algoritmo "semnome"

Var
   media:real
   soma:real
   primeira_nota:real
   segunda_nota:real
   resultado:caracter
   nome:caracter
   idade:inteiro
   
Inicio
  escreva("digite seu nome:")
   
   leia(nome)
   
  escreva("digite sua idade:")
   
   leia(idade)

  escreva("digite a primeira nota:")
  
   leia(primeira_nota)
  
  escreva("digite a primeira nota:")
  
   leia(segunda_nota)
  
  escreva("digite a terceira nota:")
  

  
  soma <- primeira_nota + segunda_nota
  
  media <- soma / 2
  
  
  se    media >= 7  entao
        resultado   <- "aprovado"
  senao
       resultado  <- "reprovado"
  fimse
   
  
  
  escreval
  
  escreval("soma:",soma)
  escreval("media:",media)
  escreval("resultado:",resultado)
  
  

Fimalgoritmo