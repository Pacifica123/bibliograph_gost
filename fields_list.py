PRINTED_FIELDS = [
    # {"name": "authors", "label": "Авторы (через запятую):", "required": True},
    {"name": "title", "label": "Название книги:", "required": True},
    {"name": "place", "label": "Место издания:", "required": False},
    {"name": "publisher", "label": "Издательство:", "required": False},
    {"name": "year", "label": "Год издания:", "required": False},
    {"name": "edition_number", "label": "Номер издания:", "required": False, "type": "number"},
    {"name": "page_count", "label": "Количество страниц:", "required": False, "type": "number"},
]

ELECTRONIC_FIELDS = [
    # {"name": "authors", "label": "Авторы (через запятую):", "required": True},
    {"name": "title", "label": "Название статьи:", "required": True},
    {"name": "journal", "label": "Научный журнал:", "required": False},
    {"name": "publication_year", "label": "Год публикации:", "required": False},
    {"name": "url", "label": "URL:", "required": True},
    {"name": "access_date", "label": "Дата доступа:", "required": True, "type": "date"},
]
