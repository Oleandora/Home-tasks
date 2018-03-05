from datetime import datetime
from flask import Flask, abort, request
import requests, pprint

key = '5a8160579c036312bb4163fd1fbf9767'
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, adventurer!"

@app.route("/names")
def names():
    year = int(request.args.get('year'))
    data = get_data_from_url("http://api.data.mos.ru/v1/datasets/2009/rows?api_key={0}".format(key))
    body = "Данные за {0} год.\n<table border=1><tr><th>Имя</th><th>Кол-во пиплов</th><th>Месяц</th></tr><tr>".format(year)
    for row in data:
        if row['Cells']['Year'] == year:
            body += "<td>{0}</td><td>{1}</td><td>{2}</td></tr><tr>".format(row['Cells']['Name'],
                                                                           row['Cells']['NumberOfPersons'],
                                                                           row['Cells']['Month'])

    body += "</tr></table>"
    return body


def get_data_from_url(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("Error")


if __name__ == '__main__':
    app.run(port=8080, debug=True)
