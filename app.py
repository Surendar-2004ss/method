from flask import Flask, jsonify, request
app = Flask(__name__)
data_store = {}
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)
@app.route('/data/<key>', methods=['GET'])
def get_data_key(key):
    if key in data_store:
        return jsonify({key: data_store[key]})
@app.route('/data', methods=['POST'])
def post_data():
    data = request.json
    data_store.update(data)
    return jsonify(data_store), 200
@app.route('/data/<key>', methods=['PUT'])
def update_data(key):
    data = request.json
    if key in data_store:
        data_store[key] = data['value']
        return jsonify({key: data_store[key]})
    return jsonify({'error': 'Key is Not Defined'}), 404
@app.route('/data/<key>', methods=['DELETE'])
def delete_data(key):
    if key in data_store:
        del data_store[key]
        return jsonify({'message': f'{key} is Deleted'})
    return jsonify({'error': 'Key is Not Defined'}), 404
if __name__ == '__main__':
    app.run(debug=True)