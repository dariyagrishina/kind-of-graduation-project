from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def first_page():
    return render_template("index.html")

app.debug = True
if __name__ == '__main__':
    app.run()
