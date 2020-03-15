"""
Png to Ico
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from PIL import Image
import random
import os


class Png2Ico(toga.App):

    def startup(self):
        self.msg = '请开始操作'
        main_box = toga.Box(style=Pack(direction=COLUMN))
        img_path_box = toga.Box(style=Pack(direction=ROW))
        labelPath = toga.Label(
            '请选择文件',
            style=Pack(padding=(5, 5))
        )
        self.labelMsg = toga.Label(
            self.msg,
            style=Pack(padding=(5, 5))
        )
        buttonDir = toga.Button(
            '选择图像',
            on_press=self.select_png,
            style=Pack(padding=5)
        )
        buttonExec = toga.Button(
            '执行转换',
            on_press=self.png_to_ico,
            style=Pack(padding=5)
        )
        self.dirInput = toga.TextInput(style=Pack(flex=1), readonly=True)
        img_path_box.add(labelPath)
        img_path_box.add(buttonDir)
        img_path_box.add(self.dirInput)
        main_box.add(img_path_box)
        main_box.add(self.labelMsg)
        main_box.add(buttonExec)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def select_png(self, widget):
        try:
            pngPath_ = self.main_window.open_file_dialog(
                '请选择png图片', file_types="(*.png)|*.png")
            if pngPath_:
                if pngPath_.split('.').pop() == 'png':
                    self.pngPath = pngPath_
                    self.msg = '已成功选择图片！转换后将保存到相同目录！'
                else:
                    self.msg = '请选择png格式的图片！'
                    self.pngPath = ''
        except Exception as e:
            self.pngPath = ''
        self.labelMsg.text = self.msg
        self.dirInput.value = self.pngPath

    def png_to_ico(self, widget):
        try:
            self.pngPath
            goOn = 1
            if self.dirInput.value == self.pngPath:
                goOn = 1
            else:
                goOn = 0
        except Exception:
            goOn = 0
        if goOn and os.path.exists(self.pngPath):
            if self.pngPath:
                preList_ = self.pngPath.split('\\')
                preList_.pop()
                self.saveDir = '\\'.join(preList_)+'\\'
                self.msg = '成功选择存储路径,转换中...'
                goOn = 1
            else:
                self.msg = '存储路径不存在'
                goOn = 0
            self.labelMsg.text = self.msg
            if goOn == 1:
                toIco = Image.open(self.pngPath)
                toIco.save(self.saveDir+'transfromed' +
                           str(random.randint(10000, 99999)) + '.ico')
                self.msg = '转换成功！'
            else:
                pass
        else:
            self.msg = '操作路径不存在,请重新选择！'
        self.labelMsg.text = self.msg


def main():
    return Png2Ico()
