from datetime import date, datetime
import os
import pickle

try:
  arqClientes = open("clientes.dat", "rb")
  clientes = pickle.load(arqClientes)
  arqClientes.close()
except IOError:
  clientes={}
try:
  arqHistorico = open("historico.dat", "rb")
  historico = pickle.load(arqHistorico)
  arqHistorico.close()
except IOError:
  historico={}

def arqClientes(clientes):
    arqClientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arqClientes)
    arqClientes.close()
    return print("Operação realizada com sucesso!")

def arqHistorico(clientes):
    arqHistorico = open("historico.dat", "wb")
    pickle.dump(historico, arqHistorico)
    arqHistorico.close()
    return print()

regTransacao = []

def menuPrincipal():
  os.system('clear')
  print("=====================================")
  print("==== M E N U   P R I N C I P A L ====")
  print("=====================================")
  print()
  print("\t1 - Cadastro de Clientes")
  print("\t2 - Contas")
  print("\t3 - Transações")
  print("\t0 - Finalizar Programa")
  print()
  print("=====================================")
  print()
  opcao = input("Escolha sua opção: ")
  return opcao

def menuCliente():
  os.system('clear')
  print("=====================================")
  print("======== M E N U  C L I E N T E  ========")
  print("=====================================")
  print()
  print("\t1 - Cadastrar Cliente")
  print("\t2 - Pesquisar Cliente")
  print("\t3 - Editar Cliente")
  print("\t4 - Apagar Cliente")
  print("\t0 - Voltar ao Menu Principal")
  print()
  print("=====================================")
  print()
  opcao = input("Escolha sua opção: ")
  return opcao

def menuContas():
  os.system('clear')
  print("=====================================")
  print("==== M E N U   C O N T A S ====")
  print("=====================================")
  print()
  print("\t1 - Verificar Saldo: ")
  print("\t2 - Realizar Saque: ")
  print("\t3 - Realizar Deposito: ")
  print("\t0 - Voltar ao Menu Principal")
  print()
  print("=====================================")
  print()
  opcao = input("Escolha sua opção: ")
  return opcao


def menuTransação():
  os.system('clear')
  print("=====================================")
  print("==== M E N U   T R A N S A Ç Ã O ====")
  print("=====================================")
  print()
  print("\t1 - Transferência" ) 
  print("\t2 - Historico de transferências")
  print("\t0 - Voltar ao Menu Principal")
  print()
  print("=====================================")
  print()
  opcao = input("Escolha sua opção: ")
  return opcao


def cadastrarCliente():
  print()
  print("Favor informar do dados abaixo:")
  nome = input("Nome: ")
  cpf = input("CPF: ")
  if cpf not in clientes:    
    if len(cpf) != 11:
      testeCPF = True
      while testeCPF:
        cpf = input('Digite um CPF com 11 digitos valido: ')
        if len(cpf) == 11:
          testeCPF = False 
    numero = input("Informe o numero da conta: ")
    agencia = input("Informe a agência: ")
    operacao = input("Informe a operação: ")
    saldo = 0  
    clientes[cpf] = [nome, numero, agencia, operacao, saldo]
    arqClientes(clientes)
  else:
    print('Cliente já cadastrado!')
  input("Tecle ENTER para continuar!")

def pesquisarCliente():
  print()
  cpf = input("Favor informar o CPF: ")
  if len(cpf) != 11:
    testeCPF = True
    while testeCPF:
      cpf = input('Digite um CPF com 11 digitos valido: ')
      if len(cpf) == 11:
        testeCPF = False 
  if cpf in clientes:
    print("Nome: ", clientes[cpf][0])
    print("CPF: ", cpf)
    print("Número da conta: ", clientes[cpf][1])
    print("Número da agência: ", clientes[cpf][2])
    print("Número da operação: ", clientes[cpf][3])
  else:
    print('Cliente não cadastrado!')
  input("Tecle ENTER para continuar!") 

def verificarSaldo(clientes):
  cpf = input('Favor informar o CPF: ')
  if len(cpf) != 11:
    testeCPF = True
    while testeCPF:
      cpf = input('Digite um CPF com 11 digitos valido: ')
      if len(cpf) == 11:
        testeCPF = False 
  if cpf in clientes:
    print('Seu saldo é: ',clientes[cpf][4])
  input("\nTecle ENTER para continuar!")

