from flask import Flask, render_template, request
import model

app = Flask(__name__)



@app.route('/' , methods = ['GET',"POST"])
def home():
    if request.method == 'POST':
        p_h = request.form.get('p_h')
        p_w = request.form.get('p_w')
        s_h = request.form.get('s_h')
        s_w = request.form.get('s_w')
        data = [float(p_h), float(p_w), float(s_h), float(s_w)]

        pre = model.predict_it(data)
        return render_template('predict.html' , pre = pre)
    else:
        return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)