import sys
from PySide.QtGui import QApplication
from src.view.Window import Window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wid = Window()
    wid.show()
    # mainloop
    sys.exit(app.exec_())
# print(code(full_table(4, "прилетаювосьмого"), [4, 1, 3, 2], [3, 1, 4, 2]))
# print(code(full_table(5, "invalidfunctionresulttype"), [1, 2, 3, 5, 4], [2, 3, 5, 4, 1]))

# print(decode(full_table(5, "epyatreiiftneidtonis'ah'c"), [4, 5, 3, 2, 1], [5, 4, 1, 3, 2]))
# print(decode(full_table(4, "азюже_сшгтооипер"), [2, 4, 1, 3], [4, 1, 2, 3]))

