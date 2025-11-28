from flask import Flask

app= Flask(__name__)

@app.route('/')
def hello():
    return 'Welcme to Flask App Bank of America'

if __name__ == '__main__':
    app.run()
    