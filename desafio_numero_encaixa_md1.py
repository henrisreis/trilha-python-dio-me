"""
// Encaixa ou Não?

/*
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu
que construísse um programa para verificar, à partir de dois valores muito
grandes A e B, se B corresponde aos últimos dígitos de A.

- Entrada

A entrada consiste de vários casos de teste. A primeira linha de entrada
contém um inteiro N que indica a quantidade de casos de teste. Cada caso de
teste consiste de dois valores A e B maiores que zero, cada um deles podendo
ter até 1000 dígitos.

- Saída

Para cada caso de entrada imprima uma mensagem indicando se o segundo valor
encaixa no primeiro valor, conforme exemplo abaixo.
*/
"""

print('Verificando se o segundo número encaixa no primeiro')
n = int(input('Digite o número de vezes que deseja verificar: '))

while n > 0:

    a, b = input('Digite dois números separados por um espaço => primeiro_numero segundo_numero: ').split()

    numeros_invalidos = True if int(a) <= 0 or int(b) <= 0 else False
    digitos_invalidos = True if len(a) > 1000 or len(b) > 1000 else False

    if numeros_invalidos or digitos_invalidos:
        print('Número inválido!')
        continue

    comprimento_fatia = len(b) * (-1)
    a_fatiado = a[comprimento_fatia:]
    
    if a_fatiado == b:
        print('Encaixa!')

    else:
        print('Não encaixa!')    

    n -= 1
