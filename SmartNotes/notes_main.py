from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QLineEdit, QTextEdit, QListWidget
)

# Создание виджетов
app = QApplication([])
window = QWidget()
note_field = QTextEdit()
notes_list = QListWidget()
tags_list = QListWidget()
btn_create_note = QPushButton('Создать заметку')
btn_delete_note = QPushButton('Удалить заметку')
btn_save_note = QPushButton('Сохранить заметку')
btn_add_tag = QPushButton('Добавить к заметке')
btn_remove_tag = QPushButton('Открепить от заметки')
btn_search_by_tag = QPushButton('Искать заметки по тегу')
lbl_for_notes = QLabel('Список заметок:')
lbl_for_tags = QLabel('Список тегов:')
search_tag_field = QLineEdit()
# Создание виджетов

# Создание лэйаутов
main_layout = QHBoxLayout()

left_side = QVBoxLayout()
right_side = QVBoxLayout()

h_1 = QHBoxLayout()
h_2 = QHBoxLayout()
h_3 = QHBoxLayout()
h_4 = QHBoxLayout()
h_5 = QHBoxLayout()
h_6 = QHBoxLayout()
h_7 = QHBoxLayout()
h_8 = QHBoxLayout()
h_9 = QHBoxLayout()
# Создание лэйаутов