
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)
from .model import ContactsModel

class Window(QMainWindow):
    """MainWindow."""
     
    def __init__(self, parent=None):
        """"Intializer."""
        super().__init__(parent)
        self.setWindowTitle("Contacts")
        self.resize(550,250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
                
        self.contactsModel = ContactsModel()
        self.setupUI()
        
        def setupUI(self):
              
            """Setup the main window's GUI."""
            # create the table view widget
            
            self.table = QTableView()
            self.table.setModel(self.contactsModel.model)
            self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.table.resizeColumnsToContents()
                # create buttons
            self.addButton = QPushButton("Add...")
            self.addButton.clicked.connect(self.openAddDialog)
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
            
        def openAddDialog(self):
            """Open the Add Contact Dialog."""
            dialog = AddDialog(self)
            if dialog.exec() == QDialog.Accepted:
                self.contactsModel.addContact(dialog.data)
                self.table.resizeColumnsToContents()
        
class AddDialog(QDialog):
        """Add Contact dialog."""
        
        def __init__(self, parent=None):
            """Intializer."""
            super().__init__(parent=parent)
            self.setWindowTitle("Add Contact")
            self.layout = QVBoxLayout()
            self.setLayout(self.layout)
            self.data = None
            
            self.setupUI()
            
        def setupUI(self):
            """Setup the add contact dialog's GUI."""
                # create line edits for data fields
            self.nameField = QLineEdit()
            self.nameField.setObjectName("Name")
            self.jobField = QLineEdit()
            self.jobField.setObjectName("Job")
            self.nameField = QLineEdit()
            self.nameField.setObjectName("Email")
                # lay out the data fields
            layout = QFormLayout()
            layout.addRow("Name:", self.nameField)
            layout.addRow("Job:", self.nameField)
            layout.addRow("Email:", self.nameField)
            self.layout.addLayout(layout)
                # add standard buttons to the dialog and connect them
            self.buttonsBox = QDialogButtonBox(self)
            self.buttonsBox.setOrientation(Qt.Horizontal)
            self.buttonsBox.setStandardButtons(
                    QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            )
            self.buttonsBox.accepted.connect(self.accept)
            self.buttonsBox.rejected.connect(self.reject)
            self.layout.addWidget(self.buttonsBox)
                
            def accept(self):
                """Accept the data provided through the dialog."""
                self.data = []
                for field in (self.nameField, self.jobField, self.emailField):
                    if not field.text():
                        QMessageBox.critical(
                            self,
                            "Error!",
                            f"You must provide a contact's {field.objectName()}",
                            
                        )
                        self.data = None 
                        return
                    
                    self.data.append(field.text())
                        
                if not self.data:
                    return
                    
                super().accept()