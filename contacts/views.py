from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

class Window(QMainWindow):
    #  """MainWindow."""
    def __init__(self, parent=None):
        #  """"Intializer."""
        super().__init__(parent)
        self.setWindowTitle("Contacts")
        self.resize(550,250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.setupUI()
        
    def setupUI(self):
        # create the table view widget
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # create buttons
        self.addButton = QPushButton("Add...")
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")
        # lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.add.Widget(self.table)
        self.layout.addLayout(layout)
        