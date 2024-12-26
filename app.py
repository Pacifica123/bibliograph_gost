from flask import Flask, render_template, request, redirect, url_for, jsonify
from formator import create_reference
from validation_chain import Validator
from datetime import datetime
from fields_list import PRINTED_FIELDS, ELECTRONIC_FIELDS

app = Flask(__name__)
app.secret_key = 'TODO : _secret_key'

@app.route('/')
def home():
    return render_template('index.html', fields=None, reference=None)

@app.route('/form/printed')
def form_printed():
    return render_template('index.html', fields=PRINTED_FIELDS, reference=None, form_type="printed")


@app.route('/form/electronic')
def form_electronic():
    access_date = datetime.today().strftime('%Y-%m-%d')
    return render_template('index.html', fields=ELECTRONIC_FIELDS, reference=None, form_type="electronic", access_date=access_date)


@app.route('/submit', methods=['POST'])
def submit():
    form_type = request.form['form_type']
    reference = ""
    data_for_reference = {}

    print(request.form)

    # Сбор данных об авторах
    authors = []
    surnames = request.form.getlist('authors_surname[]')
    names = request.form.getlist('authors_name[]')
    patronymics = request.form.getlist('authors_patronymic[]')

    for i in range(len(surnames)):
        last_name = surnames[i].strip()
        first_name = names[i].strip()
        middle_name = patronymics[i].strip() if len(patronymics) > i else ''

        if last_name and first_name:  # Проверяем наличие фамилии и имени
            authors.append({
                'last_name': last_name,
                'first_name': first_name,
                'middle_name': middle_name
            })

    # Обязательно добавляем authors в data_for_reference, даже если список пуст
    data_for_reference['authors'] = authors

    # Генерация ссылки в зависимости от формы
    if form_type == 'printed':
        title = request.form['title']
        place = request.form.get('place', '')
        publisher = request.form.get('publisher', '')
        year = request.form.get('year', '')
        edition_number = request.form.get('edition_number', '')
        page_count = request.form.get('page_count', '')

        data_for_reference.update({
            'type': form_type,
            'title': title,
            'place': place,
            'publisher': publisher,
            'year': year,
            'edition_number': edition_number,
            'page_count': page_count
        })

    elif form_type == 'electronic':
        title = request.form['title']
        journal = request.form.get('journal', '')
        publication_year = request.form.get('publication_year', '')
        url = request.form['url']
        access_date = request.form['access_date']

        data_for_reference.update({
            'type': form_type,
            'title': title,
            'website': journal,
            'url': url,
            'publication_year': publication_year,
            'access_date': access_date
        })

    reference = create_reference(data_for_reference)

    # Перенаправляем пользователя на нужную страницу с результатом
    fields_to_render = PRINTED_FIELDS if form_type == 'printed' else ELECTRONIC_FIELDS

    return render_template('index.html', fields=fields_to_render, reference=reference, form_type=form_type)




if __name__ == '__main__':
    app.run(debug=True)
