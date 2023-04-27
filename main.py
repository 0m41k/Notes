#import
from PyQt5.QtWidgets import (
    QLabel, QPushButton, QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QListWidget, QTextEdit, QLineEdit, QInputDialog
)
import json
#import

#показ заметок
def show_note():
    key = list_notes.selectedItems()[0].text()
    note_field.setText(notes[key]['text'])
    list_tags.clear()
    list_tags.addItems(notes[key]['tags'])
#показ заметок

#загрузка первой заметки
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        list_notes.addItems(notes)
        return notes
    except:
        notes = {
            'Приветственная заметка': {
                'text': 'Это ваша первая заметка в программе!',
                'tags': ['Начало работы' , 'Первый запуск']
            }
        }
        with open('notes.json', 'w') as file:
            json.dump(notes, file)
        list_notes.addItems(notes)
        return notes
#загрузка первой заметки

#добавления заметок
def add_note():
    note_name, result = QInputDialog.getText(window, "Добавить заметку", "Название заметки:")
    if result and len(note_name) > 0:
        notes[note_name] = {
            'text': '',
            'tags': []
        }
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['tags'])
#добавления заметок

#удаление заметок
def del_notes():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        note_field.clear()
        list_notes.addItems(notes)
        with open('notes.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
#удаление заметок

#Удаление всех заметок
def del_all_notes():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['tags'].remove(tag)
        notes[key]['text'].remove(tag)
        with open('notes.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)

#Удаление всех заметок

#сохранение заметок
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['text'] = note_field.toPlainText()
        with open('notes.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
#сохранение заметок

#прикрепление тегов
def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['tags'] and len(tag) > 0:
            notes[key]['tags'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
            with open('notes.json', 'w') as file:
                json.dump(notes, file, sort_keys=True)
#прикрепление тегов

#открепление тегов
def remove_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['tags'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['tags'])
        with open('notes.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
#открепление тегов

#поиск по тегу
def search_by_tag():
    tag = field_tag.text()
    if btn_search_by_tag.text() != 'Сбросить поиск' and len(tag) > 0:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['tags']:
                notes_filtered[note] = notes[note]
        list_notes.clear()
        list_tags.clear()
        note_field.clear()
        list_notes.addItems(notes_filtered)
        btn_search_by_tag.setText('Сбросить поиск')
    else:
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        note_field.clear()
        list_notes.addItems(notes)
        btn_search_by_tag.setText('Искать заметки по тегу')
#поиск по тегу

#создание виджетов
app = QApplication([])
window = QWidget()

note_field = QTextEdit()
lbl_note = QLabel('Список заметок')
list_notes = QListWidget()

btn_creat_note = QPushButton('Добавить заметку')
btn_delete_note = QPushButton('Удалить заметку')
btn_save_note = QPushButton('Сохранить заметку')
btn_delete_all_note = QPushButton('Удалить все заметки')

lbl_tag = QLabel('Список тегов')
list_tags = QListWidget()
field_tag = QLineEdit()

btn_add_tag = QPushButton('Добавить к заметке')
btn_remove_tag = QPushButton('Открепить от заметки')
btn_search_by_tag = QPushButton('Искать заметки по тегу')
#создание виджетов

#создание лэйаутов
h_main = QHBoxLayout()
left_layout = QVBoxLayout()
right_layout = QVBoxLayout()

h_1 = QHBoxLayout()
h_2 = QHBoxLayout()
h_3 = QHBoxLayout()
h_4 = QHBoxLayout()
h_5 = QHBoxLayout()
h_6 = QHBoxLayout()
h_7 = QHBoxLayout()
h_8 = QHBoxLayout()
h_9 = QHBoxLayout()
h_10 = QHBoxLayout()
#создание лэйаутов

#размещение виджетов на лэйаутах
h_1.addWidget(lbl_note)
h_2.addWidget(list_notes)
h_3.addWidget(btn_creat_note)
h_3.addWidget(btn_delete_note)

h_4.addWidget(btn_save_note)
h_5.addWidget(lbl_tag)
h_6.addWidget(list_tags)
h_7.addWidget(field_tag)
h_8.addWidget(btn_add_tag)
h_8.addWidget(btn_remove_tag)
h_9.addWidget(btn_search_by_tag)
h_10.addWidget(btn_delete_all_note)


right_layout.addLayout(h_1)

right_layout.addLayout(h_2)
right_layout.addLayout(h_3)
right_layout.addLayout(h_4)
right_layout.addLayout(h_5)
right_layout.addLayout(h_6)
right_layout.addLayout(h_7)
right_layout.addLayout(h_8)
right_layout.addLayout(h_9)
right_layout.addLayout(h_10)

left_layout.addWidget(note_field)

h_main.addLayout(left_layout)
h_main.addLayout(right_layout)
#размещение виджетов на лэйаутах

#настройка приложения
window.setWindowTitle('Умные заметки')
window.resize(900, 600)
field_tag.setPlaceholderText('Введите тег...')
window.setLayout(h_main)
#настройка приложения

#обработка событий
notes = load_notes()
list_notes.itemClicked.connect(show_note)
btn_creat_note.clicked.connect(add_note)
btn_save_note.clicked.connect(save_note)
btn_delete_note.clicked.connect(del_notes)
btn_add_tag.clicked.connect(add_tag)
btn_remove_tag.clicked.connect(remove_tag)
btn_search_by_tag.clicked.connect(search_by_tag)
btn_delete_all_note.clicked.connect(del_all_notes)
#обработка событий

#запуск приложения
window.show()
app.exec()
#запуск приложения

