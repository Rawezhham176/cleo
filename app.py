from flask import Flask, render_template
from utils.extensions import db, jwt
from flask_cors import CORS
from routes.contract_routes import contracts_route
from routes.customer_routes import customer_route
from routes.auth_routes import auth_route
from config import config


def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "*"}},
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         allow_headers=["Content-Type", "Authorization"],
         supports_credentials=True)

    app.config.from_object(config.Config)
    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(contracts_route, url_prefix="/contracts")
    app.register_blueprint(customer_route, url_prefix="/customers")
    app.register_blueprint(auth_route, url_prefix="/auth")


    @app.errorhandler("/*")
    def not_found(e):
        return {"error": "Not found"}, 404

    @app.route('/')
    def login_page():
        return render_template('login.html')

    @app.route('/table')
    def table_page():
        return render_template('table.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="localhost", port=4000, debug=True)
