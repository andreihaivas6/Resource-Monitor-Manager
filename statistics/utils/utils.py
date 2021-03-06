from statistics.utils.canvas_config import CanvasConfig

import matplotlib.axes

from typing import List


class Utils:
    BYTES_ON_KB = 1024

    @staticmethod
    def get_seconds() -> List[int]:
        """
        Get a list of seconds of length MAX_SECONDS_ON_PLOTS
        :return: List of seconds (int)
        """
        return [
            second
            for second in range(CanvasConfig.MAX_SECONDS_ON_PLOTS)
        ]

    @staticmethod
    def get_front_padding(resources: list) -> List[float]:
        """
        Add zeroes when resources list is smaller than MAX_SECONDS_ON_PLOTS
        :param resources: the list of resources from last minute
        :return: List of zeroes
        """
        return [0.] * (CanvasConfig.MAX_SECONDS_ON_PLOTS - len(resources))

    @staticmethod
    def draw_plot(
            axes: matplotlib.axes.Axes, x_list: List[int], y_list: List[float],
            color: str, label: str, alpha: int = 0.4) -> None:
        """
        Draw plot with colors and legends.
        :param axes: Given axes to draw on
        :param x_list: List of x coordinates
        :param y_list: List of y coordinates
        :param color: Color for plot
        :param label: Label for legend
        :param alpha: Alpha transparency
        :return: None
        """
        axes.fill_between(
            x_list,
            y_list,
            color=color,
            alpha=alpha,
        )

        axes.plot(
            x_list,
            y_list,
            color=color,
            label=label,
        )
        if len(label) > 0:
            axes.legend()

    @staticmethod
    def transform_to_gb(my_bytes: int) -> float:
        """
        Transform a value of bytes into gigabytes.
        :param my_bytes: Value on bytes
        :return: Value on gigabytes (float)
        """
        return round(my_bytes / (Utils.BYTES_ON_KB ** 3), 1)

    @staticmethod
    def transform_bytes(my_bytes: int) -> str:
        """
        Transform a value of bytes into a multiple of bytes in order to look properly
        :param my_bytes: Value on bytes
        :return: a string containing the value transformed and measure unit
        """
        values = ['B', 'KB', 'MB', 'GB', 'TB']

        count = 0
        while (my_bytes / Utils.BYTES_ON_KB) > 1:
            my_bytes /= Utils.BYTES_ON_KB
            count += 1

        return f'{round(my_bytes, 1)} {values[count]}'
