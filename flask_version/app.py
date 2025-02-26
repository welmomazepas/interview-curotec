from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    new_item = Item(name=data['name'], description=data.get('description', ''), price=data['price'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"id": new_item.id, "message": "Item created successfully"}), 201


@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price}
            for item in items
        ])


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify({"id": item.id, "name": item.name, "description": item.description, "price": item.price})


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.json
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    item.price = data.get('price', item.price)
    db.session.commit()
    return jsonify({"message": "Item updated successfully"})


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
