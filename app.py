from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def sarjaan():
  return render_template("home.html")  # home.html or home_bootstrap.html


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
