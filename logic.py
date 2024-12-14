from PyQt6.QtWidgets import *
from gui import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import csv
import os

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.hide_buttons()
        self.button_savefile.clicked.connect(self.save_file)
        self.combo_fonts.currentIndexChanged.connect(self.change_font)
        self.combo_color.currentIndexChanged.connect(self.change_color)
        self.text_size_edit.valueChanged.connect(self.change_size)
        self.button_bold.clicked.connect(self.change_bold)
        self.button_italic.clicked.connect(self.change_italic)
        self.bold_count = 0
        self.italic_count = 0

    def apply_format(self, format_val) -> None:
        '''
        This method will select the entire main_text and apply the formatting to it.
        :param format_val:
        :return:
        '''
        text_select = self.main_text.textCursor()
        text_select.select(QTextCursor.SelectionType.Document)
        text_select.mergeCharFormat(format_val)
        self.main_text.setTextCursor(text_select)

    def change_font(self) -> None:
        '''
        This method collects the selected font from combo_fonts and sends it to apply_format() for the
        formatting to be applied to selected text.
        :return:
        '''
        font = self.combo_fonts.currentText()
        format_val = QTextCharFormat()
        format_val.setFontFamily(font)
        self.apply_format(format_val)

    def change_color(self) -> None:
        '''
        This method collects the selected color from combo_fonts and sends it to apply_format() to be
        applied to selected text.
        :return:
        '''
        color_name = self.combo_color.currentText()
        format_val = QTextCharFormat()
        format_val.setForeground(QColor(color_name))
        self.apply_format(format_val)

    def change_size(self) -> None:
        '''
        This method collects the chosen font number from the text_size_edit Qspinbox and then sends it
        to apply_fromat() to be applied to selected text.
        :return:
        '''
        font_size = self.text_size_edit.value()
        format_val = QTextCharFormat()
        format_val.setFontPointSize(font_size)
        self.apply_format(format_val)

    def change_bold(self) -> None:
        '''
        This method changes the boldness of the selected text using a count system to count how many
        times the button has been pressed to determine if it needs to bold or unbold selected text. Then
        it sends it to apply_format() to be applied to selected text.
        :return:
        '''
        format_val = QTextCharFormat()
        self.bold_count += 1

        if self.bold_count % 2 == 0:
            format_val.setFontWeight(QFont.Weight.Normal)
        else:
            format_val.setFontWeight(QFont.Weight.Bold)

        self.apply_format(format_val)

    def change_italic(self) -> None:
        '''
        This method changes the italics of the text using a count system to count how many times the
        button has been pressed to determine if it needs to italisize or unitalisize the selected text.
        Then, it sends it to apply_format() to be applied to selected text.
        :return:
        '''
        format_val = QTextCharFormat()
        self.italic_count += 1
        if self.italic_count % 2 == 0:
            format_val.setFontItalic(False)
        else:
            format_val.setFontItalic(True)
        self.apply_format(format_val)

    def hide_buttons(self) -> None:
        '''
        This method sets the label, button_y, and button_n to not visible so that the interface is not
        confusing.
        :return:
        '''
        self.button_n.setVisible(False)
        self.button_y.setVisible(False)
        self.label_save.setVisible(False)

    def show_buttons(self) -> None:
        '''
        This method shows the label, button_y, and button_n to visible so that the user can see error
        messages with their save file and also choose to overwrite a file.
        :return:
        '''
        self.button_n.setVisible(True)
        self.button_y.setVisible(True)
        self.label_save.setVisible(True)

    def write_data(self) -> None:
        '''
        This method collects the title value and the text and writes/overwrites it to a file. Then, it
        hides any buttons that appeared.
        :return:
        '''

        text_data = self.main_text.toPlainText()
        title = self.input_name.text()

        with open(title, 'w', newline='') as write_file:
            content = csv.writer(write_file)
            content.writerow([text_data])

        self.hide_buttons()


    def overwrite_no(self) -> None:
        '''
        This method updates the label to tell the user to put in a new title. This is called when the user
        decides not to overwrite their file.
        :return:
        '''
        self.label_save.setText("Enter new title.")

    def save_file(self) -> None:
        '''
        This method collects the title and checks if it is unnamed, then it checks if the file exists. If
        the file exists, it will show the buttons and ask if the user wants to overwrite the file. Then it
        sends it to write_file() to be written.
        :return:
        '''

        title = self.input_name.text()

        if title == '':
            self.show_buttons()
            self.label_save.setText("Enter title.")
        else:

            if os.path.isfile(title):
                self.show_buttons()
                self.label_save.setText("File exists. Overwrite?")
                self.button_y.clicked.connect(self.write_data)
                self.button_n.clicked.connect(self.overwrite_no)
            else:
                self.write_data()



