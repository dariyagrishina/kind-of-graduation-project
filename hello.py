from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def first_page():
    return render_template("index.html")

# R: нелогичное место для поднятия флага, нужно было это делать
#     - сразу после создания app
#     - непосредственно перед вызовом app.run()
#     - в вызове app.run(debug=True)
app.debug = True
if __name__ == '__main__':
    app.run()
