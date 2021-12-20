from dumping.figure_saver import FigureSaver
from dumping.history import History
from statistics.statistics import Statistics
from statistics.utils.canvas_config import CanvasConfig
from system_resources.system_resources import SystemResources

import matplotlib

from PyQt5 import QtCore, QtWidgets
from datetime import datetime
from typing import List

matplotlib.use('Qt5Agg')


class MainWindow(QtWidgets.QMainWindow):
    WIDTH = 1360
    HEIGHT = 700
    MILLISECONDS_TO_WAIT_IN_TIMER = 1000

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Resource Monitor Manager')
        self.resize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.showMaximized()

        self._history: History = History()
        self._dates: List[int] = self._history.get_dates_on_periods()
        self._combo_box: QtWidgets.QComboBox = QtWidgets.QComboBox()
        self._combo_box_initialised: bool = False

        self._stats: Statistics = Statistics()
        self._update_plot()
        self.setCentralWidget(self._stats)

        self._configure_window()
        self.show()
        self._set_timer()

    def _update_plot(self) -> None:
        system_resources = SystemResources()
        self._stats.add_resource(system_resources)
        self._history.dump(system_resources)
        if self._combo_box_initialised and system_resources.time - self._dates[-1] >= CanvasConfig.MAX_SECONDS_ON_PLOTS:
            self._dates.append(system_resources.time)
            self._combo_box.addItem(MainWindow.get_date_for_combo_box(system_resources.time))

        self._stats.clear()
        self._stats.calculate()
        self._stats.draw()

    def _configure_window(self) -> None:
        self._buttons = QtWidgets.QHBoxLayout()
        self._get_widgets()
        self._add_action_on_buttons()
        self._add_widgets()
        self._set_layout()

    def _get_widgets(self) -> None:
        self._now_button = QtWidgets.QPushButton("Get current statistics")
        self._history_button = QtWidgets.QPushButton("Get History on Date:")
        self._save_jpeg_button = QtWidgets.QPushButton("Save as JPEG")
        self._save_pdf_button = QtWidgets.QPushButton("Save as PDF")
        self._exit_button = QtWidgets.QPushButton("Exit")

        self._label = QtWidgets.QLabel('Getting current statistics...')
        self._label.setAlignment(QtCore.Qt.AlignCenter)

        self._combo_box.addItems([
            MainWindow.get_date_for_combo_box(date)
            for date in self._dates
        ])
        self._combo_box_initialised = True

    def _add_action_on_buttons(self) -> None:
        self._save_jpeg_button.clicked.connect(self._save_as_jpeg_action)
        self._save_pdf_button.clicked.connect(self._save_as_pdf_action)
        self._history_button.clicked.connect(self._get_history)
        self._now_button.clicked.connect(self._get_current_stats)
        self._exit_button.clicked.connect(self._exit_app)

    def _save_as_jpeg_action(self) -> None:
        self._label.setText('Figure successfully saved as jpeg file.')
        FigureSaver(self._stats).save_as_jpeg()

    def _save_as_pdf_action(self) -> None:
        self._label.setText('Figure successfully saved as pdf file.')
        FigureSaver(self._stats).save_as_pdf()

    def _get_history(self) -> None:
        self._label.setText(f'History on date: {self._combo_box.currentText()}')
        self.timer.stop()

        date = self._dates[self._combo_box.currentIndex()]
        history_resources = self._history.get_resources_from_period(date)

        self._stats.set_resources_from_history(history_resources)
        self._stats.clear()
        self._stats.calculate()
        self._stats.draw()

    def _get_current_stats(self) -> None:
        if not self.timer.isActive():
            self.timer.start()
            self._label.setText(f'Getting current statistics...')
            self._stats.clear_resources()

    def _exit_app(self) -> None:
        self._history.close()
        self.close()

    def _add_widgets(self) -> None:
        self._buttons.addWidget(self._now_button, 2)
        self._buttons.addWidget(self._history_button, 2)
        self._buttons.addWidget(self._combo_box, 2)
        self._buttons.addWidget(self._label, 6)
        self._buttons.addWidget(self._save_jpeg_button, 2)
        self._buttons.addWidget(self._save_pdf_button, 2)
        self._buttons.addWidget(self._exit_button, 1)

    def _set_layout(self) -> None:
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self._stats)
        layout.addLayout(self._buttons)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def _set_timer(self) -> None:
        self.timer = QtCore.QTimer()
        self.timer.setInterval(MainWindow.MILLISECONDS_TO_WAIT_IN_TIMER)
        self.timer.timeout.connect(self._update_plot)
        self.timer.start()

    @staticmethod
    def get_date_for_combo_box(date: int) -> str:
        return datetime.utcfromtimestamp(date).strftime('%A %d/%m/%Y %H:%M:%S')
