import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QFont

import objekti as obj

class MainWindow(QMainWindow):
	
	def __init__(self):
		super(MainWindow, self).__init__()

		self.setWindowTitle("Nihanja - laboratorijska vaja")
		
		self.lf = obj.LastnaFrekvenca()
		self.lf.setParent(self)
		self.lf.setMinimumWidth(1200)
		
		logo = QLabel()
		pixmap = QPixmap("/home/ladisk/Desktop/test/jacopo/ladisk_logo.png")
		logo.setPixmap(pixmap)
		
		font = QFont()
		font.setPointSize(16)
		
		vpisna_stevilka = QLineEdit()
		vpisna_stevilka.setFixedSize(500, 50)
		vpisna_stevilka.setFont(font)
		vpisna_stevilka.setMaxLength(8)
		vpisna_stevilka.setPlaceholderText("vpisna stevilka")
		
		mail = QLineEdit()
		mail.setFixedSize(500, 50)
		mail.setFont(font)
		mail.setPlaceholderText("e-mail naslov")
		
		self.navodilo = QLabel("\n\n")
		self.navodilo.setFixedSize(500, 50)
		self.navodilo.setFont(font)
		
		layout = QHBoxLayout()
		desni_layout = QVBoxLayout()
		
		desni_layout.setSpacing(5)
		desni_layout.setContentsMargins(100, 200, 100, 200)
		desni_layout.addWidget(logo)
		desni_layout.addWidget(vpisna_stevilka)
		desni_layout.addWidget(mail)
		desni_layout.addWidget(self.navodilo)

		desni_widget = QWidget()
		desni_widget.setLayout(desni_layout)

		layout.addWidget(self.lf)
		layout.addWidget(desni_widget)
		
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
		
		self.showFullScreen()
		
		self.timer = QTimer()
		self.timer.timeout.connect(self.check_n)
		self.timer.start(1000)
	
	def udarite(self):
		self.navodilo.setText("\n\t      udarite X s kladivom")
	
	def check_n(self):
		if self.lf.n == True:
			self.timer.stop()
			info_lf = [self.lf.a, self.lf.ts, self.lf.tk]
			self.graf = obj.Graf(info_lf)
			self.motor = obj.Motor()
			lay2 = QHBoxLayout()
			lay2.addWidget(self.graf)
			lay2.addWidget(self.motor)
			widg2 = QWidget()
			widg2.setLayout(lay2)
			self.setCentralWidget(widg2)
			self.motor_worker = obj.MotorWorker(self.motor, lf = self.graf.lfrpm, delta = self.graf.delta)
			self.motor_worker.start()
		else:
			pass
	
	def keyPressEvent(self, event):
		if event.key() == Qt.Key.Key_Return:
			self.udarite()
		if event.key() == Qt.Key.Key_Escape:
			self.close()

def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()

if __name__ == '__main__':
    main()