def realizarSaque(clientes):
  cpf = input('Favor informar o CPF: ')
  if len(cpf) != 11:
    testeCPF = True
    while testeCPF:
      cpf = input('Digite um CPF com 11 digitos valido: ')
      if len(cpf) == 11:
        testeCPF = False 
  saque = int(input("Que valor deseja sacar? "))    
  total = valor    


def realizarDeposito(clientes):
  cpf = input('Digite o CPF: ')
  if len(cpf) != 11:
    testeCPF = True
    while testeCPF:
      cpf = input('Digite um CPF com 11 digitos valido: ')
      if len(cpf) == 11:
        testeCPF = False 
  valor = float(input('Valor do deposito? '))
  valor = float(valor)
  clientes[cpf][4]+=valor
  arqClientes(clientes)

def historicoTransacoes(clientes):
  cpfR = input('Digite seu CPF: ')
  if cpfR in clientes:
    for cpf in clientes:
      if cpf == cpfR:
        os.system('clear')
        print('Seu CPF: ',cpfR)
        print('Conta Favorecida: ', historico[cpfR][0])
        print('Valor: ',historico[cpfR][1])
        print('Data: ', historico[cpfR][2],'Hora: ',historico[cpfR][3])
  else:
    print('Cliente não encontrado! ')



def transferencia(clientes):
  contaEmissor = input('Digite a seu CPF: ')
  if contaEmissor not in clientes:
    print('Conta não encontrada! ')
  else:
    print("=====================================")
    print("==== T R A N S F E R Ê N C I A S ====")
    print("=====================================")
    print()
    print()
    contaRecebe = input('Digite o numero da conta destino: ')
    if contaRecebe not in clientes:
      testeConta = True
      while testeConta:
        contaRecebe = input('Digite o numero do CPF destino: ')
        if testeConta in clientes:
          testeConta = False
        else:
          opcao = input('Deseja continuar? Sim ou Não')
          if opcao.upper() == 'NAO' or opcao.upper() == 'NÃO':
            testeConta = False
          else:
            pass
    else:
      print('O cliente é:',clientes[contaRecebe][0],'?')
      opcao = input('Digite SIM ou NÃO: ')
      if opcao.upper() == 'SIM':
        print('Seu saldo atual é',clientes[contaEmissor][4] )
        valor = float(input('\nValor: '))
        clientes[contaRecebe][4] += valor
        clientes[contaEmissor][4] -= valor
        arqClientes(clientes)
        dia_transferencia = date.today()
        dia_transferencia = dia_transferencia.strftime('%d-%m-%Y')
        hora_transferencia = datetime.today()
        hora_transferencia = hora_transferencia.strftime('%H:%M')
        historico[contaEmissor] = [contaRecebe,valor,dia_transferencia,hora_transferencia]
        arqHistorico(clientes)
      else:
        input('\nDigite enter para sair ')



 

op1 = menuPrincipal()
while op1 != "0":
  if op1 == "1":
    op2 = menuCliente()
    while op2 != "0":
      if op2 == "1":
        cadastrarCliente()
      elif op2 == "2":
        pesquisarCliente()
      elif op2 == "3":
        print("menu editar cliente")
      elif op2 == "4":
        print("menu apagar cliente")
      op2 = menuCliente()
  elif op1 == "2":
    op2 = menuContas()
    while op2 != "0":
      if op2 == "1":
        verificarSaldo(clientes)
      elif op2 == "2":
        realizarSaque(clientes)
      elif op2 == "3":
        realizarDeposito(clientes)
      elif op2 == "4":
        print("menu apagar cliente")
      input("Tecle ENTER para continuar")
      op2 = menuCliente()
  elif op1 == "3":
    op2 = menuTransação()
    while op2 != "0":
      if op2 == "1":
        transferencia(clientes)
      elif op2 == '2':
        historicoTransacoes(clientes)       
      input("Tecle ENTER para continuar")
      op2 = menuContas()
  elif op1 == "4":
    op2 = menuTransação()
    while op2 != "0":
      if op2 == "1":
        print("menu cadastrar cliente")
      elif op2 == "2":
        print("menu pesquisar cliente")
      elif op2 == "3":
        print("menu editar cliente")
      elif op2 == "4":
        print("menu apagar cliente")
      input("Tecle ENTER para continuar")
      op2 = menuTransação()
  op1 = menuPrincipal()
print("Fim")