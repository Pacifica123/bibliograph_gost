# PRINTED_FIELDS = [
#     # {"name": "authors", "label": "Авторы (через запятую):", "required": True},
#     {"name": "title", "label": "Название книги:", "required": True},
#     {"name": "place", "label": "Место издания:", "required": False},
#     {"name": "publisher", "label": "Издательство:", "required": False},
#     {"name": "year", "label": "Год издания:", "required": False},
#     {"name": "edition_number", "label": "Номер издания:", "required": False, "type": "number"},
#     {"name": "page_count", "label": "Количество страниц:", "required": False, "type": "number"},
# ]

# ELECTRONIC_FIELDS = [
#     # {"name": "authors", "label": "Авторы (через запятую):", "required": True},
#     {"name": "title", "label": "Название статьи:", "required": True},
#     {"name": "journal", "label": "Научный журнал:", "required": False},
#     {"name": "publication_year", "label": "Год публикации:", "required": False},
#     {"name": "url", "label": "URL:", "required": True},
#     {"name": "access_date", "label": "Дата доступа:", "required": True, "type": "date"},
# ]
# Поля для электронных и печатных ресурсов
FIELDS = {
    "electronic": {
        "selector": {
            "name": "electronic_type",
            "label": "Тип ресурса:",
            "options": [
                {"value": "journal", "label": "Журнал"},
                {"value": "web", "label": "Веб-сайт"}
            ]
        },
        "journal": [
            {"authors": {
                    "label": "Авторы:",
                    "fields": [
                        {"name": "authors_surname[]", "placeholder": "Фамилия", "required": True},
                        {"name": "authors_name[]", "placeholder": "Имя", "required": True},
                        {"name": "authors_patronymic[]", "placeholder": "Отчество", "required": False}
                    ]
                }
            },
            {"name": "title", "label": "Название статьи:", "required": False},
            {"name": "journal", "label": "Название журнала:", "required": True},
            {"name": "publication_year", "label": "Год издания:", "required": True, "type": "number"},
            {"name": "publication_date", "label": "Дата публикации:", "required": True, "type": "date"},
            {"name": "url", "label": "URL:", "required": True},
        ],
        "web": [
            {"name": "site_name", "label": "Название сайта:", "required": True},
            {"name": "title", "label": "Название статьи на сайте:", "required": False},
            {"name": "url", "label": "URL:", "required": True},
            {"name": "access_date", "label": "Дата доступа:", "required": True, "type": "date"},
        ],

    },
    "printed": {
        "authors": {
            "label": "Авторы:",
            "fields": [
                {"name": "authors_surname[]", "placeholder": "Фамилия", "required": True},
                {"name": "authors_name[]", "placeholder": "Имя", "required": True},
                {"name": "authors_patronymic[]", "placeholder": "Отчество", "required": False}
            ]
        },
        "fields": [
            {"name": "title", "label": "Название:", "required": True},
            {"name": "publisher", "label": "Издатель:", "required": True},
            {"name": "year", "label": "Год издания:", "required": True, "type": "number"}
        ]
    }
}
