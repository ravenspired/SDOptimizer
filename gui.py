# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("SDOptimizer 1.0 ")

		# setting geometry
		self.setGeometry(100, 100, 600, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# creating the check-box
		self.checkbox = QCheckBox('Exposure', self)


		self.startButton = QPushButton('Start', self)


		self.startButton.resize(100,32)
		self.startButton.move(50, 50)     

		# setting geometry of check box
		self.checkbox.setGeometry(200, 150, 100, 30)






		# self.startButton.clicked.connect(self.clickMethod)
		# connecting it to function
		self.checkbox.stateChanged.connect(self.method)

		# checking if it checked
		check = self.checkbox.isChecked()

		# printing the check
		print(check)

		def clickMethod(self):
			if self.checkBox.isChecked() == True:
				print('beginning processing.')
			else:
				print("was not checked so not processing.")

		def method(self):


		# printing the checked status
			print(self.checkbox.isChecked())




# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
