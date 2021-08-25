from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    answer = "No."
    if datetime.now().weekday() == 3:
        answer = "Yes!"
    return render_template('index.html', answer=answer)


if __name__ == "__main__":
    app.run()
