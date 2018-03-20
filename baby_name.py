from flask import Flask, request
import requests
import os

key = os.environ.get('DATA_MOS_API_KEY')
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, adventurer!'


@app.route('/names')
def names_by_year():
    year = int(request.args.get('year'))
    data = get_data()
    body = '''Данные за {0} год.
    <table border=1>
        <tr>
            <th>Имя</th>
            <th>Кол-во пиплов</th>
            <th>Месяц</th>
        </tr>
        <tr>'''.format(year)
    for row in data:
        if row['Cells']['Year'] == year:
            body += '''<td>{0}</td>
                       <td>{1}</td>
                       <td>{2}</td>
                       </tr> 
                       <tr>'''.format(row['Cells']['Name'],
                                      row['Cells']['NumberOfPersons'],
                                      row['Cells']['Month'],
                                      )
    body += '</tr></table>'
    return body


def get_data():
    result = requests.get('http://api.data.mos.ru/v1/datasets/2009/rows', params={'api_key': key})
    if result.status_code == 200:
        return result.json()
    else:
        print('Error')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
