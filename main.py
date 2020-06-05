import shutil
import sys

import pytesseract
from PyQt5 import QtWidgets, QtGui
import design

import os
from PIL import Image
from PyQt5.QtWidgets import QFileDialog
from pytesseract import image_to_string
from gtts import gTTS

import speech_recognition as sr

from pydub import AudioSegment
from pydub.silence import split_on_silence
from docx import Document

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.toolButton_browse.clicked.connect(self.browse_file)
        self.pushButton_convert.clicked.connect(self.convert)
        self.pushButton_save_doc.clicked.connect(self.save_doc)

        self.comboBox_lang.addItems(["", "arab", "eng", "rus"])

    def clear_choice(self):
        self.lineEdit_path.setText("")
        self.lineEdit_page.setText("")
        self.buttonGroup.setExclusive(False)
        self.radioButton_pdf_to_txt.setChecked(False)
        self.radioButton_txt_to_speech.setChecked(False)
        self.radioButton_speech_to_txt.setChecked(False)
        self.buttonGroup.setExclusive(True)

    def choice_service(self):
        if self.radioButton_pdf_to_txt.isChecked():
            if len(self.lineEdit_path.text()) == 0:
                self.create_msg_box('/chooce_file.html', 'تنبيه', QtWidgets.QMessageBox.Ok, '/msg_chooce_file.png')
            elif self.get_dir_file()[1].endswith('.pdf') and self.lineEdit_page.text() == "":
                self.create_msg_box('/pages.html', 'تنبيه', QtWidgets.QMessageBox.Ok, '\\msg_pages.png')
            else:
                self.pdf_to_txt()
                self.clear_choice()
        elif self.radioButton_txt_to_speech.isChecked():
            if len(self.textEdit.toPlainText()) == 0:
                self.create_msg_box('/text_to_conv.html', 'تنبيه', QtWidgets.QMessageBox.Ok, '/msg_text_to_conv.png')
            else:
                self.txt_to_mp3()
                self.clear_choice()
        elif self.radioButton_speech_to_txt.isChecked():
            if len(self.lineEdit_path.text()) == 0:
                self.create_msg_box('/chooce_file.html', 'تنبيه', QtWidgets.QMessageBox.Ok, '/msg_chooce_file.png')
            else:
                self.wav_to_txt()
                self.clear_choice()

    def change_lang(self):
        lang = ""
        arab = ["ara", "ar", "ar-SA"]
        eng = ["eng", "en", "en-US"]
        rus = ["rus", "ru", "ru-RU"]
        if self.comboBox_lang.currentText() == "arab":
            if self.radioButton_pdf_to_txt.isChecked():
                lang = arab[0]
            elif self.radioButton_txt_to_speech.isChecked():
                lang = arab[1]
            elif self.radioButton_speech_to_txt.isChecked():
                lang = arab[2]
        elif self.comboBox_lang.currentText() == "eng":
            if self.radioButton_pdf_to_txt.isChecked():
                lang = eng[0]
            elif self.radioButton_txt_to_speech.isChecked():
                lang = eng[1]
            elif self.radioButton_speech_to_txt.isChecked():
                lang = eng[2]
        elif self.comboBox_lang.currentText() == "rus":
            if self.radioButton_pdf_to_txt.isChecked():
                lang = rus[0]
            elif self.radioButton_txt_to_speech.isChecked():
                lang = rus[1]
            elif self.radioButton_speech_to_txt.isChecked():
                lang = rus[2]
        return lang

    def browse_file(self):
        if self.comboBox_lang.currentText() == "":
            self.create_msg_box('/chooce_lang.html', 'تنبيه', QtWidgets.QMessageBox.Ok, '/msg_chooce_lang.png')
        else:
            self.lineEdit_path.setText("")
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getOpenFileName(self, "فتح الملف", "",
                                                       "All Files (*);;", options=options)
            self.lineEdit_path.setText(file_name)

    def get_dir_file(self):
        dir, file = os.path.split(self.lineEdit_path.text())
        return dir, file

    def convert(self):
        if self.radioButton_txt_to_speech.isChecked() and self.comboBox_lang.currentText() == "":
            self.create_msg_box('/chooce_lang.html', 'تنبيه', QtWidgets.QMessageBox.Ok, '/msg_chooce_lang.png')
        else:
            self.choice_service()

    def pdf_to_txt(self):
        os.chdir(self.get_dir_file()[0])
        if self.get_dir_file()[1].endswith('.pdf'):
            os.system(
                'convert -resize 85% -quality 100 -density 300 -background white -alpha remove {}[{}] 1.jpg'.format(
                    self.get_dir_file()[1], self.lineEdit_page.text()))
        text = ""
        for file_name in os.listdir(self.get_dir_file()[0]):
            if file_name.endswith('.jpg'):
                image = Image.open(file_name, mode='r')
                result = image_to_string(image, lang=self.change_lang())
                text += result
                os.remove(file_name)
        self.textEdit.setText(text)

    def txt_to_mp3(self):
        self.save_file_dialog()
        os.chdir(self.get_dir_file()[0])
        text = self.textEdit.toPlainText()
        myobj = gTTS(text=text, lang=self.change_lang(), slow=False)
        myobj.save(self.get_dir_file()[1])

    def wav_to_txt(self):

        sound = AudioSegment.from_file(self.lineEdit_path.text(), format="wav")
        chunks = split_on_silence(sound, min_silence_len=1000, silence_thresh=-40, keep_silence=500)  # -40
        new_folder = self.get_dir_file()[0] + '/del_it'
        os.mkdir(new_folder)
        os.chdir(new_folder)
        for i, chunk in enumerate(chunks):
            chunk.export(str(i) + ".wav", bitrate='320k', format="wav")
        r = sr.Recognizer()
        filelist = os.listdir(new_folder)
        filelist = sorted(filelist, key=lambda x: int(os.path.splitext(x)[0]))
        result = ""
        for file_name in filelist:
            if file_name.endswith('.wav'):
                with sr.AudioFile(file_name) as source:
                    audio = r.record(source)
                try:
                    text = r.recognize_google(audio, language=self.change_lang())
                    t = text + '\n'
                    result += t
                except sr.UnknownValueError:
                    pass
                except ConnectionResetError:
                    pass
                except sr.RequestError:
                    pass
        os.chdir(self.get_dir_file()[0])
        shutil.rmtree(new_folder)
        self.textEdit.setText(result)

    def save_doc(self):
        document = Document()
        text = self.textEdit.toPlainText()
        document.add_paragraph(text)
        document.add_page_break()
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getSaveFileName(self, "حفظ الملف", ".docx",
                                                       "All Files (*);", options=options)
            document.save(file_name)
        except Exception:
            pass

    def save_file_dialog(self):
        self.lineEdit_path.setText("")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "حفظ الملف", ".mp3",
                                                   "All Files (*);", options=options)
        self.lineEdit_path.setText(file_name)
        # return file_name

    def create_msg_box(self, html, title, button, image):
        data_dir = os.getcwd() + '/msgs'
        with open(data_dir + html, 'r', encoding="utf-8") as f:
            content = f.read()
        msg = QtWidgets.QMessageBox(self)
        data_dir = os.getcwd() + '/imgs'
        if image:
            msg.setIconPixmap(QtGui.QIcon(data_dir + image).pixmap(65))
        else:
            pass
        msg.setWindowTitle(title)
        msg.setText(content)
        msg.setStandardButtons(button)
        message = msg.exec_()
        return message


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
