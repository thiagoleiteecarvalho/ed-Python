from typing import Optional

class No:
    def __init__(self, dado: int, filho_esquerdo=None, filho_direito=None):
        self.dado = dado
        self.filho_esquerdo = filho_esquerdo
        self.filho_direito = filho_direito


def insert(no: No, dado: int):
    
    if dado <= no.dado:
        if no.filho_esquerdo is None:
            no.filho_esquerdo = No(dado)
            return

        insert(no.filho_esquerdo, dado)

    else:
        if no.filho_direito is None:
            no.filho_direito = No(dado)
            return

        insert(no.filho_direito, dado)


def search(no: No, dado: int) -> Optional[No]:
    if no is None:
        return None

    if no.dado == dado:
        return no

    if dado <= no.dado:
        return search(no.filho_esquerdo, dado)

    return search(no.filho_direito, dado)

def delete(no: No, dado: int) -> Optional[No]:
    if no is None or no.dado == dado:
        return None

    if dado <= no.dado:
        no.filho_esquerdo = delete(no.filho_esquerdo, dado)
        return no

    no.filho_direito = delete(no.filho_direito, dado)
    return no

def imprimir_pre_ordem(no: No):

    print(no.dado + ' ')
    imprimir_pre_ordem(no.filho_esquerdo)
    imprimir_pre_ordem(no.filho_direito)

def imprimir_em_ordem(no: No):

    imprimir_pre_ordem(no.filho_esquerdo)
    print(no.dado + ' ')
    imprimir_pre_ordem(no.filho_direito)

def imprimir_pos_ordem(no: No):

    imprimir_pre_ordem(no.filho_esquerdo)
    imprimir_pre_ordem(no.filho_direito)
    print(no.dado + ' ')
