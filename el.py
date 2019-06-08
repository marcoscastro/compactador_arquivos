# coding: utf-8
# Compactador de Arquivos El
# Módulo compactador
# Esse módulo tem como objetivo compactor arquivos no formato ZIP
# Autor: Marcos Castro

import zipfile # módulo que contém funções para criar arquivp ZIP
import os.path # módulo para caminhos

class Compactador:
	# método para compactar arquivos
	# recebe uma lista de caminhos de arquivos a serem compactados
	# é um padrão chamar o primeiro parâmetro de 'self'
	# o nome 'self' é reconhecido como o nome do objeto a ser invocado no método
	# 'self' é semelhante ao 'this' do Java
	def compactar(self, lista_arquivos):
		# abre o arquivo para escrita para escrita
		# primeiro parâmetro é o nome do arquivo ZIP
		# segundo parâmetro é o modo de abertura, 'w' é para escrita
		arquivo_zip = zipfile.ZipFile("arquivo.zip", "w")
		# percorre a lista
		for arquivo in lista_arquivos:
			# testa se é arquivo e se o arquivo existe
			if(os.path.isfile(arquivo) and os.path.exists(arquivo)):
				# pega o nome do arquivo base, sem o diretório
				base = os.path.basename(arquivo)
				# passa o diretório e o nome do arquivo a ser gravado
				arquivo_zip.write(arquivo, base)
		arquivo_zip.close() # fecha o arquivo


# teste
#compactador = Compactador()
#lista = ['C:/Users/Marcos/Desktop/Tkinter - PUG-PI/Compactador de arquivos/compactador.py']
#lista.append('C:/Users/Marcos/Desktop/main.cpp')
#lista.append('projeto.exe')
#lista.append('C:\Users\Marcos\Desktop\Tkinter - PUG-PI')
#compactador.compactar(lista)

