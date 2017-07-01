from flask import Flask, render_template
import json


app = Flask(__name__)
# app.config['SERVER_NAME'] = 'meu12server123.org'
lessons = ['L'+str(i+1) for i in range(60)]         # lessons = [L1,L2,...,L60,R1,R2,...,R10]
[lessons.append('R'+str(i+1)) for i in range(10)]
# print(lessons)

# file = open("content.json","r")
# data = file.read()
# data = data.split(',')
# b = "[]{}\"\'"
# for char in b:
#     data = [s.replace(char,"") for s in data]
# print(data)
# file.close()
# print(['a','b'])



json_data = open('content.json')
d = json.load(json_data)
data = d['lessonList']
for section in data:
    for s in section['sectionList']:
        print('tuple -> ',s['name'],s['audio'])


# Index
@app.route('/')
def index():
    return render_template('index.html',lessons=lessons,data=data)

# Audio
@app.route('/play/<string:folder>/<string:file>/')
def audio(folder,file):
    return render_template('audio.html', folder=folder, file=file, data=data)

if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0',debug=True, threaded=True)

# port=80, host='0.0.0.0'
