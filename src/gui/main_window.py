from PySide6.QtWidgets import (
    QMainWindow, QWidget, QListWidget, QPushButton,
    QSplitter, QVBoxLayout, QCheckBox, QFileDialog,
    QToolBar, QGroupBox
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

from core.xml_reader import XMLReader
from gui.fixture_view import FixtureView


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.reader = XMLReader()

        self.setWindowTitle("xToolkit")
        self.resize(1500, 850)

        self.create_toolbar()
        self.create_widgets()
        self.create_layout()
        self.connect_signals()

        self.statusBar().showMessage("Version 0.4.0 Alpha    Ready")

    def create_toolbar(self):
        toolbar = QToolBar("Main")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        self.open_action = QAction("📂 Open XML", self)
        self.open_action.triggered.connect(self.open_xml)
        toolbar.addAction(self.open_action)

        toolbar.addSeparator()

        self.compare_action = QAction("🔄 Compare", self)
        self.compare_action.setEnabled(False)
        toolbar.addAction(self.compare_action)

        toolbar.addSeparator()

        self.export_action = QAction("💾 Export", self)
        self.export_action.setEnabled(False)
        toolbar.addAction(self.export_action)

        toolbar.addSeparator()

        self.about_action = QAction("❓ About", self)
        toolbar.addAction(self.about_action)

    def create_widgets(self):
        self.filter = QCheckBox("Moving Heads Only")
        self.source = QListWidget()
        self.destination = QListWidget()
        self.viewer = FixtureView()
        self.compare = QPushButton("🔄 Compare Fixtures")
        self.compare.setMinimumHeight(42)
        self.compare.setEnabled(False)

    def create_layout(self):
        splitter = QSplitter(Qt.Horizontal)

        sg = QGroupBox("Original Fixture")
        sl = QVBoxLayout(sg)
        sl.addWidget(self.source)

        dg = QGroupBox("Replacement Fixture")
        dl = QVBoxLayout(dg)
        dl.addWidget(self.destination)

        vg = QGroupBox("Fixture Information")
        vl = QVBoxLayout(vg)
        vl.addWidget(self.viewer)

        splitter.addWidget(sg)
        splitter.addWidget(dg)
        splitter.addWidget(vg)
        splitter.setSizes([280,280,940])

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(self.filter)
        layout.addWidget(splitter)
        layout.addWidget(self.compare)
        self.setCentralWidget(central)

    def connect_signals(self):
        self.source.currentTextChanged.connect(self.show_source)
        self.destination.currentTextChanged.connect(self.enable_compare)
        self.filter.stateChanged.connect(self.refresh)

    def open_xml(self):
        filename,_=QFileDialog.getOpenFileName(self,"Open rgbeffects.xml","","XML Files (*.xml)")
        if not filename:
            return
        if self.reader.load(filename):
            self.refresh()
            mh=len(self.reader.get_moving_heads())
            self.statusBar().showMessage(f"Models: {self.reader.count()} | Moving Heads: {mh} | Version 0.4.0 Alpha")

    def refresh(self):
        names=[m.name for m in self.reader.get_moving_heads()] if self.filter.isChecked() else self.reader.get_model_names()
        self.source.clear()
        self.destination.clear()
        self.source.addItems(names)
        self.destination.addItems(names)

    def show_source(self,name):
        self.viewer.show_fixture(self.reader.get_model(name))
        self.enable_compare()

    def enable_compare(self):
        enabled=self.source.currentItem() is not None and self.destination.currentItem() is not None
        self.compare.setEnabled(enabled)
        self.compare_action.setEnabled(enabled)
