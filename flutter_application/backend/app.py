from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://amukam:loc@localhost/locsafedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

# Import models
from models import *

db.init_app(app)

@app.route('/')
def home():
    return "API is running!"

""" if __name__ == '__main__':
    app.run(debug=True)
 """

@app.route('/properties', methods=['GET', 'POST'])
def manage_properties():
    if request.method == 'POST':
        data = request.json
        new_property = Property(name=data['name'], address=data['address'], rent_amount=data['rent_amount'])
        db.session.add(new_property)
        db.session.commit()
        return jsonify({'message': 'Property added successfully'}), 201
    else:
        properties = Property.query.all()
        return jsonify([{
            'id': p.id, 'name': p.name, 'address': p.address, 'rent_amount': str(p.rent_amount)
        } for p in properties])

# Add similar endpoints for tenants and payments

@app.route('/tenants', methods=['GET', 'POST'])
def manage_tenants():
    if request.method == 'POST':
        data = request.json
        new_tenant = Tenant(name=data['name'], contact_info=data['contact_info'])
        db.session.add(new_tenant)
        db.session.commit()
        return jsonify({'message': 'Tenant added successfully'}), 201
    else:
        tenants = Tenant.query.all()
        return jsonify([{
            'id': t.id, 'name': t.name, 'contact_info': t.contact_info
        } for t in tenants])
    
@app.route('/payments', methods=['GET', 'POST'])
def manage_payments():
    if request.method == 'POST':
        data = request.json
        new_payment = Payment(tenant_id=data['tenant_id'], amount=data['amount'], payment_date=data['payment_date'])
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({'message': 'Payment added successfully'}), 201
    else:
        payments = Payment.query.all()
        return jsonify([{
            'id': p.id, 'tenant_id': p.tenant_id, 'amount': str(p.amount), 'payment_date': str(p.payment_date)
        } for p in payments])
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)