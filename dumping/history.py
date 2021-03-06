from dumping.figure_saver import FigureSaver
from system_resources.system_resources import SystemResources
from statistics.utils.canvas_config import CanvasConfig

import os
import sqlite3
import jsonpickle

from typing import List


class History:
    DB_NAME = 'history.db'

    def __init__(self) -> None:
        self._initialisation_db()

    def _initialisation_db(self) -> None:
        """
        Create history table if it is not created yet and connect to database
        :return: None
        """
        db_path = os.path.join(os.getcwd(), FigureSaver.SAVE_DIRECTORY_NAME, History.DB_NAME)

        self._connection: sqlite3.Connection = sqlite3.connect(db_path)
        self._cursor: sqlite3.Cursor = self._connection.cursor()

        if not self._cursor.execute("SELECT * FROM sqlite_master WHERE type='table' and name == 'history'").fetchall():
            self._cursor.execute("CREATE TABLE history (date INTEGER, resources TEXT)")

    def dump(self, system_resources: SystemResources) -> None:
        """
        Dump system resources into database using serializing
        :param system_resources: the list of resources from last minute
        :return: None
        """
        date = system_resources.time
        encoded_object = jsonpickle.encode(system_resources)

        self._cursor.execute(f"INSERT INTO history VALUES('{date}', '{encoded_object}')")
        self._connection.commit()

    def get_resources_from_period(self, time: int) -> List[SystemResources]:
        """
        For the given time, get closest in time resources from history
        :param time: Current time as timestamp (int)
        :return: List of SystemResources from history
        """
        query = f"SELECT resources FROM history WHERE date " \
                f"BETWEEN {time - CanvasConfig.MAX_SECONDS_ON_PLOTS + 1} AND {time}"

        resources_from_period: List[SystemResources] = [
            jsonpickle.decode(resource_encoded)
            for resource_encoded, in self._cursor.execute(query)
        ]

        resources_from_period = resources_from_period[::-1]
        resources_from_period_without_interruption = [resources_from_period[0]]
        for index in range(1, len(resources_from_period)):
            if resources_from_period[index].time - resources_from_period[index - 1].time != -1:
                break
            resources_from_period_without_interruption.append(resources_from_period[index])

        return resources_from_period_without_interruption[::-1]

    def get_dates_on_periods(self) -> List[int]:
        """
        Get dates from history in order to add them to combo box
        with a difference of a minute between them
        :return: List of int (timestamp formats of dates)
        """
        all_dates = [
            date
            for date, in self._cursor.execute('SELECT date FROM history')
        ][::-1]

        if len(all_dates) == 0:
            return []

        dates_separated = [all_dates[0]]
        current_date = all_dates[0]
        for date in all_dates:
            if current_date - date >= CanvasConfig.MAX_SECONDS_ON_PLOTS:
                dates_separated.append(date)
                current_date = date
        return dates_separated[::-1]

    def close(self) -> None:
        """
        Close database connection
        :return: None
        """
        self._connection.close()
