from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        if not name or not age.isdigit():
            return "Invalid input!", 400

        return f"Hello, {name}. You are {age} years old."
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
