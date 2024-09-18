class Functions():
    def __init__(self, ui):
        self.ui = ui
        self.connect_all()

    def connect_all(self):
        self.ui.pushButton.clicked.connect(self.add)

    def add(self):
        txt_one = self.ui.lineEdit.text()
        txt_two = self.ui.lineEdit_2.text()
        if txt_one.isdigit and txt_two.isdigit():
            sum = int(txt_one) + int(txt_two)
            self.ui.textBrowser.setText(str(sum))
        else:
            self.ui.textBrowser.setText('Na')
