from flask import Flask, render_template, url_for

app = Flask('Psyche Explorer')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)