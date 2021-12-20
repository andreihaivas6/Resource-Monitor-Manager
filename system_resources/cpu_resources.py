import psutil
import json


class CPUResources:
    INTERVAL_CPU = 0.0

    def __init__(self) -> None:
        cpu_percents = psutil.cpu_times_percent(interval=CPUResources.INTERVAL_CPU)
        self._cpu_percent: float = round(100 - cpu_percents.idle, 1)
        self._cpu_percent_user: float = cpu_percents.user
        self._cpu_percent_system: float = cpu_percents.system

        self._processes_count: int = len(psutil.pids())

        self._cpu_logical_count: int = psutil.cpu_count()
        self._cpu_physical_count: int = psutil.cpu_count(logical=False)
        self._cpu_base_speed: float = psutil.cpu_freq().current

    @property
    def cpu_percent(self) -> float:
        return self._cpu_percent

    @property
    def cpu_percent_user(self) -> float:
        return self._cpu_percent_user

    @property
    def cpu_percent_system(self) -> float:
        return self._cpu_percent_system

    @property
    def processes_count(self) -> int:
        return self._processes_count

    @property
    def cpu_logical_count(self) -> int:
        return self._cpu_logical_count

    @property
    def cpu_physical_count(self) -> int:
        return self._cpu_physical_count

    @property
    def cpu_base_speed(self) -> float:
        return self._cpu_base_speed

    def __str__(self) -> str:
        return json.dumps(self.__dict__, indent=4)
