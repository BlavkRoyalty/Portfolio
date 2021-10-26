from flask import render_template, send_file, request, flash, session, redirect
from werkzeug.utils import redirect
from portfolio import prt, db
from portfolio.models import Message



@prt.route('/',methods=['POST','GET'])
def home():
    m = Message()
    if request.method == 'GET':
        return render_template('user/home.html')

    else:
        #retrieve form data
        fname = request.form.get('name')
        mail = request.form.get('email')
        msg = request.form.get('message')

        m = Message(sender_name = f'{fname}',sender_email = f'{mail}',sender_message = f'{msg}')
        db.session.add(m)
        db.session.commit()
        # session = m.sender_id
        # flash = (f'Thanks {fname}, your message has been recieved we will get back you as sooon as possible')
        return redirect('/welcome')


    # return render_template('user/home.html')

@prt.route('/download')
def download_file():
    p = 'resume.docx'
    return send_file(p,as_attachment=True)

@prt.route('/welcome', methods=['POST','GET'])
def welcome():
    return render_template('user/welcome.html')