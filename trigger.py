from flask import Flask,render_template,send_from_directory
my_app_obj = Flask(__name__)


@my_app_obj.route("/")
def hello():
    return render_template("home.html")

@my_app_obj.route("/index")
def show():
    return send_from_directory("static","icons/psmohammedali_CV.pdf")

@my_app_obj.route("/old")
def old_portfolio():
    return render_template("old.html")


if __name__ == "__main__":
    my_app_obj.run(debug=False,host='0.0.0.0')
