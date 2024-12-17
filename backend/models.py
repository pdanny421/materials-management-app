from app import db

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material_name = db.Column(db.String(100), nullable=False)
    hs_code = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

class MaterialField(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'), nullable=False)
    field_name = db.Column(db.String(100), nullable=False)
    field_value = db.Column(db.String(200), nullable=True)
    field_type = db.Column(db.String(50), nullable=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
