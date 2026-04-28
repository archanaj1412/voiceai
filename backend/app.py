from flask import Flask

app = Flask(__name__)

# Register blueprints here

@app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404

@app.errorhandler(Exception)
def handle_exception(e):
    return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True)