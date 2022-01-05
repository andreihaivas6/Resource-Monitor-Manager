import time

from statistics.statistics import Statistics

import os

from datetime import datetime


class FigureSaver:
    SAVE_DIRECTORY_NAME = 'saved'

    def __init__(self, statistics: Statistics) -> None:
        self._statistics: Statistics = statistics

    def save_as_jpeg(self) -> None:
        """
        Save current statistics as a jpeg file
        :return: None
        """
        self._save_figure('jpeg')

    def save_as_pdf(self) -> None:
        """
        Save current statistics as a pdf file
        :return: None
        """
        self._save_figure('pdf')

    def _save_figure(self, extension: str) -> None:
        """
        Save current statistics with current time as filename using a given extension
        :return: None
        """
        directory_path = os.path.join(os.getcwd(), FigureSaver.SAVE_DIRECTORY_NAME)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

        current_time_as_string = \
            f"{datetime.utcfromtimestamp(self._statistics.current_time).strftime('%d-%m-%Y_%H-%M-%S')}" \
            f"-{str(time.time()).replace('.', '')}"
        filename = f"{current_time_as_string}.{extension}"

        path_to_save = os.path.join(directory_path, filename)
        self._statistics.figure.savefig(path_to_save)
