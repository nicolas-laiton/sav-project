from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class HomeView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio - SAV")
        self.setGeometry(300, 300, 600, 400)

        # Configuración de estilo
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #333333;
            }
        """)

        # Layout y elementos
        layout = QVBoxLayout()
        label = QLabel("¡Bienvenido a la aplicación!")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)
