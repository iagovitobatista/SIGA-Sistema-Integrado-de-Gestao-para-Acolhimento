"""SIGA 1.0 — demonstração acadêmica com dados fictícios.
Reimplementação ilustrativa baseada nas funcionalidades apresentadas nos prints
do notebook original. Não é uma extração literal do código do Colab.
"""
import sqlite3
from pathlib import Path

BANCO = Path(__file__).resolve().parent / "siga_demo.db"
TOTAL_LEITOS = 80  # Capacidade de exemplo; não representa serviço real.


def conectar():
    return sqlite3.connect(BANCO)


def iniciar():
    with conectar() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS acolhidos (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT NOT NULL,
          idade INTEGER NOT NULL CHECK(idade BETWEEN 0 AND 120),
          leito INTEGER UNIQUE NOT NULL CHECK(leito BETWEEN 1 AND 80)
        )""")


def inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v = int(input(mensagem).strip())
            if minimo <= v <= maximo:
                return v
        except ValueError:
            pass
        print(f"Informe um número inteiro entre {minimo} e {maximo}.")


def cadastrar():
    nome = input("Nome fictício: ").strip()
    if not nome:
        print("Nome obrigatório.")
        return
    idade = inteiro("Idade: ", 0, 120)
    leito = inteiro("Leito: ", 1, TOTAL_LEITOS)
    try:
        with conectar() as conn:
            conn.execute("INSERT INTO acolhidos(nome, idade, leito) VALUES (?, ?, ?)",
                         (nome, idade, leito))
        print("Cadastro realizado.")
    except sqlite3.IntegrityError:
        print("Leito já ocupado.")


def consultar():
    with conectar() as conn:
        dados = conn.execute("SELECT id, nome, idade, leito FROM acolhidos ORDER BY leito").fetchall()
    if not dados:
        print("Nenhum cadastro encontrado.")
    for ident, nome, idade, leito in dados:
        print(f"ID {ident} | {nome} | {idade} anos | Leito {leito}")


def situacao():
    with conectar() as conn:
        ocupados = conn.execute("SELECT COUNT(*) FROM acolhidos").fetchone()[0]
    print(f"Total: {TOTAL_LEITOS} | Ocupados: {ocupados} | Livres: {TOTAL_LEITOS - ocupados}")


def liberar():
    leito = inteiro("Leito para liberar: ", 1, TOTAL_LEITOS)
    with conectar() as conn:
        cursor = conn.execute("DELETE FROM acolhidos WHERE leito = ?", (leito,))
    print("Leito liberado." if cursor.rowcount else "Leito já está livre.")


def buscar():
    termo = input("Nome para buscar: ").strip()
    with conectar() as conn:
        dados = conn.execute("SELECT nome, idade, leito FROM acolhidos WHERE nome LIKE ?",
                             (f"%{termo}%",)).fetchall()
    for nome, idade, leito in dados:
        print(f"{nome} | {idade} anos | leito {leito}")
    if not dados:
        print("Nenhum cadastro encontrado.")


def main():
    iniciar()
    opcoes = {'1': cadastrar, '2': consultar, '3': situacao,
              '4': liberar, '5': buscar}
    while True:
        print("\n🏠 SIGA — MENU PRINCIPAL")
        print("1 - Cadastrar acolhido\n2 - Consultar acolhidos\n3 - Situação dos leitos")
        print("4 - Liberar leito\n5 - Buscar acolhido\n0 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '0':
            break
        acao = opcoes.get(opcao)
        acao() if acao else print("Opção inválida.")


if __name__ == '__main__':
    main()
