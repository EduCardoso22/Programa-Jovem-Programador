programa {
  funcao inicio() {

  real n1,n2,n3,soma,div,mult,sub
  inteiro op,op2,anobi

  escreva ("Opções \n 1-Calculadora \n 2-Ano Bissexto \n 3- Par ou ímpar: ")
  leia(op2)
    escolha(op2) {
      
      caso 1:
  escreva ("Digite o primeiro número: ")
  leia(n1)
  escreva ("Digite o segundo número: ")
  leia(n2)
  escreva ("Digite o terceiro número: ")
  leia(n3)
  escreva ("Opções: \n 1 - Soma \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n 5-Ano Bissexto \n 6-Par ou Impar \n Digite o número referente a qual operação deseja realizar: ")
  leia(op)
  
  escolha(op) {

    caso 1:
      soma=n1+n2+n3
      escreva("A soma dos números é igual à: ", soma)
    pare
    caso 2:
      sub=n1-n2-n3
      escreva("A subtração dos números é igual à: ", sub)
    pare
    caso 3:
      mult=n1*n2*n3
      escreva("A multiplicação dos números é igual à: ", mult)
    pare
    caso 4:
      div=n1/n2/n3
      escreva("A divisão dos números é igual à: ", div)
    pare
  }
    pare
  caso 2:
  escreva ("Digite o ano: ")
  leia (anobi)

  se(anobi % 4 == 0) {
    escreva("É ano bissexto!")
  }
  senao {
    escreva("Não é ano bissexto!")
  }
  pare

  caso 3:
  escreva("Digite o número: ")
  leia(n1)
  se(n1 % 2 == 0) {
    escreva("É um número par!")
  }
  senao {
    escreva("É um número ímpar!")
  }
  pare
    }
  }
}
