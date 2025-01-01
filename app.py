from flask import Flask, render_template, request, redirect, url_for, jsonify
from formator import create_reference, format_authors
from validation_chain import Validator
from datetime import datetime
import json

# from fields_list import PRINTED_FIELDS, ELECTRONIC_FIELDS,
from fields_list import FIELDS

app = Flask(__name__)
app.secret_key = 'TODO : _secret_key'

@app.route('/')
def home():
    fields_json = json.dumps(FIELDS)
    print(fields_json)  # Выводим данные в консоль для проверки
    return render_template('index.html', reference=None)
    # return render_template('index.html', fields=FIELDS, reference=None)

# @app.route('/form/printed')
# def form_printed():
#     return render_template('index.html', fields=PRINTED_FIELDS, reference=None, form_type="printed")
#
#
# @app.route('/form/electronic')
# def form_electronic():
#     access_date = datetime.today().strftime('%Y-%m-%d')
#     return render_template('index.html', fields=ELECTRONIC_FIELDS, reference=None, form_type="electronic", access_date=access_date)
#

@app.route('/form/<form_type>', methods=['GET'])
def get_form(form_type):
    if form_type not in FIELDS:
        return jsonify({"error": "Неизвестная форма"}), 400

    fields = FIELDS[form_type]
    print(fields)
    return render_template('index.html', fields=fields, form_type=form_type)


@app.route('/submit', methods=['POST'])
def submit():
    form_type = request.form['form_type']
    data_for_reference = {'type': form_type}

    if form_type == 'journal':
        # Собираем данные для журнала
        data_for_reference['authors'] = [
            {
                'surname': surname,
                'name': name,
                'patronymic': patronymic
            }
            for surname, name, patronymic in zip(
                request.form.getlist('authors_surname[]'),
                request.form.getlist('authors_name[]'),
                request.form.getlist('authors_patronymic[]')
            )
        ]
        data_for_reference['title'] = request.form['title']
        data_for_reference['journal'] = request.form['journal']
        data_for_reference['publication_year'] = request.form['publication_year']
        data_for_reference['publication_date'] = request.form['publication_date']
        data_for_reference['url'] = request.form['url']

    elif form_type == 'web':
        # Собираем данные для веб-сайта
        data_for_reference['site_name'] = request.form['site_name']
        data_for_reference['title'] = request.form['title']
        data_for_reference['url'] = request.form['url']
        data_for_reference['access_date'] = request.form['access_date']

    elif form_type == 'printed':
        # Собираем данные для печатного ресурса
        data_for_reference['authors'] = [
            {
                'surname': surname,
                'name': name,
                'patronymic': patronymic
            }
            for surname, name, patronymic in zip(
                request.form.getlist('authors_surname[]'),
                request.form.getlist('authors_name[]'),
                request.form.getlist('authors_patronymic[]')
            )
        ]
        data_for_reference['title'] = request.form['title']
        data_for_reference['publisher'] = request.form['publisher']
        data_for_reference['year'] = request.form['year']

    # Генерируем ссылку с помощью create_reference
    reference = create_reference(data_for_reference)

    return render_template("index.html", current_section=form_type, reference=reference)


if __name__ == '__main__':
    app.run(debug=True)
