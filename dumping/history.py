from dumping.figure_saver import FigureSaver
from system_resources.system_resources import SystemResources
from statistics.utils.canvas_config import CanvasConfig

import os
import sqlite3
import jsonpickle

from typing import List


class History:
    DB_NAME = 'history.db'

    def __init__(self):
        self._connection = None
        self._cursor = None
        self._init_db()

    def _init_db(self) -> None:
        db_path = os.path.join(os.getcwd(), FigureSaver.SAVE_DIRECTORY_NAME, History.DB_NAME)

        table_exists = True
        if not os.path.exists(db_path):
            table_exists = False

        self._connection = sqlite3.connect(db_path)
        self._cursor = self._connection.cursor()
        if not table_exists:
            self._cursor.execute("CREATE TABLE history (date INTEGER, resources TEXT)")

    def dump(self, system_resources: SystemResources) -> None:
        date = system_resources.time
        encoded_object = jsonpickle.encode(system_resources)

        self._cursor.execute(f"INSERT INTO history VALUES('{date}', '{encoded_object}')")
        self._connection.commit()

    def get_resources_from_period(self, time: int) -> List[SystemResources]:
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
