#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/todo": {"origins": "http://localhost:5000"}})

@app.route('/')
def index():
    return "Hello, World!"

tasks = []

@app.route('/todo', methods=['GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def get_tasks():
    response = jsonify({'tasks': tasks})
    return response

@app.route('/todo/<int:id>', methods=['GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def get_task(id):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    if (len(tasks) == 0):
        task['id'] = 1
    else:
        task['id'] = tasks[-1]['id'] + 1
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.route('/todo/<int:id>', methods=['PUT'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def update_task(id):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/<int:id>', methods=['DELETE'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def delete_task(id):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)