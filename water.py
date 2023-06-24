from flask import Flask,  render_template
app = Flask(__name__)
@app.route('/water/<tree>')
def hellow_world(tree):
    str= "Save waterbsave planet and "+tree
    return str

@app.route('/water')
def hellow_planet():
    return render_template('2nd page.html')


@app.route('/tree')
def input_tree():
    return render_template('hello.html')

@app.route("/")
def hollow_planet():
    return render_template('main.html')


