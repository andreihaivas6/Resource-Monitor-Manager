import psutil
import json


class DiskResources:
    FILE_SYSTEM_TYPES = [
        'NTFS',
        'ext3',
    ]

    def __init__(self) -> None:
        available_partitions_mount_points = [
            partition.mountpoint
            for partition in psutil.disk_partitions()
            if partition.fstype in DiskResources.FILE_SYSTEM_TYPES
        ]
        self._partitions_counter: int = len(available_partitions_mount_points)

        partitions_usage = [
            psutil.disk_usage(mount_point)
            for mount_point in available_partitions_mount_points
        ]

        self._total_space: int = sum([
            partition_usage.total
            for partition_usage in partitions_usage
        ])
        self._used_space: int = sum([
            partition_usage.used
            for partition_usage in partitions_usage
        ])
        self._free_space: int = sum([
            partition_usage.free
            for partition_usage in partitions_usage
        ])

        self._used_space_percent: float = round(100 * self._used_space / self._total_space, 1)
        self._free_space_percent: float = round(100 * self._free_space / self._total_space, 1)

        disk_io_counters = psutil.disk_io_counters()
        self._read_bytes: int = disk_io_counters.read_bytes
        self._write_bytes: int = disk_io_counters.write_bytes

    @property
    def partitions_counter(self) -> int:
        return self._partitions_counter

    @property
    def total_space(self) -> int:
        return self._total_space

    @property
    def free_space(self) -> int:
        return self._free_space

    @property
    def used_space(self) -> int:
        return self._used_space

    @property
    def free_space_percent(self) -> float:
        return self._free_space_percent

    @property
    def used_space_percent(self) -> float:
        return self._used_space_percent

    @property
    def read_bytes(self) -> int:
        return self._read_bytes

    @property
    def write_bytes(self) -> int:
        return self._write_bytes

    def __str__(self) -> str:
        return json.dumps(self.__dict__, indent=4)
