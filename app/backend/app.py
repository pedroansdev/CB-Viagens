from flask import Flask, json, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('../data.json','r', encoding = 'utf8') as file:
    data = json.load(file)

@app.route('/api/all', methods = ['GET'])
def all_services():
    return jsonify(data['transport'])

@app.route('/api/curitiba', methods = ['GET'])
def services_in_curitiba():
    filtered_data = [transport for transport in data['transport'] if transport['city'] == 'Curitiba']

    # There is another way to code the same thing below:
    
    # filtered_data = []
    # for transport in data['transport']:
    #     if(transport['city'] == 'Curitiba'):
    #         filtered_data.append(transport)

    return jsonify(filtered_data)

@app.route('/api/sp', methods = ['GET'])
def services_in_sp():
    filtered_data = [transport for transport in data['transport'] if transport['city'] == 'São Paulo']
    return jsonify(filtered_data)

@app.route('/api/rj', methods = ['GET'])
def services_in_rj():
    filtered_data = [transport for transport in data['transport'] if transport['city'] == 'Rio de Janeiro']
    return jsonify(filtered_data)

@app.route('/api/bh', methods = ['GET'])
def services_in_bh():
    filtered_data = [transport for transport in data['transport'] if transport['city'] == 'Belo Horizonte']
    return jsonify(filtered_data)

@app.route('/api/manaus', methods = ['GET'])
def services_in_manaus():
    filtered_data = [transport for transport in data['transport'] if transport['city'] == 'Manaus']
    return jsonify(filtered_data)

@app.route('/api/natal', methods = ['GET'])
def services_in_natal():
    filtered_data = [transport for transport in data['transport'] if transport['city'] == 'Natal']
    return jsonify(filtered_data)

@app.route('/api/campinas', methods = ['GET'])
def services_in_campinas():
    filtered_data = [transport for transport in data['transport'] if transport['city'] == 'Campinas']
    return jsonify(filtered_data)

@app.route('/api/recife', methods = ['GET'])
def services_in_recife():
    filtered_data = [transport for transport in data['transport'] if transport['city'] == 'Recife']
    return jsonify(filtered_data)

@app.route('/api/salvador', methods = ['GET'])
def services_in_salvador():
    filtered_data = [transport for transport in data['transport'] if transport['city'] == 'Salvador']
    return jsonify(filtered_data)

@app.route('/api/fortaleza', methods = ['GET'])
def services_in_fortaleza():
    filtered_data = [transport for transport in data['transport'] if transport['city'] == 'Fortaleza']
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug = True, port = 3000)