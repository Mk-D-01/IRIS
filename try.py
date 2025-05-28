from flask import Flask, session, render_template, request

app = Flask(__name__)
app.secret_key = 'kokok'
@app.route('/', methods = ["POST","GET"])

def main():
    if request.method == "POST"  :
        session["name"] = request.form.get("name")
        if session['name'] == 'mk':
            return render_template('welcome.html' ,name = 'JOnny')
        else:return 'mk '

    return render_template("login.html")




if __name__ == "__main__":
    app.run(debug = True)