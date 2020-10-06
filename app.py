from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)


@app.route("/mypage/me")
def me():
    return render_template("first_page.html")


@app.route("/mypage/contact")
def contact():
    return render_template("second_page.html")


@app.route('/mypage/contact', methods=['POST'])
def contact_post():
    if request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/mypage/contact")


if __name__ == '__main__':
    app.run()