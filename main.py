import sys
import ifaddr
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_logic.main_window import MainWindow
from data.list_devices import Devices


if __name__ == "__main__":
    app = QApplication(sys.argv)
    devices = dict()
    adapters = ifaddr.get_adapters()
    for adapter in adapters:
        devices[adapter.nice_name] = {
            'MAC': adapter.ips[0].ip[0],
            'IP': adapter.ips[1].ip,
            'NETWORK PREFIX': adapter.ips[1].network_prefix,
        }
    Devices.set_devices(devices)
    main_window: QMainWindow = MainWindow()
    main_window.show()
    sys.exit(app.exec())  