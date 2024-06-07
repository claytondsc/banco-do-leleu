import os
import platform

saldo = 1150.99

def limpar_terminal():
    # Detecta o sistema operacional e executa o comando apropriado para limpar o terminal
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mensagem():
    print(""" 
    =========BANCO DO LELÉU==========
    
      QUAL OPERAÇÃO DESEJA REALIZAR?
      
      1. SALDO
      2. SAQUE
      3. DEPÓSITO
      0. SAIR

    =================================
    """)

def menu_de_selecao():
    while True:
        mensagem()
        try:
            comando = int(input("Digite a opção desejada: "))
            return comando
        except ValueError:
            limpar_terminal()
            print("Entrada inválida. Por favor, digite um número.")

def realizar_saque(saldo):
    limpar_terminal()
    while True:
        try:
            valor_saque = float(input("QUAL VALOR DESEJA SACAR? "))
            if valor_saque <= 0:
                limpar_terminal()
                print("DIGITE UM VALOR POSITIVO")
            elif valor_saque > saldo:
                limpar_terminal()
                print("SALDO INSUFICIENTE PARA O SAQUE")
            else:
                saldo -= valor_saque
                limpar_terminal()
                print(f"SAQUE REALIZADO: {valor_saque:.2f}")
                break
        except ValueError:
            limpar_terminal()
            print("Entrada inválida. Por favor, digite um número.")
    return saldo

def realizar_deposito(saldo):
    limpar_terminal()
    while True:
        try:
            valor_deposito = float(input("QUAL VALOR DESEJA DEPOSITAR EM SUA LELÉU CONTA? "))
            if valor_deposito <= 0:
                limpar_terminal()
                print("DIGITE UM VALOR POSITIVO")
            else:
                saldo += valor_deposito
                limpar_terminal()
                print(f"VALOR DEPOSITADO: {valor_deposito:.2f}")
                break
        except ValueError:
            limpar_terminal()
            print("Entrada inválida. Por favor, digite um número.")
    return saldo

def consultar_saldo(saldo):
    limpar_terminal()
    print(f"SEU SALDO É: {saldo:.2f}")

def continuar_ou_sair():
    while True:
        resposta = input("\nDeseja continuar ou sair? (c/s): ").strip().lower()
        if resposta == 'c':
            return True
        elif resposta == 's':
            return False
        else:
            print("Opção inválida. Por favor, digite 'c' para continuar ou 's' para sair.")

# Loop principal do menu
while True:
    limpar_terminal()
    comando = menu_de_selecao()
    if comando == 1:
        consultar_saldo(saldo)
    elif comando == 2:
        saldo = realizar_saque(saldo)
    elif comando == 3:
        saldo = realizar_deposito(saldo)
    elif comando == 0:
        limpar_terminal()
        print("TENHA UM LELÉU DIA! :)\n.\n.\n.\n.")
        break
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA")
    
    # Pergunta ao usuário se deseja continuar ou sair após cada operação
    if not continuar_ou_sair():
        limpar_terminal()
        print("TENHA UM LELÉU DIA! :)\n.\n.\n.\n.<3")
        break