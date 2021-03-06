# main_telas.py

# Convertemos as interfaces desenvolvidas no programa QtDesign em códigos python;
# remover a classe endereco

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

from cliente import Cliente
from funcionario import Funcionario
from historico import Historico
from pessoa import Pessoa
from produto import Produto
from registros import Registros
from venda import Venda

from tela_login import Tela_login
from tela_inicial import Tela_inicial
# Menus
from tela_funcionarios_menu import Tela_funcionarios_menu
from tela_produtos_menu import Tela_produtos_menu
from tela_clientes_menu import Tela_clientes_menu

# Opcoes Funcionarios
from tela_cadastro_funcionario import Tela_cadastro_funcionario

# Opcoes Produtos
from tela_cadastro_produto import Tela_cadastro_produto
from tela_apagar_produto import Tela_apagar_produto

# Opcoes Clientes:
from tela_cadastro_cliente import Tela_cadastro_cliente
from tela_apagar_cliente import Tela_apagar_cliente
from tela_editar_cliente import Tela_editar_cliente

nome_auto = "Matheus"
cpf_auto = "123"
email_auto = "123"
tel_auto = "123"
senha_auto = "123"
confirmSENHA_auto = "123"

class Ui_Main(QtWidgets.QWidget):
    
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640,480) # definição do tamanho da tela

        # Criação das pilhas de interfaces.
        self.QtStack = QtWidgets.QStackedLayout() 
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()

        # Criação do objeto para cada tela
        self.tela_login = Tela_login()
        self.tela_login.setupUi(self.stack0)

        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack1)

        self.tela_cadastro_funcionario  = Tela_cadastro_funcionario()
        self.tela_cadastro_funcionario.setupUi(self.stack2)

        self.tela_produtos_menu = Tela_produtos_menu()
        self.tela_produtos_menu.setupUi(self.stack3)

        self.tela_cadastro_produto = Tela_cadastro_produto()
        self.tela_cadastro_produto.setupUi(self.stack4)

        self.tela_apagar_produto = Tela_apagar_produto()
        self.tela_apagar_produto.setupUi(self.stack5)

        self.tela_clientes_menu = Tela_clientes_menu()
        self.tela_clientes_menu.setupUi(self.stack6)

        self.tela_cadastro_cliente = Tela_cadastro_cliente()
        self.tela_cadastro_cliente.setupUi(self.stack7)

        self.tela_apagar_cliente = Tela_apagar_cliente()
        self.tela_apagar_cliente.setupUi(self.stack8)

        self.tela_editar_cliente = Tela_editar_cliente()
        self.tela_editar_cliente.setupUi(self.stack9)

        #
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)



