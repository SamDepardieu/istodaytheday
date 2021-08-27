import os
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    dow = os.getenv('DAY_OF_WEEK')
    answer = os.getenv('ANSWER_NEGATIVE')
    if datetime.now().weekday() == int(dow):
        answer = os.getenv('ANSWER_POSITIVE')
    return render_template(
        'index.html',
        answer=answer,
        question=os.getenv('TITLE_QUESTION'),
    )


if __name__ == "__main__":
    app.run()
