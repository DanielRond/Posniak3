# Project Guidelines

## Code Style
Este repositório reúne exercícios de programação competitiva em Python, seguindo o padrão procedural de ler, calcular e imprimir em um único arquivo.

Use entrada padrão com `input()` e, quando necessário, `map()` para múltiplos valores. Preserve a formatação exata das saídas com `f`-strings e especificadores como `:.2f` e `:.3f`, como nos arquivos [aumento.py](../aumento.py), [Atividade1/salario.py](../Atividade1/salario.py) e [Atividade1/bhaskara.py](../Atividade1/bhaskara.py).

## Build and Test
Não há infraestrutura de build ou testes neste workspace. Execute cada exercício diretamente com Python, normalmente fornecendo a entrada pela stdin, por exemplo `python aumento.py < input.txt`.

## Conventions
Mantenha os scripts independentes, sem classes, sem dependências externas e sem estrutura adicional desnecessária.

Ao alterar ou criar exercícios, preserve o contrato de entrada e saída do enunciado e evite introduzir tratamento de erro que altere o comportamento esperado para entradas válidas.