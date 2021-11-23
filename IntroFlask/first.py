from flask import Flask, render_template
import sqlite3
import os

currentDirectory=os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

headings = ("Name", "RegNo", "Phone")
data = (
    ("rolf", "1900012", "91909090"),
    ("amy", "1900014", "9191919191"),
    ("bob", "1900012", "9898989898"),
)


@app.route('/')
def table():
    return render_template("table.html", headings=headings, data=data, )


if __name__ == '__main__':
    app.run()
