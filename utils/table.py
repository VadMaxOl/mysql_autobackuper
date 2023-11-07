from PySide6.QtWidgets import QTableView
from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6 import QtGui
from typing import List
import pandas as pd
from data.constants import COLUMNS_DEVICES

data_table: pd.DataFrame # глобальная переменная для хранения данных РАБОЧЕЙ таблицы...

def get_devices_table(ip_adreses: list = None) -> pd.DataFrame:
    data_frame = list()
    indexes = list()
    count = 0
    for ip_adress in ip_adreses:
        indexes.append(count)
        count += 1
        data_frame.append([ip_adress])  # ФИО наблюдателя
    result = pd.DataFrame(data_frame, columns=COLUMNS_DEVICES, index=indexes)
    return result

################ модель данных для таблицы РАБОЧЕГО ОКНА #########
class TableModel_MainWindow(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame, tableView: QTableView):   
        super(TableModel_MainWindow, self).__init__()
        self._data = data # data - данные;
        self._tableView = tableView # tableView - объект таблицы;

    def data(self, index, role):
        value = self._data.iloc[index.row(), index.column()] # значение текущей ячейки
        if role == Qt.DisplayRole:
            return str(value)
        if role == Qt.BackgroundRole:
            pass

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def sort(self, column=None, direction=None):
        if direction == Qt.SortOrder.AscendingOrder:
            ascending = True
        else: ascending = False
        temp_data_table = data_table.sort_values(by=str(column+1), ascending=ascending)
        model = TableModel_MainWindow(temp_data_table, self._tableView)
        self._tableView.setModel(model)
##########################################################
