from flask import Flask, jsonify, request

app = Flask(__name__)
points = [ {
    "name": "Музей археологии Москвы",
    "coords": "55.75632,37.617132",
    "description": "мать жива?",
    "category": "Музеи",
    "address": " Манежная площадь, 1А, Москва"
  },
  {
    "name": "Музей Отечественной войны 1812 года",
    "coords": "55.756305,37.61865",
    "description": "мать жива?",
    "category": "Музеи",
    "address": "площадь Революции, 2/3, Москва"
  },
  {
    "name": "Музей Оружейный подвал",
    "coords": "55.756842,37.62175",
    "description": "мать жива?",
    "category": "Музеи",
    "address": "Никольская ул., 11-13с1, Москва"
  },
  {
    "name": "Музей уникальных кукол",
    "coords": "55.759334,37.644486",
    "description": "мать жива?",
    "category": "Музеи",
    "address": "ул. Покровка, 13, стр. 2, Москва"
  },
  {
    "name": "Мемориальный музей-квартира художника А.М. Васнецова",
    "coords": "55.763741,37.648546",
    "description": "мать жива?",
    "category": "Музеи",
    "address": "Фурманный переулок, 6, Москва"
  },
  {
    "name": "Иннопарк",
    "coords": "55.760135,37.624957",
    "description": "мать жива?",
    "category": "Музеи",
    "address": "Театральный пр., 5, стр. 1, Москва"
  },
  {
    "name": "Музей МАРХИ",
    "coords": "55.763022,37.622558",
    "description": "мать жива?",
    "category": "Музеи",
    "address": "ул. Рождественка, 11, стр. 2, Москва"
  },
  {
    "name": "Музей уникальных кукол",
    "coords": "55.759334,37.644486",
    "description": "мать жива?",
    "category": "Музеи",
    "address": "ул. Покровка, 13, стр. 2, Москва"
  }]

@app.route('/points', methods=['GET'])
def hello_world():  # put application's code here
    args = request.args
    print(args)
    query = {}
    if 'type' in args:
        query['type'] = args['type']
    else:
        query['type'] = 'short'
    query['categories'] = {i: int(args[i]) for i in filter(lambda x: x != 'type', args.keys() )}

    print(query)
    response = jsonify(points)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == '__main__':
    app.run()
