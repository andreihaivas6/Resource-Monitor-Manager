from statistics.statistics import Statistics
from system_resources.system_resources import SystemResources

import matplotlib

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

matplotlib.use('Qt5Agg')


class MainWindow(QtWidgets.QMainWindow):
    WIDTH = 1360
    HEIGHT = 700
    MILLISECONDS_TO_WAIT_IN_TIMER = 500

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.resize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.showMaximized()

        self._stats = Statistics()
        self.update_plot()

        self.setCentralWidget(self._stats)

        # toolbar = NavigationToolbar(self._stats, self)
        #
        # layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(toolbar)
        # layout.addWidget(self._stats)
        #
        # widget = QtWidgets.QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

        self.show()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        self._stats.add_resource(SystemResources())
        self._stats.clear()
        self._stats.calculate()
        self._stats.draw()
