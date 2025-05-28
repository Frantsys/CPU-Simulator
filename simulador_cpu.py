# Definindo memória e registradores
memoria = [0] * 64
registradores = {
    "R0": 0,
    "R1": 0,
    "R2": 0,
}

PC = 0  # Contador do Programa

# Carregar programa
def carregar_programa(nome_arquivo):
    instrucoes = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.split('#')[0].strip()
            if linha:
                instrucoes.append(linha)
    return instrucoes

# Função de execução da CPU
def executar_programa(instrucoes):
    global PC
    while PC < len(instrucoes):
        instrucao = instrucoes[PC]
        print(f"Executando: {instrucao}")
        executar_instrucao(instrucao)
        print_estado()
        if instrucao.strip().upper() == 'HLT':
            break
        PC += 1

# Decodificação e execução das instruções
def executar_instrucao(instrucao):
    tokens = instrucao.replace(',', '').split()
    if not tokens:
        return
    cmd = tokens[0].upper()

    if cmd == "LOAD":
        reg, fonte = tokens[1], tokens[2]
        if fonte.startswith('[') and fonte.endswith(']'):
            endereco = int(fonte[1:-1])
            registradores[reg] = memoria[endereco]
        else:
            registradores[reg] = int(fonte)

    elif cmd == "STORE":
        endereco = int(tokens[1][1:-1])
        memoria[endereco] = registradores[tokens[2]]

    elif cmd == "ADD":
        reg_dest, reg_fonte = tokens[1], tokens[2]
        registradores[reg_dest] += registradores[reg_fonte]

    elif cmd == "HLT":
        pass

    else:
        raise ValueError(f"Instrução desconhecida: {cmd}")

# Mostrar estado dos registradores e parte da memória
def print_estado():
    print(f"R0: {registradores['R0']} | R1: {registradores['R1']} | R2: {registradores['R2']} | PC: {PC}")
    print(f"Memória[30]: {memoria[30]}")
    print("--------------------------")

# Exemplo de execução
if __name__ == "__main__":
    nome_arquivo = "test.txt"
    instrucoes = carregar_programa(nome_arquivo)
    executar_programa(instrucoes)