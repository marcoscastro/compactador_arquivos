# coding: utf-8

# Módulo da interface
# Esse módulo tem como objetivo construir a interface gráfica do programa
# Autor: Marcos Castro

from Tkinter import * # funções Tkinter
from tkFileDialog import askopenfilename # função para escolher arquivo
from compactador import * # módulo compactador
import tkMessageBox # message box
from threading import Thread # importa módulo thread

class Aplicacao:

	def __init__(self, master):
		# cria um frame, será contêiner para armazenar os widgets
		self.frame = Frame(master) # master é instância Tk
		# pack é um gerenciador de geometria
		# gereciandor de geometria dá uma localização para o widget
		# se não colocar, ele vai existir, mas não ficará visível ao usuário
		self.frame.pack()

		# cria o botão adicionar
		# passa o parent, título, função associada ao evento e a borda
		self.botao_adicionar = Button(self.frame, text="Adicionar", command=self.adicionar, bd=3)
		self.botao_adicionar['font'] = ('Arial', 12) # adiciona uma fonte
		self.botao_adicionar.pack(pady=10, padx=30, side="left")

		# cria botão deletar, semelhante ao botão adicionar
		self.botao_deletar = Button(self.frame, text="Deletar", command=self.deletar, bd=3)
		self.botao_deletar['font'] = ('Arial', 12)
		self.botao_deletar.pack(padx=30, side="right")

		# cria outro frame
		self.frame2 = Frame(master)
		self.frame2.pack() 

		# cria scrollbar (barra de rolagem) vertical
		self.sby = Scrollbar(self.frame2)
		self.sby.pack(side=RIGHT, fill=Y)

		# cria scrollbar (barra de rolagem) horizontal
		self.sbx = Scrollbar(self.frame2, orient=HORIZONTAL)
		self.sbx.pack(side=BOTTOM, fill=X)

		# cria uma listbox
		self.listbox = Listbox(self.frame2, width=50, height=10, selectmode=EXTENDED)
		# selectmode=EXTENDED permite seleção de mais de um item
		self.listbox.pack()

		# anexa listbox para scrollbar vertical e horizontal
		self.listbox.config(yscrollcommand=self.sby.set)
		self.sby.config(command=self.listbox.yview)
		self.listbox.config(xscrollcommand=self.sbx.set)
		self.sbx.config(command=self.listbox.xview)

		# cria outro frame
		self.frame3 = Frame(master)
		self.frame3.pack() 

		# cria o botão compactar
		self.botao_compactar = Button(self.frame3, text="Compactar", command=self.compactar, bd=3)
		self.botao_compactar['font'] = ('Arial', 12)
		self.botao_compactar.pack(pady=10)

	# função associada ao evento do botão adicionar
	def adicionar(self):
		# abre janela para escolher arquivo
		nome_arquivo = askopenfilename()
		if nome_arquivo != "": # se escolheu algo
			self.listbox.insert(END, nome_arquivo)

	# função associada ao evento do botão deletar
	# essa função deleta os itens selecionados
	def deletar(self):
		items = self.listbox.curselection() # obtem lista de índices dos itens
		if len(items) == 0:
			tkMessageBox.showinfo("Compactador", "Selecione pelo menos um item!")
		else:
			pos = 0
			for i in items: # percorre a lista de indices
				item_pos = int(i) - pos # obtem a posição do item selecionado
				self.listbox.delete(item_pos, item_pos) # deleta um item selecionado
				pos = pos + 1 # incrementa pos

	# função associada ao evento do botão compactar
	def compactar(self):
		# pega todos os itens da listbox
		lista_arquivos = self.listbox.get(0, END)
		if len(lista_arquivos) == 0:
			tkMessageBox.showinfo("Compactador", "Adicione algum arquivo para compactar!")
			return # sai da função
		def executar():
			self.botao_compactar.configure(state=DISABLED) # desabilita o botão
			# se a lista não estiver vazia, compacta
			compactador = Compactador() # obtém instância de Compactador
			compactador.compactar(lista_arquivos) # compacta todos os arquivos
			self.botao_compactar.configure(state=NORMAL) # habilita o botão
		t = Thread(target=executar) # cria thread
		t.start() # inicia a thread


root = Tk() # obtém uma instância de Tk
root.title("Compactador de arquivos") # coloca um titulo na janela
root.iconbitmap(default="icone.ico") # coloca um icone
root.geometry('400x300') # ajusta o tamanho
root.resizable(width=FALSE, height=FALSE) # desabilita o redimensionamento da janela
Aplicacao(root) # passa instancia de Tk para classe Aplicacao
root.mainloop() # event loop da aplicação