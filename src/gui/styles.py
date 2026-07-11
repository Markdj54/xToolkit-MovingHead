"""
xToolkit Style Sheet

Version 0.4.0
"""

DARK_STYLE = """

QMainWindow {
    background-color: #252526;
}

QWidget {
    background-color: #252526;
    color: #F0F0F0;
    font-size: 10pt;
    font-family: Segoe UI;
}

QListWidget {
    background-color: #2D2D30;
    border: 1px solid #3F3F46;
    selection-background-color: #007ACC;
}

QTableWidget {
    background-color: #1E1E1E;
    color: white;
    border: 1px solid #444444;
    gridline-color: #404040;
    alternate-background-color: #252526;
}

QHeaderView::section {
    background-color: #2D2D30;
    color: #58A6FF;
    font-weight: bold;
    padding: 6px;
    border: none;
}

QPushButton {
    background-color: #007ACC;
    color: white;
    padding: 8px;
    border-radius: 5px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #0098FF;
}

QCheckBox {
    color: #58A6FF;
    font-size: 11pt;
    font-weight: bold;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
}

QToolBar {
    spacing: 12px;
    padding: 8px;
    background-color: #2C2C2C;
    border-bottom: 1px solid #444444;
}

QToolButton {
    color: white;
    padding: 8px;
    border-radius: 6px;
}

QToolButton:hover {
    background-color: #3A3A3A;
}

QStatusBar {
    background-color: #333333;
}

QLabel {
    color: white;
}

QGroupBox {
    border: 1px solid #444444;
    border-radius: 6px;
    margin-top: 10px;
    font-weight: bold;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0px 5px;
    color: #58A6FF;
}

"""