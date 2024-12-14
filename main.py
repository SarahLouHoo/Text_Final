from logic import *

def main():
    application = QApplication([])
    window = Logic()
    window.show()
    window.setWindowTitle("Text Editor")
    application.exec()

if __name__ == '__main__':
    main()