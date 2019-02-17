import sys
from PyQt5.QtWidgets import QDialog, QApplication,QTableWidget,QTableWidgetItem
from main import *
from admin import Admin
from PyQt5.QtCore import QObject, pyqtSlot

class AppWindow(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.show()
		self.admin = Admin(self.ui)

		self.ui.pushButton.clicked.connect(self.slot_method)

	@pyqtSlot()
	def slot_method(self):
		self.admin.showData()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = AppWindow()
	window.show()
	sys.exit(app.exec_())