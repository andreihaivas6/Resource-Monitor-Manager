"""
Useful:
    - psutil:
        https://pypi.org/project/psutil/
        https://psutil.readthedocs.io/en/latest/

    - matplotlib

    - serialize/deserialize:
        import jsonpickle

        x = SystemResources()
        y = jsonpickle.encode(x)
        new_x = jsonpickle.decode(y)

        SAU
        in toate 4 clase:
            def as_dict(self) -> dict:
                return self.__dict__
        apoi in SR:
            def as_dict(self) -> dict:
                return {
                    "_time": self._time,
                    "_cpu_resources": self._cpu_resources.as_dict(),
                    "_disk_resources": self._disk_resources.as_dict(),
                    "_memory_resources": self._memory_resources.as_dict(),
                    "_networking_resources": self._networking_resources.as_dict(),
                }
        si:
            my_json_str = json.dumps(x.__dict__)  # face string
            new_json_dict = json.loads(my_json_str)  # face dict
            new_x = Test(**new_json_dict)  # + constructori in toate clasele

    - convert jpeg to pdf:
        from PIL import Image

        image1 = Image.open(r'D:/Facultate/MATERII/An 3 Sem1/5. PP/Proiect/Resource-Monitor-Manager/2013.jpeg')
        im1 = image1.convert('RGB')
        im1.save(r'D:/Facultate/MATERII/An 3 Sem1/5. PP/Proiect/Resource-Monitor-Manager/2013.pdf')

        sau

        import matplotlib.pyplot as plt

        f = plt.figure()
        plt.plot(range(10), range(10), "o")
        plt.show()

        f.savefig("foo.pdf", bbox_inches='tight')

    - collect processes info:
        ram = psutil.virtual_memory().total
        for p in psutil.process_iter():
            print(p, p.cpu_percent(), ram / p.memory_info().vms * 100)
            print(p, p.cpu_percent(), p.memory_info().vms / ram * 100, p.memory_info().vms / 1024 / 1024,
                  '-------------' if 'charm' in p.name() else '')

    - convert json -> obj / obj -> json:
        import json

        class Test:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __str__(self):
                return f'Test: x = {self.x}, y = {self.y}.'

        if __name__ == '__main__':
            x = Test(1, 2)
            my_json_str = json.dumps(x.__dict__)  # face string
            new_json_dict = json.loads(my_json_str)  # face dict
            new_x = Test(**new_json_dict)

"""

from app.main_window import MainWindow

import sys

from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = MainWindow()
    app.exec_()
