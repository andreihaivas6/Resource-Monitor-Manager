from statistics.statistics import Statistics

from datetime import datetime

import os


class FigureSaver:
    DIRECTORY_NAME = 'saved'

    def __init__(self, statistics: Statistics):
        self._statistics = statistics

    def save_as_jpeg(self) -> None:
        self._save_figure('jpeg')

    def save_as_pdf(self) -> None:
        self._save_figure('pdf')

    def _save_figure(self, extension: str) -> None:
        directory_path = os.path.join(os.getcwd(), FigureSaver.DIRECTORY_NAME)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

        current_time_as_string = datetime.utcfromtimestamp(self._statistics.current_time).strftime('%Y-%m-%d_%H-%M-%S')
        filename = f"{current_time_as_string}.{extension}"

        path_to_save = os.path.join(directory_path, filename)
        self._statistics.figure.savefig(path_to_save)
