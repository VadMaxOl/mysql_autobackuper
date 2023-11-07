from PySide6.QtWidgets import QTableView, QLabel
from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6 import QtGui
from typing import List

import pandas as pd


data_table: pd.DataFrame # глобальная переменная для хранения данных РАБОЧЕЙ таблицы...

def get_devices_table(repair: Repair = None) -> pd.DataFrame:
    data_frame = list()
    indexes = list()
    count = 0
    for operation in operations:
        indexes.append(count)
        count += 1
        data_frame.append([operation.operation_entry_at, # дата и время вноса
                        operation.operation_workpermit, # наряд
                        operation.operation_system.system_kks, # kks оборудования
                        operation.operation_system.system_name, # оборудование
                        operation.operation_object.object_real_code + ' - ' + operation.operation_object.object_name + ' - ' + str(operation.operation_count_object_in)+ ' ед.' , # регистрационный код СО, наименование и количество
                        operation.operation_user_in.user_surname + ' ' + operation.operation_user_in.user_name[0]+'. '+operation.operation_user_in.user_fathername[0]+'.', # ФИО исполнителя
                        operation.operation_observer_in.user_surname + ' ' + operation.operation_observer_in.user_name[0]+'. '+operation.operation_observer_in.user_fathername[0]+'.', # ФИО наблюдателя
                        'да' if operation.operation_left_in_the_zone == True else '',  # оставлено в ЗОНЕ?
                        '' if operation.operation_exit_at == None else operation.operation_exit_at, # дата и время Выноса
                        operation.operation_user_out.user_surname + ' ' + operation.operation_user_out.user_name[0]+'. '+operation.operation_user_out.user_fathername[0]+'.' if operation.operation_user_out else '', # ФИО исполнителя
                        operation.operation_observer_out.user_surname + ' ' + operation.operation_observer_out.user_name[0]+'. '+operation.operation_observer_out.user_fathername[0]+'.' if operation.operation_observer_out else '']  # ФИО наблюдателя
                        )
    result = pd.DataFrame(data_frame, columns=COLUMNS, index=indexes)
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
