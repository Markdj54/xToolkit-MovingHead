from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QFileDialog,
    QListWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QSplitter,
    QToolBar,
    QMessageBox
)

from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

from core.xml_reader import XMLReader


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.reader = XMLReader()

        self.setWindowTitle("xToolkit v0.1 Alpha")

        self.resize(1200, 700)

        self.create_toolbar()

        self.create_ui()

        self.statusBar().showMessage("Ready")

    # -------------------------------------------------

    def create_toolbar(self):

        toolbar = QToolBar()

        self.addToolBar(toolbar)

        open_action = QAction("Open XML", self)

        open_action.triggered.connect(self.open_xml)

        toolbar.addAction(open_action)

    # -------------------------------------------------

    def create_ui(self):

        splitter = QSplitter(Qt.Horizontal)

        self.model_list = QListWidget()

        self.property_table = QTableWidget()

        self.property_table.setColumnCount(2)

        self.property_table.setHorizontalHeaderLabels(
            ["Property", "Value"]
        )

        splitter.addWidget(self.model_list)

        splitter.addWidget(self.property_table)

        splitter.setSizes([300, 900])

        self.setCentralWidget(splitter)

        self.model_list.currentTextChanged.connect(
            self.show_properties
        )

    # -------------------------------------------------

    def open_xml(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open rgbeffects.xml",
            "",
            "XML Files (*.xml)"
        )

        if filename == "":
            return

        if not self.reader.load(filename):

            QMessageBox.warning(
                self,
                "Error",
                "Could not load XML."
            )

            return

        self.model_list.clear()

        self.model_list.addItems(
            self.reader.get_model_names()
        )

        self.statusBar().showMessage(
            f"{self.reader.count()} models loaded"
        )

    # -------------------------------------------------

    def show_properties(self, name):

        model = self.reader.get_model(name)

        if model is None:
            return

        self.property_table.setRowCount(
            len(model.attributes)
        )

        row = 0

        for key, value in sorted(model.items()):

            self.property_table.setItem(
                row,
                0,
                QTableWidgetItem(key)
            )

            self.property_table.setItem(
                row,
                1,
                QTableWidgetItem(str(value))
            )

            row += 1