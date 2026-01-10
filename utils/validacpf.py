import re

def valida_cpf(cpf: str | int) -> bool:
    cpf = str(cpf)
    cpf = re.sub(r"[^0-9]", "", cpf)

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2] # Elimina os dois últimos dígitos do cpf
    reverso = 10 # Contador reverso
    total = 0

    # Loop do cpf
    for index in range(19):
        if index > 8: # Primeiro índice vai de 0 a 9
            index -= 9 # São os 9 primeiros dígitos do cpf

        total += int(novo_cpf[index]) * reverso # Valor total da multiplicação

        reverso -= 1 # Decrementa o valor reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9: # Se o dígito for maior que 9 o valor é 0
                d = 0

            total = 0 # zera o total
            novo_cpf += str(d) # Concatena o dígito gerado no novo cpf

    # Evita sequências. Ex: 111111111-11
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências também avaliam como verdadeiro, então também adicionei
    # essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        return True
    return False