class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cadastros = Registros()
        self.logado = Funcionario('','')
        self.cliente_aux = Cliente('')

        self.cadastros.cadastraFUNC(nome_auto, cpf_auto, email_auto, tel_auto, senha_auto, confirmSENHA_auto)
        

        # Configuação dos botões de cada tela:
        # Funções dos botões da tela:

        # botões de voltar:
        self.tela_inicial.pushButton_SAIR.clicked.connect(self.botaoSAIR)
        self.tela_cadastro_funcionario.voltar.clicked.connect(self.abrir_tela_login)
        self.tela_produtos_menu.voltar.clicked.connect(self.abrir_tela_inicial)  # <----- PRODUTO
        self.tela_cadastro_produto.voltar.clicked.connect(self.abrir_tela_produtos_menu)
        self.tela_apagar_produto.voltar.clicked.connect(self.abrir_tela_produtos_menu)
        self.tela_clientes_menu.voltar.clicked.connect(self.abrir_tela_inicial)  # <----- CLIENTES
        self.tela_cadastro_cliente.voltar.clicked.connect(self.abrir_tela_clientes_menu)
        self.tela_apagar_cliente.voltar.clicked.connect(self.abrir_tela_clientes_menu)
        self.tela_editar_cliente.voltar.clicked.connect(self.abrir_tela_clientes_menu)

        # Tela de Login:
        self.tela_login.pushButton.clicked.connect(self.botaoENTRAR)
        self.tela_login.pushButton_2.clicked.connect(self.abrir_tela_cadastro_pessoa)

        # Tela de cadastro de Funcionário:
        self.tela_cadastro_funcionario.cadastrar.clicked.connect(self.cadastrar_novo_FUNC)

        # Tela inicial:
        #self.tela_inicial.pushButton.clicked.connect()   # Vendas
        self.tela_inicial.pushButton_2.clicked.connect(self.abrir_tela_clientes_menu) # Clientes
        self.tela_inicial.pushButton_3.clicked.connect(self.abrir_tela_produtos_menu) # Produtos
        
        # Tela PRODUTOS menu:
        self.tela_produtos_menu.pushButton.clicked.connect(self.abrir_tela_cadastro_produto) # cadastrar um novo produto
        self.tela_produtos_menu.pushButton_2.clicked.connect(self.abrir_tela_apagar_produto) # apagar um produto
        # Tela de cadastro de Produto:
        self.tela_cadastro_produto.cadastrar.clicked.connect(self.cadastrar_novo_PROD)
        # Tela de apagar um produto:
        self.tela_apagar_produto.apagar.clicked.connect(self.apagar_PROD)

        # Tela CLIENTES menu:
        self.tela_clientes_menu.pushButton.clicked.connect(self.abrir_tela_cadastro_cliente) # cadastrar um novo cliente.
        self.tela_clientes_menu.pushButton_2.clicked.connect(self.abrir_tela_apagar_cliente) # apagar registro de um cliente.
        self.tela_clientes_menu.pushButton_3.clicked.connect(self.abrir_tela_editar_cliente) # editar registro de um cliente.
        # Tela cadastro Clientes
        self.tela_cadastro_cliente.cadastrar.clicked.connect(self.cadastrar_novo_CLIENTE)
        # Tela apagar Clientes
        self.tela_apagar_cliente.apagar.clicked.connect(self.apagar_um_CLIENTE)
        # Tela editar Clientes
        self.tela_editar_cliente.buscar.clicked.connect(self.buscar_um_CLIENTE)
        self.tela_editar_cliente.editar.clicked.connect(self.botao_editar_CLIENTE)

    def botaoSAIR(self):
        self.usuario_logado = None
        self.usuario_logado = Funcionario('','')
        self.tela_login.lineEdit.setText("")
        self.tela_login.lineEdit_2.setText("")
        self.QtStack.setCurrentIndex(0)

    def abrir_tela_login(self):
        self.QtStack.setCurrentIndex(0)

    def abrir_tela_inicial(self):
        self.QtStack.setCurrentIndex(1)

    def abrir_tela_cadastro_pessoa(self):
        self.QtStack.setCurrentIndex(2)

    def abrir_tela_produtos_menu(self):
        self.QtStack.setCurrentIndex(3)

    def abrir_tela_cadastro_produto(self):
        self.QtStack.setCurrentIndex(4)

    def abrir_tela_apagar_produto(self):
        self.QtStack.setCurrentIndex(5)

    def abrir_tela_clientes_menu(self):
        self.QtStack.setCurrentIndex(6)

    def abrir_tela_cadastro_cliente(self):
        self.QtStack.setCurrentIndex(7)

    def abrir_tela_apagar_cliente(self):
        self.QtStack.setCurrentIndex(8)

    def abrir_tela_editar_cliente(self):
        self.QtStack.setCurrentIndex(9)

    def botaoENTRAR(self):
        cpf = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        usuario = self.cadastros.fazerLOGIN(cpf, senha)
        if usuario[0] != None:
            self.logado = usuario[0]
            self.tela_inicial.label_bem_vindo.setText(f"Bem vindo, {usuario[0].nome}!")
            self.QtStack.setCurrentIndex(1)
        QMessageBox.information(None,'POOII',f'{usuario[1]}')
        self.tela_login.lineEdit.setText("")
        self.tela_login.lineEdit_2.setText("")
        
    def cadastrar_novo_FUNC(self):
        nome = self.tela_cadastro_funcionario.lineEdit.text()
        cpf = self.tela_cadastro_funcionario.lineEdit_2.text()
        email = self.tela_cadastro_funcionario.lineEdit_3.text()
        tel = self.tela_cadastro_funcionario.lineEdit_4.text()
        senha = self.tela_cadastro_funcionario.lineEdit_6.text()
        confirmSENHA = self.tela_cadastro_funcionario.lineEdit_7.text()
        
        mensagem = self.cadastros.cadastraFUNC(nome, cpf, email, tel, senha, confirmSENHA)
        QMessageBox.information(None,'SILE',f'{mensagem}')
        self.QtStack.setCurrentIndex(0)

        self.tela_cadastro_funcionario.lineEdit.setText('')
        self.tela_cadastro_funcionario.lineEdit_2.setText('')
        self.tela_cadastro_funcionario.lineEdit_3.setText('')
        self.tela_cadastro_funcionario.lineEdit_4.setText('')
        self.tela_cadastro_funcionario.lineEdit_6.setText('')
        self.tela_cadastro_funcionario.lineEdit_7.setText('')

    def cadastrar_novo_PROD(self):
        codigo = self.tela_cadastro_produto.lineEdit_4.text()
        nome = self.tela_cadastro_produto.lineEdit.text()
        preco = self.tela_cadastro_produto.lineEdit_2.text()
        qnt = self.tela_cadastro_produto.lineEdit_3.text()
        
        mensagem = self.cadastros.cadastraPROD(codigo, nome, preco, qnt)
        QMessageBox.information(None,'POOII',f'{mensagem}')
        
        self.tela_cadastro_produto.lineEdit.setText('')
        self.tela_cadastro_produto.lineEdit_2.setText('')
        self.tela_cadastro_produto.lineEdit_3.setText('')
        self.tela_cadastro_produto.lineEdit_4.setText('')

    def apagar_PROD(self):
        codigo = self.tela_apagar_produto.lineEdit.text()
        mensagem = self.cadastros.apagaPROD(codigo)
        QMessageBox.information(None,'POOII',f'{mensagem}')
        self.tela_apagar_produto.lineEdit.setText('')

    def cadastrar_novo_CLIENTE(self):
        nome = self.tela_cadastro_cliente.lineEdit.text()
        cpf = self.tela_cadastro_cliente.lineEdit_2.text()
        email = self.tela_cadastro_cliente.lineEdit_3.text()
        tel = self.tela_cadastro_cliente.lineEdit_4.text()

        mensagem = self.cadastros.cadastraCLIENTE(nome, cpf, email, tel)
        QMessageBox.information(None,'SILE',f'{mensagem}')

        self.tela_cadastro_cliente.lineEdit.setText('')
        self.tela_cadastro_cliente.lineEdit_2.setText('')
        self.tela_cadastro_cliente.lineEdit_3.setText('')
        self.tela_cadastro_cliente.lineEdit_4.setText('')

    def apagar_um_CLIENTE(self):
        cpf = self.tela_apagar_cliente.lineEdit.text()
        mensagem = self.cadastros.apagaCLIENTE(cpf)
        QMessageBox.information(None,'SILE',f'{mensagem}')
        self.tela_apagar_cliente.lineEdit.setText('')

    def buscar_um_CLIENTE(self):
        cpf = self.tela_editar_cliente.lineEdit_BUSCAR.text()
        retorno = self.cadastros.editaCLIENTE_busca(cpf)
        QMessageBox.information(None,'SILE',f'{retorno[1]}')
        if retorno[0] != None:
            # Não foi encontrado.
            self.tela_editar_cliente.lineEdit.setText(f"{retorno[0].nome}")
            self.tela_editar_cliente.lineEdit_2.setText(f"{retorno[0].cpf}")
            self.tela_editar_cliente.lineEdit_3.setText(f"{retorno[0].email}")
            self.tela_editar_cliente.lineEdit_4.setText(f"{retorno[0].telefone}")
            self.cliente_aux = retorno[0]
        else:
            self.cliente_aux = None
        self.tela_editar_cliente.lineEdit_BUSCAR.setText('')

    def botao_editar_CLIENTE(self):
        nome = self.tela_editar_cliente.lineEdit.text()
        cpf = self.tela_editar_cliente.lineEdit_2.text()
        email = self.tela_editar_cliente.lineEdit_3.text()
        tel = self.tela_editar_cliente.lineEdit_4.text()

        if self.cliente_aux != None:
            mensagem = self.cliente_aux.editar(nome, cpf, email, tel)
            QMessageBox.information(None,'SILE',f'{mensagem}')

        self.tela_editar_cliente.lineEdit.setText('')
        self.tela_editar_cliente.lineEdit_2.setText('')
        self.tela_editar_cliente.lineEdit_3.setText('')
        self.tela_editar_cliente.lineEdit_4.setText('')
        self.tela_editar_cliente.lineEdit_BUSCAR.setText('')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

print("tudo certo! ")