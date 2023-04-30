from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # extract form data from request object
        name = request.form['fullName']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # insert form data into database
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute('INSERT INTO messages (name, email, subject, message) VALUES (?, ?, ?, ?)',
                  (name, email, subject, message))
        conn.commit()
        conn.close()

        return render_template('thankyou.html')
    else:
        return render_template('contact.html')

@app.route('/snake')
def snake():
    return render_template('snake.html')

if __name__ == '__main__':
    app.run(debug=True)
