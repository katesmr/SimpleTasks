from PySide.QtCore import Qt
from PySide.QtGui import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QRadioButton, \
                         QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
from src.core.algorithm import code, decode, create_matrix_message
from src.view.utils.helper import str_list_to_int, split_edit


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.base_layer = QVBoxLayout()
        self.data_part = QGridLayout()
        self.result_layer = QVBoxLayout()
        self.table_part = QHBoxLayout()

        self.row_label = QLabel("Enter row key")
        self.column_label = QLabel("Enter column key")
        self.row_edit = QLineEdit()
        self.column_edit = QLineEdit()
        self.message_label = QLabel("Enter message")
        self.message_edit = QLineEdit()
        self.radiobutton_label = QLabel("Check action")
        self.code_radiobutton = QRadioButton("coding")
        self.decode_radiobutton = QRadioButton("decoding")
        self.run_button = QPushButton("O K")

        self.table1 = QTableWidget()
        self.table2 = QTableWidget()
        self.table3 = QTableWidget()
        self.result_label = QLabel()

        self.run_button.clicked.connect(self.run)

        self.__pack_widgets()
        self.resize(600, 200)
        self.setWindowTitle('Encryption method "Double transposition"')

    def __pack_widgets(self):
        # pack part of widgets which for entering data
        self.data_part.addWidget(self.row_label, 0, 0)
        self.data_part.addWidget(self.column_label, 0, 1)
        self.data_part.addWidget(self.row_edit, 1, 0)
        self.row_edit.setFixedWidth(150)
        self.data_part.addWidget(self.column_edit, 1, 1)
        self.column_edit.setFixedWidth(150)
        self.data_part.addWidget(self.message_label, 2, 0, 1, 2)
        self.message_label.setAlignment(Qt.AlignCenter)
        self.data_part.addWidget(self.message_edit, 3, 0, 1, 2, Qt.AlignCenter)
        self.message_edit.setFixedWidth(300)
        self.data_part.addWidget(self.radiobutton_label, 4, 0, 1, 2)
        self.radiobutton_label.setAlignment(Qt.AlignCenter)
        self.data_part.addWidget(self.code_radiobutton, 5, 0)
        self.data_part.addWidget(self.decode_radiobutton, 5, 1)
        self.data_part.addWidget(self.run_button, 6, 0, 1, 2, Qt.AlignCenter)
        self.run_button.setFixedWidth(150)
        # pack tables
        self.table_part.addWidget(self.table1)
        self.table_part.addWidget(self.table2)
        self.table_part.addWidget(self.table3)
        # pack main layers
        self.base_layer.addLayout(self.data_part)
        self.result_layer.addLayout(self.table_part)
        self.result_layer.addWidget(self.result_label)
        self.widget.setLayout(self.base_layer)

    def run(self):
        row_key = self.row_edit.text()
        column_key = self.column_edit.text()
        row_length = len(row_key)
        column_length = len(column_key)
        if row_length == 0 or column_length == 0:
            QMessageBox.warning(self.widget, "Warning", "Enter key.")
        elif row_length != column_length:
            QMessageBox.warning(self.widget, "Warning",
                                "Wrong key! Row and column key must have equal count of numbers.")
        else:
            message = self.message_edit.text()
            message_length = len(message)
            if message_length:
                row_key = split_edit(self.row_edit.text(), ' ')
                column_key = split_edit(self.column_edit.text(), ' ')
                size = len(row_key)
                if message_length <= size * len(column_key):
                    sorted_row_key = sorted(row_key)
                    sorted_column_key = sorted(column_key)
                    source_matrix = create_matrix_message(size, message)
                    if self.code_radiobutton.isChecked():
                        self.base_layer.addLayout(self.result_layer)  # show layer with tables
                        result = code(source_matrix, str_list_to_int(column_key), str_list_to_int(row_key))
                        # Full source message in table
                        self.__full_table(self.table1, source_matrix, size, row_key, column_key)
                        # Full table with sorting columns
                        self.__full_table(self.table2, result[0], size, row_key, sorted_column_key)
                        # Full table with sorting rows and columns
                        self.__full_table(self.table3, result[1], size, sorted_row_key, sorted_column_key)
                        self.result_label.setText("Ciphertext: " + str(result[2]))
                    elif self.decode_radiobutton.isChecked():
                        self.base_layer.addLayout(self.result_layer)  # show layer with tables
                        result = decode(source_matrix, str_list_to_int(column_key), str_list_to_int(row_key))
                        # Full source message in table
                        self.__full_table(self.table1, source_matrix, size, sorted_row_key, sorted_column_key)
                        # Full table with sorting rows
                        self.__full_table(self.table2, result[0], size, row_key, sorted_column_key)
                        # Full table with sorting columns and rows
                        self.__full_table(self.table3, result[1], size, row_key, column_key)
                        self.result_label.setText("Source text: " + str(result[2]))
                    else:
                        QMessageBox.warning(self.widget, "Warning", "Chose action.")
                else:
                    QMessageBox.warning(self.widget, "Warning", "Long message.")
            else:
                QMessageBox.warning(self.widget, "Warning", "Enter message.")

    @staticmethod
    def __full_table(table, data, size, vertical_header, horizontal_header):
        """
        :param table: QTableWidget
        :param data: list - double list
        :param vertical_header: list
        :param horizontal_header: list
        :return: void
        """
        def full_data():
            """
            Full QTableWidget
            """
            for i in range(size):
                for j in range(size):
                    value = data[i][j]
                    if type(value) is not str:
                        value = str(value)
                    table.setItem(i, j, QTableWidgetItem(value))

        table.setRowCount(size)
        table.setColumnCount(size)
        table.setVerticalHeaderLabels(vertical_header)
        table.setHorizontalHeaderLabels(horizontal_header)
        full_data()
        table.resizeColumnsToContents()
