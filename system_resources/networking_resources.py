import psutil
import json


class NetworkingResources:
    NETWORK_INTERFACE_CARD_NAMES = [
        'Wi-Fi',
        'Ethernet',
    ]

    def __init__(self) -> None:
        net_io_counter = psutil.net_io_counters(nowrap=True)
        self._bytes_sent: int = net_io_counter.bytes_sent
        self._bytes_received: int = net_io_counter.bytes_recv

        self._network_name: str = '-'
        self._network_address: str = '-'
        network_interface_card_stats = psutil.net_if_stats()
        network_interface_card_addresses = psutil.net_if_addrs()
        for name in NetworkingResources.NETWORK_INTERFACE_CARD_NAMES:
            if network_interface_card_stats[name].isup:
                self._network_name = name
                self._network_address = network_interface_card_addresses[name][1].address
                break

    @property
    def bytes_sent(self) -> int:
        return self._bytes_sent

    @property
    def bytes_received(self) -> int:
        return self._bytes_received

    @property
    def network_name(self) -> str:
        return self._network_name

    @property
    def network_address(self) -> str:
        return self._network_address

    def __str__(self) -> str:
        return json.dumps(self.__dict__, indent=4)
