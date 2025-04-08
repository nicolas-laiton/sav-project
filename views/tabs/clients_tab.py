from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLabel, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
import pandas as pd

class ClientsTab(QWidget):
    def __init__(self, drive_service, file_id, output_path):
        super().__init__()
        self.drive_service = drive_service
        self.file_id = file_id
        self.output_path = output_path
        self.data = None  # Almacenar los datos del archivo Excel

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Menú desplegable para seleccionar Apartamento
        self.apartment_dropdown = QComboBox()
        self.apartment_dropdown.addItem("Seleccione un Apartamento")  # Opción por defecto
        self.apartment_dropdown.currentIndexChanged.connect(self.on_apartment_selected)
        layout.addWidget(self.apartment_dropdown)

        # Etiqueta para mostrar resultados
        self.results_label = QLabel("Resultados:")
        layout.addWidget(self.results_label)

        # Tabla para mostrar datos
        self.results_table = QTableWidget()
        self.results_table.setSizePolicy(
            self.results_table.sizePolicy().Expanding, 
            self.results_table.sizePolicy().Expanding
        )
        layout.addWidget(self.results_table)

        self.setLayout(layout)

        # Establecer un tamaño inicial razonable
        self.setMinimumSize(800, 600)

        # Descargar y cargar los datos al iniciar
        self.load_clients_data()

    def load_clients_data(self):
        """Descargar y cargar los datos del archivo Excel."""
        try:
            # Descargar el archivo de Drive
            from controllers.drive_controller import download_file_from_drive
            download_file_from_drive(self.drive_service, self.file_id, self.output_path)

            # Leer los datos del archivo Excel
            self.data = pd.read_excel(self.output_path)

            # Poblar el menú desplegable con valores únicos de la columna A
            if not self.data.empty:
                unique_apartments = self.data.iloc[:, 0].dropna().unique()  # Suponiendo que la columna A es la primera
                self.apartment_dropdown.addItems(sorted(map(str, unique_apartments)))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar los datos de clientes: {e}")

    def on_apartment_selected(self, index):
            """Mostrar datos del apartamento seleccionado."""
            try:
                if index == 0:  # Si selecciona la opción por defecto
                    self.results_table.clear()
                    self.results_label.setText("Resultados:")
                    return

                if self.data is None:
                    raise Exception("Los datos no han sido cargados correctamente.")

                # Obtener el apartamento seleccionado
                apartment_code = self.apartment_dropdown.currentText()

                # Filtrar datos
                filtered_data = self.data[self.data.iloc[:, 0] == apartment_code]

                if filtered_data.empty:
                    self.results_table.clear()
                    self.results_label.setText(f"No se encontraron datos para el Apartamento: {apartment_code}")
                    return

                # Limitar los datos entre columnas B (índice 1) y AB (índice 27)
                limited_data = filtered_data.iloc[:, 1:28]  # Índices ajustados para pandas (1 = B, 27 = AB inclusive)

                # Mostrar resultados como tabla vertical
                self.results_table.setRowCount(len(limited_data.columns))
                self.results_table.setColumnCount(2)
                self.results_table.setHorizontalHeaderLabels(["Campo", "Valor"])

                for row_idx, (col_name, value) in enumerate(zip(limited_data.columns, limited_data.iloc[0])):
                    self.results_table.setItem(row_idx, 0, QTableWidgetItem(str(col_name)))
                    self.results_table.setItem(row_idx, 1, QTableWidgetItem(str(value)))

                self.results_label.setText(f"Mostrando datos para Apartamento: {apartment_code}")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al mostrar los datos: {e}")
