# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowvBRoKM.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 659)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_device = QLabel(self.centralwidget)
        self.label_device.setObjectName(u"label_device")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_device.setFont(font)

        self.verticalLayout_7.addWidget(self.label_device)

        self.comboBox_devices = QComboBox(self.centralwidget)
        self.comboBox_devices.setObjectName(u"comboBox_devices")
        font1 = QFont()
        font1.setPointSize(12)
        self.comboBox_devices.setFont(font1)

        self.verticalLayout_7.addWidget(self.comboBox_devices)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_mac_adress = QLabel(self.centralwidget)
        self.label_mac_adress.setObjectName(u"label_mac_adress")
        self.label_mac_adress.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_mac_adress)

        self.label_info_mac_adress = QLabel(self.centralwidget)
        self.label_info_mac_adress.setObjectName(u"label_info_mac_adress")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        self.label_info_mac_adress.setFont(font2)
        self.label_info_mac_adress.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_info_mac_adress)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_ip_adress = QLabel(self.centralwidget)
        self.label_ip_adress.setObjectName(u"label_ip_adress")
        self.label_ip_adress.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_ip_adress)

        self.label_info_ip_adress = QLabel(self.centralwidget)
        self.label_info_ip_adress.setObjectName(u"label_info_ip_adress")
        self.label_info_ip_adress.setFont(font2)
        self.label_info_ip_adress.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_info_ip_adress)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_mask = QLabel(self.centralwidget)
        self.label_mask.setObjectName(u"label_mask")
        self.label_mask.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_mask)

        self.label_info_mask = QLabel(self.centralwidget)
        self.label_info_mask.setObjectName(u"label_info_mask")
        self.label_info_mask.setFont(font2)
        self.label_info_mask.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_info_mask)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_6.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_6)

        self.devices_view = QTableView(self.centralwidget)
        self.devices_view.setObjectName(u"devices_view")

        self.verticalLayout_6.addWidget(self.devices_view)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_4)

        self.port_enter = QLineEdit(self.centralwidget)
        self.port_enter.setObjectName(u"port_enter")

        self.verticalLayout_4.addWidget(self.port_enter)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.skanport_button = QPushButton(self.centralwidget)
        self.skanport_button.setObjectName(u"skanport_button")

        self.verticalLayout_5.addWidget(self.skanport_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.verticalLayout.addWidget(self.label)

        self.login_enter = QLineEdit(self.centralwidget)
        self.login_enter.setObjectName(u"login_enter")

        self.verticalLayout.addWidget(self.login_enter)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_2)

        self.password_enter = QLineEdit(self.centralwidget)
        self.password_enter.setObjectName(u"password_enter")
        self.password_enter.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_enter)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MySQL Auto Backuper", None))
        self.label_device.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0442\u0435\u0432\u043e\u0439 \u0430\u0434\u0430\u043f\u0442\u0435\u0440:", None))
        self.label_mac_adress.setText(QCoreApplication.translate("MainWindow", u"MAC \u0430\u0434\u0440\u0435\u0441:", None))
        self.label_info_mac_adress.setText(QCoreApplication.translate("MainWindow", u"MAC", None))
        self.label_ip_adress.setText(QCoreApplication.translate("MainWindow", u"IP \u0430\u0434\u0440\u0435\u0441:", None))
        self.label_info_ip_adress.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.label_mask.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u043a\u0430 \u043f\u043e\u0434\u0441\u0435\u0442\u0438:", None))
        self.label_info_mask.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u043a\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0440\u0442:", None))
        self.label_5.setText("")
        self.skanport_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
#if QT_CONFIG(statustip)
        self.login_enter.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.login_enter.setInputMask("")
        self.login_enter.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.password_enter.setInputMask("")
    # retranslateUi

