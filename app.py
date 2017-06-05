from flask import Flask, render_template

app = Flask(__name__)

# Index
@app.route('/')
def index():
    return render_template('index.html')

# Audio
@app.route('/play/<string:folder>/<string:file>/')
def audio(folder,file):
    return render_template('audio.html', folder=folder, file=file)

if __name__ == '__main__':
    app.run(debug=True)
