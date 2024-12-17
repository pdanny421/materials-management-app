from app import app, db
from models import Material, MaterialField, User
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required

# Authentication
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "User already exists"}), 400
    
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=user.username)
    return jsonify(access_token=access_token), 200


# Materials CRUD
@app.route('/materials', methods=['POST'])
@jwt_required()
def create_material():
    data = request.json
    material = Material(
        material_name=data['material_name'],
        hs_code=data.get('hs_code', '')
    )
    db.session.add(material)
    db.session.commit()

    custom_fields = data.get('fields', [])
    for field in custom_fields:
        new_field = MaterialField(
            material_id=material.id,
            field_name=field['field_name'],
            field_value=field['field_value'],
            field_type=field['field_type']
        )
        db.session.add(new_field)
    db.session.commit()

    return jsonify({"message": "Material created", "id": material.id}), 201
