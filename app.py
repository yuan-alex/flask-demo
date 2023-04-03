from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

if __name__ == '__main__':
    app.run()
