from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.Customer import Customer
from models.Contract import Contract
from utils.extensions import db

customer_route = Blueprint("customers", __name__)

@customer_route.route("/all_customers", methods=["GET"])
@jwt_required()
def get_customers():
    user = get_jwt_identity()
    if not user:
        return jsonify({
            "message": "Unauthorized access"
        }), 401
    customers = Customer.query.all()
    return jsonify(
        [
            {
                "customer_id": customer.customer_id,
                "customer_name": customer.customer_name,
                "customer_surname": customer.customer_surname,
                "customer_phone_number": customer.customer_phone_number,
                "customer_email": customer.customer_email,
                "customer_address": customer.customer_address
             }
            for customer in customers
        ]
    ), 200

@customer_route.route("/<int:customer_id>/contracts", methods=["GET"])
@jwt_required()
def get_contracts_by_customer_id(customer_id):
    user = get_jwt_identity()
    if not user:
        return jsonify({
            "message": "Unauthorized access"
        }), 401
    contracts = Contract.query.filter_by(customer_id=customer_id).all()
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

@customer_route.route("/<int:customer_id>/contracts/<int:contract_id>", methods=["GET"])
@jwt_required()
def get_contract_details_by_customer_id(customer_id, contract_id):
    user = get_jwt_identity()
    if not user:
        return jsonify({
            "message": "Unauthorized access"
        }), 401

    contract = Contract.query.filter_by(customer_id=customer_id, contract_id=contract_id).first()

    if not contract:
        return jsonify({
            "message": "Contract not found"
        }), 404

    return jsonify({
        "contract_id": contract.contract_id,
        "contract_name": contract.contract_name,
        "customer_id": contract.customer_id,
        "date_created": contract.date_created
    }), 200

@customer_route.route("/<int:customer_id>/contracts/<int:contract_id>", methods=["PUT"])
@jwt_required()
def update_contract_by_customer_id(customer_id, contract_id):
    user = get_jwt_identity()
    if not user:
        return jsonify({
            "message": "Unauthorized access"
        }), 401

    contract_data = request.json
    if not all([contract_data.get("contract_name"),
                contract_data.get("customer_id")]):
        return jsonify({
            "message": "contract_name and customer_id are required"
        }), 400

    contract = Contract.query.filter_by(customer_id=customer_id, contract_id=contract_id).first()
    if not contract:
        return jsonify({
            "message": "contract not found or unauthorized"
        }), 404

    contract.contract_name = contract_data.get("contract_name")
    contract.customer_id = contract_data.get("customer_id")
    db.session.commit()

    return jsonify({
        "message": "Blog updated successfully"
    }), 200