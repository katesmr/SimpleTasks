from PySide.QtGui import QTableWidget, QTableWidgetItem


class MTable(QTableWidget):
    def __init__(self, data, header_vertical_data=None, header_horizontal_data=None):
        super().__init__()
        self.data = data
        self.height = len(data)
        self.setRowCount(self.height)
        self.width = len(data[0])
        self.setColumnCount(self.width)
        self.header_vertical_data = header_vertical_data
        self.header_horizontal_data = header_horizontal_data
        self.full_table()

    def update_table(self):
        pass

    def full_header(self):
        if self.header_vertical_data:
            # increase column count (consider additional column for header)
            # self.width += 1
            self.setVerticalHeaderLabels(self.header_vertical_data)
            # fulling of table will begin from second column
            # self.begin_column = 1
        if self.header_horizontal_data:
            # increase row count (consider additional row for header)
            # self.height += 1
            self.setHorizontalHeaderLabels(self.header_horizontal_data)
            # fulling of table will begin from second row
            # self.begin_row = 1

    def full_data(self):
        for i in range(self.height):
            for j in range(self.width):
                value = self.data[i][j]
                if type(value) is not str:
                    value = str(value)
                self.setItem(i, j, QTableWidgetItem(value))

    def full_table(self):
        self.full_header()
        self.full_data()

# t = MTable(full_table(4, "азюже_сшгтооипер"), ['2', '4', '1', '3'], ['4', '1', '2', '3'])

