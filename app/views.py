from flask import render_template, request, flash
from app import app
from .forms import ContactForm
from flask_mail import Message, Mail

mail = Mail()
app.secret_key = '741Bag963!'

app.config["MAIL_SERVER"] = "secure53.webhostinghub.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@bryangalindo.com'
app.config["MAIL_PASSWORD"] = '741Bag963!'

mail.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/bio')
def bio():
    return render_template('bio.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@bryangalindo.com',
                          recipients=['galindo.bryan08@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('contact.html', success=True)

    elif request.method == 'GET':
        return render_template('contact.html', form=form)
