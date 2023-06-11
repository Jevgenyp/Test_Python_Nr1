from Notebook import NotebookClass
import Notebook
import json
import datetime
import csv
from collections import OrderedDict

def main():
    notebook = NotebookClass()

    while True:
        action = input("Введите действие (add, view, edit, delete, save, quit): ")
        if action == "add":
            title = input("Введите заголовок заметки: ")
            text = input("Введите текст заметки: ")
            notebook.add_note(title, text)
        elif action == "view":
            notebook.view_notes()
        elif action == "edit":
            id = int(input("Введите ID заметки: "))
            new_title = input("Введите новый заголовок: ")
            new_text = input("Введите новый текст: ")
            notebook.edit_note(id, new_title, new_text)
        elif action == "delete":
            id = int(input("Введите ID заметки: "))
            notebook.delete_note(id)
        elif action == "save":
            filename = input("Введите имя файла: ")
            format = input("Введите формат файла (json, csv): ")
            notebook.save_to_file(filename, format)
        elif action == "quit":
            break
        else:
            print("Неправильная команда")

if __name__ == "__main__":
    main()