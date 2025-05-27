
def Fetch(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        lista = [linha.rstrip('\n') for linha in arquivo]
    return lista

# Checa se a Origem faz referencia a memoria
def checarSeMemoria(m: str) -> bool:
    return m.__contains__("[")

# Chega a referencia a memoria mas para o Destino
def checarSeMemoriaPDest(m: str) -> bool:
    return m.__contains__("[") or m.isdigit()


# Extrai o endereco de memoria em ambos os casos
def extrairEndMemoria(end: str) -> int:
    if end.__contains__("["):
        return int(end.strip("[]"))
    else:
        return int(end)


def main():

    registradores = {
        "R0": 0,
        "R1": 0,
        "R2": 0
    }

    PC = 0

    memoria = [0] * 64

    # Função FETCH
    inst = Fetch("test.txt")
    print(inst)

    for i in range(0, len(inst)):

        # Função DECODE
        Decoded = inst[i].replace(",", " ").split()
        print(Decoded)
        opcode, destino, origem = Decoded
        print(opcode, destino, origem)


        try:
            # Função EXECUTE
            Execute(opcode, destino, origem, registradores, memoria)
        except IndexError:
            print("memória de acesso nao permitido")
        PC += 1


def Execute(opcode, destino, origem, registradores, m):

    match opcode:
        case "ADD":
            ADD(destino, origem, registradores, m)




def ADD(dest:str, ori:str, registradores: dict[str,int], m: list[int]):

    if dest in registradores:
        if ori in registradores:
            registradores[dest] += registradores[ori]
        elif checarSeMemoria(ori):
            registradores[dest] += m[extrairEndMemoria(ori)]
        elif ori.isdigit():
            registradores[dest] += int(ori)

    elif checarSeMemoriaPDest(dest):
        end = extrairEndMemoria(dest)
        if ori in registradores:
            m[end] += registradores[ori]
        elif checarSeMemoria(ori):
            m[end] += m[extrairEndMemoria(ori)]
        elif ori.isdigit():
            m[end] += int(ori)



main()