from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from controllers.drive_controller import check_google_drive_connection
from views.home_view import HomeView  # Importar la nueva vista

class AppSetup(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio - SAV")
        self.setGeometry(300, 300, 500, 400)

        self.setStyleSheet("""
            QWidget {
                background-color: #fffefe;
            }
            QLabel#titleLabel {
                font-size: 24px;
                font-weight: bold;
                color: #333333;
            }
            QPushButton {
                background-color: #018023;
                color: white;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005f99;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)

        # Logo (opcional, si tenés uno)
        try:
            pixmap = QPixmap("utils/virtualiza.PNG").scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo = QLabel()
            logo.setPixmap(pixmap)
            logo.setAlignment(Qt.AlignCenter)
            layout.addWidget(logo)
        except Exception:
            pass  # Si no hay imagen, no se rompe

        # Título
        self.label = QLabel("Bienvenido al Sistema Administrativo de Virtualiza")
        self.label.setObjectName("titleLabel")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Botón
        self.button = QPushButton("Iniciar aplicación")
        self.button.clicked.connect(self.on_click)
        layout.addWidget(self.button)

        # Mensaje dinámico
        self.status = QLabel("")
        self.status.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(layout)

    def on_click(self):
        try:
            # Verificar conexión a Google Drive
            connected = check_google_drive_connection()
            if connected:
                self.status.setText("✔️ Conexión a Google Drive establecida")
                QMessageBox.information(self, "Conexión exitosa", "¡Conexión a Google Drive establecida!")
                self.redirect_to_home()  # Redirigir a la nueva vista
            else:
                self.status.setText("⚠️ No se pudo conectar a Google Drive")
                QMessageBox.warning(self, "Conexión fallida", "No se pudo conectar a Google Drive.")
        except Exception as e:
            self.status.setText("❌ Error al conectar a Google Drive")
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {str(e)}")
            
    def redirect_to_home(self):
        # Redirigir a HomeView
        self.hide()  # Ocultar la ventana actual
        self.home_view = HomeView()
        self.home_view.show()
