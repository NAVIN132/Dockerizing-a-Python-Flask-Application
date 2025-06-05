from flask import Flask, render_template, request

app = Flask(__name__)
applications = []  # In-memory list to store submitted applications

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    student = {
        'name': request.form['name'],
        'email': request.form['email'],
        'dob': request.form['dob'],
        'course': request.form['course']
    }
    applications.append(student)
    return render_template('success.html', student=student)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
