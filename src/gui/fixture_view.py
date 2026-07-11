"""
fixture_view.py

Professional Fixture Inspector
xToolkit v0.4.0
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)


class FixtureView(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        #
        # Heading
        #

        heading = QLabel("Fixture Information")

        heading.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
            color:#58A6FF;
            padding:6px;
        """)

        layout.addWidget(heading)

        #
        # Property table
        #

        self.properties = QTableWidget()

        self.properties.setColumnCount(2)

        self.properties.setHorizontalHeaderLabels(
            ["Property", "Value"]
        )

        self.properties.verticalHeader().hide()

        self.properties.horizontalHeader().setStretchLastSection(True)

        self.properties.horizontalHeader().setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents
        )

        layout.addWidget(self.properties)

        #
        # Channel heading
        #

        channels = QLabel("DMX Channel Map")

        channels.setStyleSheet("""
            font-size:15px;
            font-weight:bold;
            color:#58A6FF;
            padding-top:12px;
            padding-bottom:4px;
        """)

        layout.addWidget(channels)

        #
        # Channel table
        #

        self.channels = QTableWidget()

        self.channels.setColumnCount(2)

        self.channels.setHorizontalHeaderLabels(
            ["Channel", "Function"]
        )

        self.channels.verticalHeader().hide()

        self.channels.horizontalHeader().setStretchLastSection(True)

        self.channels.horizontalHeader().setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents
        )

        layout.addWidget(self.channels)

    # ---------------------------------------------------------

    def clear(self):

        self.properties.setRowCount(0)

        self.channels.setRowCount(0)

    # ---------------------------------------------------------

    def show_fixture(self, model):

        self.clear()

        if model is None:

            return

        summary = model.get_summary()

        self.properties.setRowCount(len(summary))

        row = 0

        for key, value in summary.items():

            self.properties.setItem(
                row,
                0,
                QTableWidgetItem(str(key))
            )

            self.properties.setItem(
                row,
                1,
                QTableWidgetItem(str(value))
            )

            row += 1

        self.channels.setRowCount(
            model.channel_count
        )

        for channel in range(1, model.channel_count + 1):

            self.channels.setItem(
                channel - 1,
                0,
                QTableWidgetItem(str(channel))
            )

            self.channels.setItem(
                channel - 1,
                1,
                QTableWidgetItem(
                    model.get_channel_name(channel)
                )
            )