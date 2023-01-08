from flask import Flask, render_template, request
from flask_mail import Mail
import pandas as pd


app = Flask(__name__)

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'codescatter8980@gmail.com'
app.config['MAIL_PASSWORD'] = 'ynqolwjdibmzudao'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

df1_main = pd.DataFrame(columns=["name", "subject", "email", "messages"])


app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["Subject"]
        message = request.form["message"]

        df = pd.read_csv("contact_data.csv")
        df = df.append(pd.DataFrame([[name,subject, email,message]], columns=["name", "subject", "email", "messages"]))
        df.to_csv("contact_data.csv", index=False)
        return render_template("index.html", msg="sending successfully")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()    
    