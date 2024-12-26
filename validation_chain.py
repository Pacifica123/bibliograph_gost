from flask import flash

class Validator:
    def __init__(self):
        self.errors = []

    def validate(self, data):
        self.validate_authors(data.get('authors'))
        self.validate_title(data.get('title'))
        self.validate_year(data.get('year'), data.get('type'))
        self.validate_place(data.get('place'), data.get('type'))
        self.validate_url(data.get('url'), data.get('type'))
        self.validate_access_date(data.get('access_date'), data.get('type'))

        if self.errors:
            flash("Ошибки в форме: " + ", ".join(self.errors), "error")
            return False
        return True

    def validate_authors(self, authors):
        if not authors or not isinstance(authors, str) or len(authors.split(',')) == 0:
            self.errors.append("Авторы не могут быть пустыми")

    def validate_title(self, title):
        if not title:
            self.errors.append("Название не может быть пустым")

    def validate_year(self, year, source_type):
        if source_type == 'printed' and year:
            if not year.isdigit():
                self.errors.append("Год издания должен быть числом")

    def validate_place(self, place, source_type):
        if source_type == 'printed' and place is not None and place.strip() == "":
            # Место может быть пустым
            pass

    def validate_url(self, url, source_type):
        if source_type == 'electronic' and (not url or not url.startswith("http")):
            self.errors.append("URL должен начинаться с 'http' или 'https'")

    def validate_access_date(self, access_date, source_type):
        if source_type == 'electronic' and access_date is None:
            # Дата доступа может быть пустой
            pass
