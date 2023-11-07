from PySide6.QtWidgets import QMainWindow, QMessageBox

from ui.main_window import Ui_MainWindow
from data.list_devices import Devices
from utils.convert_subnet import cidr_to_subnetmask

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow() # инициализация окна
        self.ui.setupUi(self) 
        self.msg = QMessageBox() # инициализация окна сообщений
        self.devices = Devices.get_devices()
        for device in self.devices:
            self.ui.comboBox_devices.addItem(device)
        self.current_device:dict = self.devices[self.ui.comboBox_devices.currentText()]
        self.current_device['name'] = self.ui.comboBox_devices.currentText()
        self.ui.port_enter.setText('3306')
        self.set_text_for_labels_device()
        self.ui.comboBox_devices.currentIndexChanged.connect(self.change_device)
        self.ui.skanport_button.clicked.connect(self.run_scan_port)
        
    def set_text_for_labels_device(self) -> None:
        self.ui.label_info_mac_adress.setText(self.current_device['MAC'])
        self.ui.label_info_ip_adress.setText(self.current_device['IP'])
        self.ui.label_info_mask.setText(cidr_to_subnetmask(self.current_device['NETWORK PREFIX']))

    def change_device(self) -> None:
        self.current_device = self.devices[self.ui.comboBox_devices.currentText()]
        self.current_device['name'] = self.ui.comboBox_devices.currentText()
        self.set_text_for_labels_device()

    def run_scan_port(self) -> None:
        port = self.ui.port_enter.text()
        ip = self.current_device['IP']