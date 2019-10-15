from flask import Flask, render_template, request

import newAD
import ItopAutomacao
import pythoncom
import Assinatura

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('teste.html')


'''@app.route('/login', methods= ['POST'])
def login():
  login = request.form
  config = {'user': request.form['User'], 'pss': request.form['Password']}
  users = DBApi.Query(config['user'], config['pss']).checkUser()
  print(users)

  if users:
    return render_template('login.html', login=login)
  else:
    return a'''


@app.route('/results', methods=['POST'])
def results():
    pythoncom.CoInitialize()
    results = request.form
    config = {'name': request.form['Name'],
              'sector': request.form['Sector'],
              'cargo': request.form['Cargo'],
              'password': request.form['Password'],
              'user': request.form['User'],
              'ramal': request.form['Ramal']
              }
    newAD.createUser(config['name'], config['user'], config['sector'])
    Assinatura.writeSignature(config['name'], config['cargo'], config['user'], config['ramal'])
    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
