from dumping.figure_saver import FigureSaver
from statistics.statistics import Statistics
from system_resources.system_resources import SystemResources

import matplotlib

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

matplotlib.use('Qt5Agg')


class MainWindow(QtWidgets.QMainWindow):
    WIDTH = 1360
    HEIGHT = 700
    MILLISECONDS_TO_WAIT_IN_TIMER = 1000

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Resource Monitor Manager')
        self.resize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.showMaximized()

        self._stats = Statistics()
        self._update_plot()
        self.setCentralWidget(self._stats)

        self._configure_window()

        self.show()

        self._set_timer()

    def _update_plot(self) -> None:
        self._stats.add_resource(SystemResources())
        self._stats.clear()
        self._stats.calculate()
        self._stats.draw()

    def _configure_window(self) -> None:
        buttons = QtWidgets.QHBoxLayout()

        history_button = QtWidgets.QPushButton("History")
        save_jpeg_button = QtWidgets.QPushButton("Save as JPEG")
        save_pdf_button = QtWidgets.QPushButton("Save as PDF")
        self._label = QtWidgets.QLabel('')
        self._label.setAlignment(QtCore.Qt.AlignCenter)

        save_jpeg_button.clicked.connect(self._save_as_jpeg_action)
        save_pdf_button.clicked.connect(self._save_as_pdf_action)

        buttons.addWidget(history_button, 1)
        buttons.addWidget(self._label, 3)
        buttons.addWidget(save_jpeg_button, 1)
        buttons.addWidget(save_pdf_button, 1)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self._stats)
        layout.addLayout(buttons)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def _save_as_jpeg_action(self) -> None:
        self._label.setText('Figure successfully saved as jpeg file.')
        FigureSaver(self._stats).save_as_jpeg()

    def _save_as_pdf_action(self) -> None:
        self._label.setText('Figure successfully saved as pdf file.')
        FigureSaver(self._stats).save_as_pdf()

    def _set_timer(self) -> None:
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self._update_plot)
        self.timer.start()
