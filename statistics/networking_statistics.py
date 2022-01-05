from system_resources.networking_resources import NetworkingResources
from statistics.utils.canvas_config import CanvasConfig
from statistics.utils.utils import Utils

import matplotlib.figure
import matplotlib.axes

from typing import List


class NetworkingStatistics:
    BYTES_ON_KILOBYTE = 1024

    def __init__(self, figure: matplotlib.figure.Figure) -> None:
        """
        Create graph plots.
        """
        self._axes_receive: matplotlib.axes.Axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.NETWORKING_POSITION_RECEIVE
        )
        self._axes_send: matplotlib.axes.Axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.NETWORKING_POSITION_SEND
        )

    def calculate(self, resources: List[NetworkingResources]) -> None:
        """
        Add plots and text on window
        :param resources: the list of resources from last minute
        :return: None
        """
        self._add_graphs(resources)
        self._add_text()

    def _add_graphs(self, resources: List[NetworkingResources]) -> None:
        """
        Add plots on window
        :param resources: the list of resources from last minute
        :return: None
        """
        seconds = Utils.get_seconds()

        sent_speed = Utils.get_front_padding(resources) + [0.]
        receive_speed = Utils.get_front_padding(resources) + [0.]
        for index in range(1, len(resources)):
            sent_speed.append(
                (resources[index].bytes_sent - resources[index - 1].bytes_sent)
                / NetworkingStatistics.BYTES_ON_KILOBYTE
            )
            receive_speed.append(
                (resources[index].bytes_received - resources[index - 1].bytes_received)
                / NetworkingStatistics.BYTES_ON_KILOBYTE
            )
        sent_speed = sent_speed[::-1]
        receive_speed = receive_speed[::-1]

        Utils.draw_plot(
            self._axes_send, seconds, sent_speed,
            'green', 'Networking sent speed'
        )

        Utils.draw_plot(
            self._axes_receive, seconds, receive_speed,
            'orange', 'Networking receive speed'
        )

    def _add_text(self) -> None:
        """
        Add text on window
        :return: None
        """
        self._axes_send.set_xlabel('seconds (s)')
        self._axes_receive.set_xlabel('seconds (s)')

        self._axes_receive.set_ylabel('KB/s')

    def clear(self) -> None:
        """
        Clear window
        :return: None
        """
        self._axes_receive.clear()
        self._axes_send.clear()
