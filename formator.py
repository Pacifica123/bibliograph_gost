from datetime import datetime

def format_date(date_str):
    """Форматирует дату из формата 'YYYY-MM-DD' в 'DD.MM.YYYY'."""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return date_str


def format_authors(authors):
    """Форматирование авторов по ГОСТ"""
    if not authors:
        return ""

    formatted_authors = []
    for author in authors:
        last_name = author.get('last_name', '').strip()
        first_name = author.get('first_name', '').strip()
        middle_name = author.get('middle_name', '').strip()

        # Форматируем имя автора
        if last_name and first_name:
            if middle_name:
                formatted_authors.append(f"{last_name}, {first_name[0]}. {middle_name[0]}. ")
            else:
                formatted_authors.append(f"{last_name}, {first_name}. {middle_name} ")

    # Форматирование списка авторов
    if len(formatted_authors) == 1:
        return formatted_authors[0]
    elif len(formatted_authors) == 2:
        return f"{formatted_authors[0]}, {formatted_authors[1]}"
    elif len(formatted_authors) == 3:
        return f"{formatted_authors[0]}, {formatted_authors[1]}, {formatted_authors[2]}"
    else:
        return formatted_authors



def format_printed_reference(data):
    """Форматирование печатного источника по ГОСТ"""
    authors = format_authors(data.get("authors", []))
    title = data.get("title", "")
    place = data.get("place", "")
    publisher = data.get("publisher", "")
    year = data.get("year", "")

    edition_number = str(data.get("edition_number", "")).strip()
    page_count = str(data.get("page_count", "")).strip()

    if not all([authors, title]):
        return "Ошибка: Отсутствуют обязательные поля для печатного источника."

    reference = f"{authors}. {title}."

    if edition_number:
        reference += f" - {edition_number}-е изд."

    if place:
        reference += f" — {place}"

    if publisher:
        reference += f".: {publisher}"

    if year:
        reference += f", {year}."

    if page_count:
        reference += f" - {page_count} с."

    return reference


def format_electronic_reference(data):
    """Форматирование электронного источника по ГОСТ"""
    authors = format_authors(data.get("authors", []))
    title = data.get("title", "")
    website = data.get("website", "")
    publication_year = data.get("publication_year", "")
    url = data.get("url", "")
    access_date = format_date(data.get("access_date", ""))

    if not all([title, url, access_date]):
        return "Ошибка: Отсутствуют обязательные поля для электронного источника."

    reference = ""

    if len(data.get("authors", [])) <= 3 and authors:
        reference += f"{authors} "
        reference += f"{title} // {website}."


    if len(data.get("authors", [])) > 3 and authors:
        reference += f"{title} "
        # Формируем список авторов после названия через '/'
        reference += f" / {', '.join(authors)} // {website}."





    if publication_year:
        reference += f" {publication_year}."

    reference += f" URL: {url} (дата обращения: {access_date})."

    return reference


def create_reference(data):
    """Функция выбора типа источника и форматирования ссылки"""
    if data["type"] == "printed":
        return format_printed_reference(data)
    elif data["type"] == "electronic":
        return format_electronic_reference(data)
    else:
        return "Ошибка: Неизвестный тип источника."
