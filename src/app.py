from flask import Flask, jsonify, request
app = Flask(__name__)
# add the jsonify method to your Flask import


# suppose you have your data in the variable some_data
todos = [ { "label": "My first task", "done": False }]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos', methods=['GET'])
def hello_world():
    # return '<h1>Hello!</h1>'
    json_text = jsonify(todos)
    return json_text








# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)