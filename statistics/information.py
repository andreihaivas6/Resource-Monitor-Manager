from statistics.utils.canvas_config import CanvasConfig
from statistics.utils.utils import Utils
from system_resources.system_resources import SystemResources

import matplotlib.figure
import matplotlib.axes
import matplotlib.lines

from typing import List


class Information:
    def __init__(self, figure: matplotlib.figure.Figure):
        self._axes: matplotlib.axes.Axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.INFORMATION_POSITION
        )

    def calculate(self, resources: List[SystemResources]) -> None:
        Utils.draw_plot(self._axes, [0, 10], [0, 10], 'white', '')

        self._calculate_cpu(resources)
        self._calculate_disk(resources)
        self._calculate_memory(resources)
        self._calculate_networking(resources)

        self._axes.axis('off')

    def _calculate_cpu(self, resources: List[SystemResources]) -> None:
        cpu = resources[-1].cpu

        self._axes.text(-0.5, 10.5, '_' * CanvasConfig.SEPARATOR_LENGTH)
        self._axes.text(0, 10, f'CPU Usage: {cpu.cpu_percent}%')
        self._axes.text(0, 9.5, f'(User: {cpu.cpu_percent_user}%, System: {cpu.cpu_percent_system}%)')
        self._axes.text(0, 9, f'Cores: Physical: {cpu.cpu_physical_count} | Logical: {cpu.cpu_logical_count}')
        self._axes.text(0, 8.5, f'Processes: {cpu.processes_count} | Threads: {cpu.threads_count}')
        self._axes.text(-0.5, 8.15, '_' * CanvasConfig.SEPARATOR_LENGTH)

    def _calculate_disk(self, resources: List[SystemResources]) -> None:
        disk2 = resources[-1].disk
        disk1 = resources[-2].disk \
            if len(resources) > 1 \
            else disk2

        self._axes.text(-0.5, 7.65, '_' * CanvasConfig.SEPARATOR_LENGTH)
        self._axes.text(0, 7.15, f'Free disk space:  {Utils.transform_to_gb(disk2.free_space)}'
                                 f'/{Utils.transform_to_gb(disk2.total_space)} GB')
        self._axes.text(0, 7.15 - 0.5, f'Used disk space: {Utils.transform_to_gb(disk2.used_space)}'
                                       f'/{Utils.transform_to_gb(disk2.total_space)} GB')
        self._axes.text(0, 6.15, f'Disk write speed: ' + Utils.transform_bytes(disk2.write_bytes - disk1.write_bytes))
        self._axes.text(0, 6.15 - 0.5, f'Disk read speed: ' + Utils.transform_bytes(disk2.read_bytes - disk1.read_bytes))
        self._axes.text(-0.5, 5.35, '_' * CanvasConfig.SEPARATOR_LENGTH)

    def _calculate_memory(self, resources: List[SystemResources]) -> None:
        memory = resources[-1].memory

        self._axes.text(-0.5, 4.85, '_' * CanvasConfig.SEPARATOR_LENGTH)
        self._axes.text(0, 4.35, f'Free memory:  {Utils.transform_to_gb(memory.available_memory)}/'
                                 f'{Utils.transform_to_gb(memory.total_memory)} GB')
        self._axes.text(0, 4.35 - 0.5, f'Used memory: {Utils.transform_to_gb(memory.used_memory)}/'
                                       f'{Utils.transform_to_gb(memory.total_memory)} GB')
        self._axes.text(0, 3.35, f'Free memory percent:  {memory.available_memory_percent} %')
        self._axes.text(0, 3.35 - 0.5, f'Used memory percent: {memory.used_memory_percent} %')
        self._axes.text(-0.5, 2.5, '_' * CanvasConfig.SEPARATOR_LENGTH)

    def _calculate_networking(self, resources: List[SystemResources]) -> None:
        net2 = resources[-1].networking
        net1 = resources[-2].networking \
            if len(resources) > 1 \
            else net2

        self._axes.text(-0.5, 1.95, '_' * CanvasConfig.SEPARATOR_LENGTH)
        self._axes.text(0, 1.45, f'Network receive speed: '
                                 f'{Utils.transform_bytes(net2.bytes_received - net1.bytes_received)}')
        self._axes.text(0, 0.95, f'Network send speed:     '
                                 f'{Utils.transform_bytes(net2.bytes_sent - net1.bytes_sent)}')
        self._axes.text(0, 0.45, f'Network name: {net2.network_name}')
        self._axes.text(0, -0.05, f'Network address: {net2.network_address}')
        self._axes.text(-0.5, -0.4, '_' * CanvasConfig.SEPARATOR_LENGTH)

    def clear(self) -> None:
        self._axes.clear()
