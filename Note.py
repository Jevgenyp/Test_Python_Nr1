
import json
import datetime
import csv
from collections import OrderedDict
class NoteClass:
    def __init__(self, id, title, text):
        self.id = id
        self.title = title
        self.text = text
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def to_dict(self):
        return OrderedDict([
            ("id", self.id),
            ("title", self.title),
            ("text", self.text),
            ("created_at", self.created_at.strftime("%Y-%m-%d %H:%M:%S")),
            ("updated_at", self.updated_at.strftime("%Y-%m-%d %H:%M:%S"))
        ])