from PIL import Image, ImageEnhance, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap

app = QApplication([])

class Window(QWidget):

    def SaveIMG(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self,"Save Image", "", "Image Files (*.jpg)", options=options)
        if file_name:
            self.gray_image.save(file_name)

    def ToGray(self):
        big_org_img = Image.open(self.file_name)
        self.gray_image = big_org_img.convert("L")
        smol_gray_image= self.gray_image.resize((250,250), Image.ANTIALIAS)
        smol_gray_image.save("fastgrayimg.jpg")
        pixmap = QPixmap("Zde vložte cestu pro krátkodobé ukládání obrázků/fastgrayimg.jpg")
        self.smol_con_img.setPixmap(pixmap)
        self.bt_save.setEnabled(True)

    def ShowIMG(self):
        big_org_img = Image.open(self.file_name)
        smol_org_img = big_org_img.resize((250,250), Image.ANTIALIAS)
        smol_org_img.save("fastsave.jpg")
        pixmap = QPixmap("Zde vložte cestu pro krátkodobé ukládání obrázků/fastsave.jpg")
        self.smol_org_img.setPixmap(pixmap)
        self.bt_con.setEnabled(True)
    

    def OpenIMG(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.jpg)", options=options)
        if file_name:
            self.file_name = file_name
            self.ShowIMG()


    def __init__(self):
        super(Window, self).__init__()
        #Button na otevření obrázku
        self.bt_open = QPushButton("Open Picture", self)
        self.bt_open.clicked.connect(self.OpenIMG)

        #Button na konverzi
        self.bt_con = QPushButton("Convert", self)
        self.bt_con.clicked.connect(self.ToGray)
        self.bt_con.setEnabled(False)

        #Button na save
        self.bt_save = QPushButton("Save Picture", self)
        self.bt_save.clicked.connect(self.SaveIMG)
        self.bt_save.setEnabled(False)

        #Originální image
        self.smol_org_img = QLabel(self)
        self.smol_org_img.setFixedSize(250, 250)

        #Converted image 
        self.smol_con_img = QLabel(self)
        self.smol_con_img.setFixedSize(250, 250)

        #Rozložení okna
        hbox = QHBoxLayout()
        hbox.addWidget(self.bt_open)
        hbox.addWidget(self.bt_con)
        hbox.addWidget(self.bt_save)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.smol_org_img)
        vbox.addWidget(self.smol_con_img)
        
        self.setWindowTitle("Convertor to BW")
        self.setLayout(vbox)
        self.show()








Window = Window()
Window.show()
app.exec_()
