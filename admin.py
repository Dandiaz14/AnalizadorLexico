from PyQt5.QtWidgets import QDialog, QApplication,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import QObject, pyqtSlot
import ply.lex as lex
import re

class Admin():
	def __init__(self,ui):
		self.ui = ui
		self.identificador = re.compile(r'^([_]?[a-z|A-Z|0-9]*)$')
		self.entero = re.compile(r'^([+-]?\d+)$')
		self.flotante = re.compile(r'^([+-]?([0-9]*)[.][0-9]+)$')
		self.relacional = re.compile(r'^(<|>|>=|<=|!=|==)$')
		self.token = re.compile(r'^(\(|\)|{|}|;|\+|\*|-|/|=)$')
		self.rows = 0
		self.columns = 0
		self.reservado = ['if','IF','while','While','return','RETURN']
		self.tipo = ['float','void','int','char','FLOAT','VOID','INT','CHAR']

	def showData(self):
		lines = self.ui.textEdit.toPlainText().split()
		self.ui.tableWidget.setRowCount(len(lines))
		self.ui.tableWidget.setColumnCount(2)
		pattern = re.compile(r"[ ,\t\n]")
		for line in lines:
			if line in self.reservado:
				self.isReserved(line)
			elif line in self.tipo:
				self.isTypeOfData(line)
			elif self.flotante.match(line):
				self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(line))
				self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Flotante"))
				self.rows += 1
			elif self.entero.match(line):
				self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(line))
				self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Entero"))
				self.rows += 1
			elif self.identificador.match(line):
				self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(line))
				self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("identificador"))
				self.rows += 1
			elif self.relacional.match(line):
				self.isRelational(line)
			elif self.token.match(line):
				self.isToken(line)
			else:
				self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(line))
				self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Error"))
				self.rows += 1

	def isTypeOfData(self,tok):
		if tok.upper() == 'INT':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Tipo de Dato"))
			self.rows += 1
		elif tok.upper() == 'VOID':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Tipo de Dato"))
			self.rows += 1
		elif tok.upper() == 'FLOAT':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Tipo de Dato"))
			self.rows += 1
		elif tok.upper() == 'CHAR':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Tipo de Dato"))
			self.rows += 1

	def isReserved(self,tok):
		if tok.upper() == 'IF':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Palabra Reservada"))
			self.rows += 1
		elif tok.upper() == 'WHILE':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Palabra Reservada"))
			self.rows += 1
		elif tok.upper() == 'RETURN':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Palabra Reservada"))
			self.rows += 1
		else:
			pass

	def isToken(self,tok):
		if tok == r'=':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Asignación"))
			self.rows += 1
		elif tok == r'(':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Parentesis Izq"))
			self.rows += 1
		elif tok == r')':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Parentesis Der"))
			self.rows += 1
		elif tok == r'{':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Llave Inicio"))
			self.rows += 1
		elif tok == r'}':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Llave Cierre"))
			self.rows += 1
		elif tok == r';':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Punto y Coma"))
			self.rows += 1
		elif tok == r'+':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Operador Suma"))
			self.rows += 1
		elif tok == r'-':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Operador Resta"))
			self.rows += 1
		elif tok == r'*':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Operador Multiplicación"))
			self.rows += 1
		elif tok == r'/':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Operador División"))
			self.rows += 1

	def isRelational(self,tok):
		if tok == r'<':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Operador Relacional"))
			self.rows += 1
		elif tok == r'>':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Operador Relacional"))
			self.rows += 1
		elif tok == r'<=':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Operador Relacional"))
			self.rows += 1
		elif tok == r'>=':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Operador Relacional"))
			self.rows += 1
		elif tok == r'!=':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Operador Relacional"))
			self.rows += 1
		elif tok == r'==':
			self.ui.tableWidget.setItem(self.rows,self.columns,QTableWidgetItem(tok))
			self.ui.tableWidget.setItem(self.rows,self.columns+1,QTableWidgetItem("Operador Relacional"))
			self.rows += 1
