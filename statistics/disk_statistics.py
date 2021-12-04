from system_resources.disk_resources import DiskResources
from statistics.utils.canvas_config import CanvasConfig
from statistics.utils.utils import Utils

import matplotlib.figure
import matplotlib.axes

from typing import List


class DiskStatistics:
    EXPLODE = [0, 0.1]
    BYTES_ON_KILOBYTE = 1024

    def __init__(self, figure: matplotlib.figure.Figure):
        self._axes_write: matplotlib.axes.Axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.DISK_POSITION_WRITE
        )
        self._axes_read: matplotlib.axes.Axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.DISK_POSITION_READ
        )
        self._pie = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.DISK_PIE_POSITION
        )
        self._init_pie = False

    def calculate(self, resources: List[DiskResources]) -> None:
        self._add_graphs(resources)
        self._add_pie(resources)
        self._add_text(resources)

    def _add_graphs(self, resources: List[DiskResources]) -> None:
        seconds = Utils.get_seconds(resources)

        read_speed = Utils.get_front_padding(resources) + [0]
        for index in range(1, len(resources)):
            read_speed.append(
                (resources[index].read_bytes - resources[index - 1].read_bytes) // DiskStatistics.BYTES_ON_KILOBYTE
            )
        read_speed = read_speed[::-1]

        write_speed = Utils.get_front_padding(resources) + [0]
        for index in range(1, len(resources)):
            write_speed.append(
                (resources[index].write_bytes - resources[index - 1].write_bytes) // DiskStatistics.BYTES_ON_KILOBYTE
            )
        write_speed = write_speed[::-1]

        Utils.draw_plot(
            self._axes_read, seconds, read_speed,
            'olive', 'Disk read speed'
        )

        Utils.draw_plot(
            self._axes_write, seconds, write_speed,
            'blue', 'Disk write speed'
        )

    def _add_pie(self, resources: List[DiskResources]) -> None:
        if not self._init_pie:
            self._pie.text(0, -1.3, 'Disk Space', ha='center', va='center')
            self._pie = self._pie.pie([
                    resources[0].free_space_percent, resources[0].used_space_percent
                ],
                explode=DiskStatistics.EXPLODE,
                labels=[
                    'Free\n\n', 'Used\n\n'
                ],
                autopct='%1.1f%%',
                shadow=True,
                startangle=90,
            )

            self._init_pie = True

    def _add_text(self, resources: List[DiskResources]) -> None:
        self._axes_write.set_ylabel('KB/s')
        # self._axes_read.set_ylabel('KB/s')
        # self._axes_read.yaxis.set_label_position('right')

        self._axes_read.set_xlabel('seconds (s)')
        self._axes_write.set_xlabel('seconds (s)')
        self._axes_read.xaxis.set_label_position('top')
        self._axes_write.xaxis.set_label_position('top')
        # self._axes_read.yaxis.tick_right()

    def clear(self) -> None:
        self._axes_read.clear()
        self._axes_write.clear()
