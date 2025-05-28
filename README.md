# Simulador de CPU em Python

Este repositório contém um projeto simples que simula o funcionamento de uma CPU utilizando Python. O programa lê um arquivo de texto contendo instruções e executa cada comando de forma organizada, reproduzindo o comportamento básico de um processador.

## 📁 Estrutura do Projeto

```
.
├── cpu_simulador.py        # Script principal em Python que executa as instruções
└── instrucoes.txt          # Arquivo de texto com as instruções simuladas
```

## ⚙️ Como Funciona

1. O arquivo `test.txt` contém uma lista de comandos que representam instruções de uma CPU.
2. O script `simulador_cpu.py` interpreta e executa essas instruções, simulando o comportamento de uma CPU simples.
3. Cada linha do arquivo é processada de forma sequencial, podendo incluir operações como carregamento de dados, somas, subtrações, armazenamento em registradores, entre outros.

## 📄 Exemplo de Instruções (`instrucoes.txt`)

```txt
LOAD A, 5
LOAD B, 10
ADD A, B
STORE C, A
PRINT C
```

Neste exemplo, o simulador:
- Carrega os valores 5 e 10 nos registradores A e B,
- Soma A com B,
- Armazena o resultado em C,
- E imprime o valor final de C.

## 🚀 Objetivo

Este projeto foi criado como parte de um trabalho acadêmico para demonstrar de forma simples como uma CPU pode interpretar e executar instruções em baixo nível. É uma ferramenta útil para compreensão dos princípios básicos de arquitetura de computadores.
