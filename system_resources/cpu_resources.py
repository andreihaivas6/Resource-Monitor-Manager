import psutil


class CPUResources:
    INTERVAL_CPU = 0.5

    def __init__(self):
        cpu_percents = psutil.cpu_times_percent(interval=CPUResources.INTERVAL_CPU)
        self._cpu_percent = round(100 - cpu_percents.idle, 1)
        self._cpu_percent_user = cpu_percents.user
        self._cpu_percent_system = cpu_percents.system

        self._processes_count = len(psutil.pids())
        self._threads_count = sum([
            process.num_threads()
            for process in psutil.process_iter()
        ])

        self._cpu_logical_count = psutil.cpu_count()
        self._cpu_physical_count = psutil.cpu_count(logical=False)
        self._cpu_base_speed = psutil.cpu_freq().current
