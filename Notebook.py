import json
import datetime
import csv
from collections import OrderedDict
from Note import NoteClass
class NotebookClass:
    def __init__(self):
        self.notes = []
        self.id_counter = 1

    def add_note(self, title, text):
        note = NoteClass(self.id_counter, title, text)
        self.notes.append(note)
        self.id_counter += 1
        print("Заметка добавлена")

    def view_notes(self):
        for note in self.notes:
            print(note.to_dict())

    def edit_note(self, id, new_title, new_text):
        for note in self.notes:
            if note.id == id:
                note.title = new_title
                note.text = new_text
                note.updated_at = datetime.datetime.now()
                print("Заметка обновлена")
                return
        print("Заметка не найдена")

    def delete_note(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                print("Заметка удалена")
                return
        print("Заметка не найдена")

    def save_to_file(self, filename, format):
        if format == "json":
            with open(filename, "w") as f:
                json.dump([note.to_dict() for note in self.notes], f)
        elif format == "csv":
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow(["id", "title", "text", "created_at", "updated_at"])
                for note in self.notes:
                    writer.writerow(note.to_dict().values())
        else:
            print("Неверный формат файла")