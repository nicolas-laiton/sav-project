from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget, QLabel
from controllers.drive_controller import get_drive_service
from views.tabs.clients_tab import ClientsTab


class HomeView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SAV - Sistema Administrativo")
        
        # Configurar servicio de Google Drive
        self.drive_service = get_drive_service()
        self.file_id = "1TyPAcHsgqsEgw7YGwHSwkzVC_uGAy3VSGEzPguKmjMk"  # ID del archivo
        self.output_path = "utils/clientes.xlsx"

        layout = QVBoxLayout()

        # Crear widget de pestañas
        tab_widget = QTabWidget()

        # Agregar pestaña "Clientes"
        clients_tab = ClientsTab(self.drive_service, self.file_id, self.output_path)
        tab_widget.addTab(clients_tab, "Clientes")

        # Otras pestañas (ejemplo)
        tab_widget.addTab(self.create_tab("Propiedades"), "Propiedades")
        tab_widget.addTab(self.create_tab("Reportes"), "Reportes")

        layout.addWidget(tab_widget)
        self.setLayout(layout)

    def create_tab(self, name):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Contenido de {name}"))
        tab.setLayout(layout)
        return tab
