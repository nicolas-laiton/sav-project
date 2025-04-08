import sys
from PyQt5.QtWidgets import QApplication
from views.setup_view import AppSetup

def main():
    app = QApplication(sys.argv)      # Inicializa la app
    ventana = AppSetup()              # Crea la vista inicial
    ventana.show()                    # Muestra la ventana
    sys.exit(app.exec_())             # Mantiene la app viva hasta que se cierre

if __name__ == '__main__':
    main()
