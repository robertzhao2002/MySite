from flask import Flask, jsonify, render_template, request
from flask import abort
from flask import make_response

app = Flask(__name__)

@app.route('/gpacalc')
def gpahome():
    return render_template('gpaform.html')

@app.route('/getgpa', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        tasks = request.form
        names = tasks['Class Names'].split(', ')
        grades = tasks['Grades'].split(', ')
        creds = tasks['Credits'].split(', ')
        tasks = []
        for i in range(len(names)):
            a = {'Name': '0', 'Grade': 0, 'Credits': 0}
            a['Name'] = names[i]
            a['Grade'] = float(grades[i])
            a['Credits'] = float(creds[i])
            tasks.append(a)
        return render_template('getgpa.html', tasks = tasks, gpa = show(tasks))

def show(tasks):
    grades = []
    creds = []
    for i in tasks:
        grades.append(i['Grade'])
        creds.append(i['Credits'])
    sum = 0
    c = 0
    print(creds)
    print(grades)
    for i in range(len(grades)):
        sum+=grades[i]*creds[i]
        c+=creds[i]
    print('sum='+str(sum))
    sum/=c
    print('c='+str(c))
    return str(round(sum,3))

if __name__ == '__main__':
    app.run(debug=True)
