from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/health-check')
def health_check():
    return "Application is running fine!", 200

if __name__ == '__main__':
    app.run(debug=True)