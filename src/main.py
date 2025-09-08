from flask import Flask
from controllers.instrument_controller import instrument_bp

app = Flask(__name__)
app.register_blueprint(instrument_bp)

if __name__ == '__main__':
    app.run(debug=True)
