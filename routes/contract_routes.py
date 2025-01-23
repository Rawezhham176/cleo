from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.Contract import Contract
from models.Customer import Customer
from utils.extensions import db

contracts_route = Blueprint("contracts", __name__)

@contracts_route.route("/all_contracts", methods=["GET"])
@jwt_required()
def get_contracts():
    user = get_jwt_identity()
    if not user:
        return jsonify({
            "message": "Unauthorized access"
        }), 401
    contracts = Contract.query.all()
    return jsonify(
        [
            {
                "contract_id": contract.contract_id,
                "contract_name": contract.contract_name,
                "customer_id": contract.customer_id,
                "date_created": contract.date_created
             }
            for contract in contracts
        ]
    ), 200

@contracts_route.route("/add_contract", methods=["POST"])
@jwt_required()
def add_contract():
    user = get_jwt_identity()
    if not user:
        return jsonify({
            "message": "Unauthorized access"
        }), 401
    contract_data = request.json
    if not all([contract_data.get("contract_name"),
                contract_data.get("customer_surname")]):
        return jsonify({
            "message": "contract_name and customer_relation_id are required"
        }), 400

    customer_id = Customer.query.filter_by(customer_surname=contract_data["customer_surname"]).first().customer_id
    new_contract = Contract(
        contract_name=contract_data["contract_name"],
        customer_id=customer_id
    )

    db.session.add(new_contract)
    db.session.commit()
    return jsonify({
        "message": "Contract created successfully"
    }), 201
