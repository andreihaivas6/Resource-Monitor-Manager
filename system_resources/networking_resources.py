import psutil


class NetworkingResources:
    NETWORK_INTERFACE_CARD_NAMES = [
        'Wi-Fi', 'Ethernet',
    ]

    def __init__(self):
        net_io_counter = psutil.net_io_counters(nowrap=True)
        self._bytes_sent = net_io_counter.bytes_sent
        self._bytes_received = net_io_counter.bytes_recv

        self._network_name = '-'
        self._network_address = '-'
        network_interface_card_stats = psutil.net_if_stats()
        network_interface_card_addresses = psutil.net_if_addrs()
        for name in NetworkingResources.NETWORK_INTERFACE_CARD_NAMES:
            if network_interface_card_stats[name].isup:
                self._network_name = name
                self._network_address = network_interface_card_addresses[name][1].address
                break
