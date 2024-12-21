from flask import Flask,render_template

app = Flask(__name__)

print(f"__name__ is: {__name__}")

@app.route('/')
def hello_world():
    #return render_template("index.html")
    return 'hello_world'

@app.route('/contents')
def hello_contents():
    return 'hello_contents'

#app.runの引数ポートは、docker runコマンドの-pの指定と一致していないとダメ
if __name__=='__main__':
    app.run(host='0.0.0.0', port=8100)
