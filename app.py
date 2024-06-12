# This is a test change to trigger CI/CD pipeline

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config.from_object('config.Config')

# Хранение данных в памяти
contacts = {}
contact_id_counter = 1

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Создание нового контакта
@app.route('/contacts', methods=['POST'])
def create_contact():
    global contact_id_counter
    contact = request.json
    contact['id'] = contact_id_counter
    contacts[contact_id_counter] = contact
    contact_id_counter += 1
    return jsonify(contact), 201

# Получение списка контактов
@app.route('/contacts', methods['GET'])
def get_contacts():
    return jsonify(list(contacts.values())), 200

# Получение информации о конкретном контакте
@app.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = contacts.get(contact_id)
    if contact is None:
        return jsonify({'error': 'Contact not found'}), 404
    return jsonify(contact), 200

# Обновление контакта
@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    contact = contacts.get(contact_id)
    if contact is None:
        return jsonify({'error': 'Contact not found'}), 404

    updated_contact = request.json
    updated_contact['id'] = contact_id
    contacts[contact_id] = updated_contact
    return jsonify(updated_contact), 200

# Удаление контакта
@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = contacts.pop(contact_id, None)
    if contact is None:
        return jsonify({'error': 'Contact not found'}), 404
    return jsonify({'message': 'Contact deleted'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
