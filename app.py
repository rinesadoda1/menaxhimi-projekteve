from flask import Flask, request, jsonify

app = Flask(__name__)
projects = []

@app.route('/projects', methods=['GET'])
def list_projects():
    return jsonify(projects)

@app.route('/projects', methods=['POST'])
def add_project():
    data = request.json
    projects.append(data)
    return jsonify({'message': 'Project added'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
