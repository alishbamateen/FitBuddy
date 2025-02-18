from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="")

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    response_message = f"You entered: {user_input}"
    return render_template('index.html', message=response_message)


if __name__ == '__main__':
    app.run(debug=True)
        