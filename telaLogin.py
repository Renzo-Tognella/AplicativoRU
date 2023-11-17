from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QFrame, QGridLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")

        layout = QGridLayout()

        # RA
        self.label_ra = QLabel("RA")
        self.text_ra = QLineEdit()
        self.label_ra.setStyleSheet('font-size: 20px')
        self.text_ra.setStyleSheet('background-color: lightgrey; border: 2px solid grey; border-radius: 20px; font-size: 20px')
        layout.addWidget(self.label_ra, 0, 0)
        layout.addWidget(self.text_ra, 0, 1)

        self.label_senha = QLabel("Senha")
        self.text_senha = QLineEdit()
        self.label_senha.setStyleSheet('font-size: 20px')
        self.text_senha.setEchoMode(QLineEdit.Password)
        self.text_senha.setStyleSheet('background-color: lightgrey; border: 2px solid grey; border-radius: 20px; font-size: 20px')
        layout.addWidget(self.label_senha, 2, 0, alignment=Qt.AlignBottom)
        layout.addWidget(self.text_senha, 2, 1, alignment=Qt.AlignBottom)

        self.button = QPushButton("Entrar")
        self.button.setStyleSheet('background-color: #D9B7F4; border: 2px solid grey; border-radius: 70px; font-size: 20px')
        layout.addWidget(self.button, 4, 0, 1, 2, alignment=Qt.AlignBottom)


        self.hint = QLabel("Dica: Use a seu registro acadêmico e a senha do Portal do Aluno")
        self.hint.setStyleSheet('font-size: 15px')
        layout.addWidget(self.hint, 6, 0, 1, 2, alignment=Qt.AlignBottom)

        self.frame = QFrame()
        self.frame.setLayout(layout)
        self.frame.setStyleSheet("background-color: #FFF059; border-radius: 20px;")

        window_layout = QGridLayout()
        window_layout.addWidget(self.frame, 1, 1, 2, 2, alignment=Qt.AlignCenter)

        container = QWidget()
        container.setLayout(window_layout)
        self.setCentralWidget(container)

        self.setStyleSheet("background-color: #F8EDED;")

    def resizeEvent(self, event):

        super().resizeEvent(event)
        frame_width = self.width() * 0.2
        frame_height = self.height() * 0.3
        frame_x = (self.width() - frame_width) / 2
        frame_y = (self.height() - frame_height) / 2
        self.frame.setGeometry(frame_x, frame_y, frame_width, frame_height)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
