from typing import Optional

class No:
    def __init__(self, dado: int, filho_esquerdo=None, filho_direito=None):
        self.dado = dado
        self.filho_esquerdo = filho_esquerdo
        self.filho_direito = filho_direito


def inserir(no: No, dado: int) -> No:
    if no is None:
        return No(dado)

    if dado <= no.dado:
        if no.filho_esquerdo is None:
            no.filho_esquerdo = No(dado)
            return no

        return inserir(no.filho_esquerdo, dado)

    if no.filho_direito is None:
        no.filho_direito = No(dado)
        return no

    return inserir(no.filho_direito, dado)


def search(no: No, dado: int) -> Optional[No]:
    if no is None:
        return None

    if no.dado == dado:
        return no

    if dado <= no.dado:
        return search(no.filho_esquerdo, dado)

    return search(no.filho_direito, dado)

def delete(no: No, dado: int) -> Optional[No]:
    if no is None:
        return None

    if no.dado == dado:
        if no.filho_direito is not None:
            no.filho_direito.filho_esquerdo = no.filho_esquerdo
            return no.filho_direito

        return no.filho_esquerdo

    if dado <= no.dado:
        no.filho_esquerdo = remover_node(no.filho_esquerdo, dado)
        return no

    no.filho_direito = remover_node(no.filho_direito, dado)
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
