# 🖥️ Simulador de CPU em Python

Este projeto é um simulador simples de CPU, desenvolvido em Python, que interpreta e executa instruções escritas em um arquivo de texto. Ele simula operações básicas de registradores e memória, servindo como uma introdução prática à arquitetura de computadores.

## 📁 Estrutura dos Arquivos

```
.
├── simulador_cpu.py   # Código-fonte do simulador da CPU
└── test.txt           # Arquivo com instruções a serem executadas
```

## ⚙️ Funcionalidades

O simulador é capaz de:

- Carregar valores diretamente ou da memória para registradores
- Armazenar valores dos registradores na memória
- Somar valores entre registradores
- Encerrar a execução com a instrução `HLT`

Os registradores disponíveis são: `R0`, `R1` e `R2`. A memória possui 64 posições numeradas de 0 a 63.

## ▶️ Como Usar

1. Certifique-se de ter o Python 3 instalado.
2. Coloque suas instruções no arquivo `test.txt`.

Durante a execução, o estado dos registradores e parte da memória será exibido a cada instrução.

## 📄 Exemplo de Instruções (`test.txt`)

```txt
# Meu primeiro programa para a CPU simulada
LOAD R0, 5
LOAD R1, 12
ADD R0, R1
STORE [30], R0
LOAD R2, [30]
HLT
```

### Explicação:

- `LOAD R0, 5`: Carrega o valor 5 em R0
- `LOAD R1, 12`: Carrega o valor 12 em R1
- `ADD R0, R1`: Soma R1 em R0 (R0 = 17)
- `STORE [30], R0`: Armazena R0 na memória posição 30
- `LOAD R2, [30]`: Carrega da memória[30] para R2
- `HLT`: Interrompe a execução

## 🎯 Objetivo

Este simulador foi desenvolvido como parte de um trabalho acadêmico para demonstrar conceitos fundamentais de operação de CPUs, como registradores, memória e instruções básicas.
