from datetime import datetime


def format_date(date_str):
    """Форматирует дату из формата 'YYYY-MM-DD' в 'DD.MM.YYYY'."""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return date_str


# def format_authors(authors):
#     """Форматирование авторов по ГОСТ"""
#     if not authors:
#         return ""

#     formatted_authors = []
#     for author in authors:
#         last_name = author.get('surname', '').strip()
#         first_name = author.get('name', '').strip()
#         middle_name = author.get('patronymic', '').strip()

#         # Форматируем имя автора
#         if last_name and first_name:
#             if middle_name:
#                 formatted_authors.append(f"{last_name}, {first_name[0]}. {middle_name[0]}.")
#             else:
#                 formatted_authors.append(f"{last_name}, {first_name[0]}.")

#     # Форматирование списка авторов
#     if len(formatted_authors) == 1:
#         return formatted_authors[0]
#     elif len(formatted_authors) == 2:
#         return f"{formatted_authors[0]}, {formatted_authors[1]}"
#     elif len(formatted_authors) == 3:
#         return f"{formatted_authors[0]}, {formatted_authors[1]}, {formatted_authors[2]}"
#     else:
#         return formatted_authors
def format_authors(authors):
    """Форматирование авторов по ГОСТ"""
    if not authors:
        return []

    formatted_authors = []
    if len(authors) >= 4:
        for author in authors:
            last_name = author.get('surname', '').strip()
            first_name = author.get('name', '').strip()
            middle_name = author.get('patronymic', '').strip()

            # Форматируем имя автора
            if last_name and first_name:
                if middle_name:
                    formatted_authors.append(f"{first_name[0]}. {middle_name[0]}. {last_name}")  # Для 1-3 авторов
                else:
                    formatted_authors.append(f"{first_name[0]}. {last_name}")
    else:
        for author in authors:
            last_name = author.get('surname', '').strip()
            first_name = author.get('name', '').strip()
            middle_name = author.get('patronymic', '').strip()

            # Форматируем имя автора
            if last_name and first_name:
                if middle_name:
                    formatted_authors.append(f"{last_name}, {first_name[0]}. {middle_name[0]}.")  # Для 1-3 авторов
                else:
                    formatted_authors.append(f"{last_name}, {first_name[0]}.")
    # # Если 4 и более авторов, меняем порядок
    # if len(authors) >= 4:
    #     formatted_authors = [f"{author.split()[1]} {author.split()[0]} " for author in formatted_authors]

    return formatted_authors


# def format_printed_reference(data):
#     """Форматирование печатного источника по ГОСТ"""
#     authors = format_authors(data.get("authors", []))
#     title = data.get("title", "")
#     place = data.get("place", "")
#     publisher = data.get("publisher", "")
#     year = data.get("year", "")

#     edition_number = str(data.get("edition_number", "")).strip()
#     page_count = str(data.get("page_count", "")).strip()

#     if not all([authors, title]):
#         return "Ошибка: Отсутствуют обязательные поля для печатного источника."

#     reference = f"{', '.join(authors)} {title}."

#     if edition_number:
#         reference += f" - {edition_number}-е изд."

#     if place:
#         reference += f" — {place}"

#     if publisher:
#         reference += f".: {publisher}"

#     if year:
#         reference += f", {year}."

#     if page_count:
#         reference += f" - {page_count} с."

#     return reference
def format_printed_reference(data):
    """Форматирование печатного источника по ГОСТ с учетом количества авторов."""
    authors = format_authors(data.get("authors", []))
    title = data.get("title", "")
    place = data.get("place", "")
    publisher = data.get("publisher", "")
    year = data.get("year", "")

    edition_number = str(data.get("edition_number", "")).strip()
    page_count = str(data.get("page_count", "")).strip()

    if not all([authors, title]):
        return "Ошибка: Отсутствуют обязательные поля для печатного источника."

    if len(data.get("authors", [])) >= 4:
        # Формат для 4 и более авторов
        reference = f"{title}. / {', '.join(authors)}. "
    else:
        # Формат для 1-3 авторов
        reference = f"{', '.join(authors)} {title}. "

    if edition_number:
        reference += f"- {edition_number}-е изд. "

    if place:
        reference += f"— {place}. "

    if publisher:
        reference += f": {publisher}. "

    if year:
        reference += f"{year}. "

    if page_count:
        reference += f"- {page_count} с."

    return reference.strip()


# def format_journal_reference(data):
#     """Форматирование журнала по ГОСТ"""
#     authors = format_authors(data.get("authors", []))
#     title = data.get("title", "")
#     journal = data.get("journal", "")
#     publication_year = data.get("publication_year", "")
#     publication_date = format_date(data.get("publication_date", ""))
#     url = data.get("url", "")

#     reference = f"{authors} " if authors else ""
#     reference += f"{title}. " if title else ""
#     reference += f"// {journal}. {publication_year}. {publication_date}. URL: {url}."

#     return reference
def format_journal_reference(data):
    """Форматирование журнала по ГОСТ с учетом количества авторов."""
    authors = format_authors(data.get("authors", []))
    title = data.get("title", "")
    journal = data.get("journal", "")
    publication_year = data.get("publication_year", "")
    publication_date = format_date(data.get("publication_date", ""))
    url = data.get("url", "")

    if len(data.get("authors", [])) >= 4:
        # Формат для 4 и более авторов
        reference = f"{title}. / {', '.join(authors)} // {journal} : журн. {publication_year}. URL: {url}. Дата публикации: {publication_date}."
    else:
        # Формат для 1-3 авторов
        reference = f"{', '.join(authors)} {title}. // {journal} : журн. Дата публикации: {publication_date}."

    return reference



def format_internet_reference(data):
    """Форматирование интернет-ресурса по ГОСТ"""
    site_name = data.get("site_name", "")
    title = data.get("title", "")
    url = data.get("url", "")
    access_date = format_date(data.get("access_date", ""))

    if title:
        reference = f"{title}. // {site_name} : сайт. URL: {url} (дата обращения: {access_date})."
    else:
        reference = f"{site_name} : сайт. URL: {url} (дата обращения: {access_date})."

    return reference


def create_reference(data):
    """Функция выбора типа источника и форматирования ссылки"""
    if data["type"] == "journal":
        return format_journal_reference(data)
    elif data["type"] == "web":
        return format_internet_reference(data)
    elif data["type"] == "printed":
        return format_printed_reference(data)
    else:
        return "Ошибка: Неизвестный тип источника."

