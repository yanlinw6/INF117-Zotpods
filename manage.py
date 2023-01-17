# coding: utf-8

import os
from flask_migrate import Migrate
from flask.cli import with_appcontext
from web import app, db, models
from web.models.user_models import User
# from flask_mail import Message
from wtforms.validators import Email
from email_validator import validate_email, EmailNotValidError
from web.mails.email import send_email
import click
import getpass
import config
import csv
import sys


migrate = Migrate(app, db)


@click.command(name='runserver')
@with_appcontext
def runserver():
    """
    run flask website in development mode

    python manage.py runserver
    """
    app.run(port=5001, host='127.0.0.1')


def __create_superuser():
    """
    create admin user
    :return:
    """

    tag = 0
    while True:
        if tag > 2:
            return
        username = click.prompt("Username", type=str, default=getpass.getuser())
        username = username.strip()
        if username:
            user = User.query.filter_by(username=username).first()
            if user is None:
                break
            else:
                print(f'{username} has been taken. Please change to another one, and try again later')
        tag += 1
    tag = 0
    while True:
        if tag > 2:
            return
        tag += 1
        email = click.prompt("Email", type=str)
        email = email.strip()
        if email:
            if email.count('@') != 1:
                print('Please supply a valid email address')
                continue
            else:
                try:
                    validate_email(email, check_deliverability=False)
                except EmailNotValidError as e:
                    print(str(e))
                    continue
                # _user, _host = email.split('@')
                # if not bool(email_validator.user_regex.match(_user)) or not email_validator.validate_hostname(_host):
                #     print('Please supply a valid email address')
                #     continue
            user = User.query.filter_by(email=email).first()
            if user is None:
                break
            else:
                print(f'{email} has been occupied.')

    tag = 0
    while True:
        if tag > 2:
            return
        password = click.prompt(text='Password', hide_input=True)
        password = password.strip()
        if len(password) < 5:
            print('Too short. Please make it longer than 6 chars')
        elif len(password) > 32:
            print('Too Long.，Please make it shorter than 32 chars')
        else:
            break
        tag += 1

    tag = 0
    while True:
        if tag > 2:
            return
        password2 = click.prompt(text='Password Repeat', hide_input=True)
        password2 = password2.strip()
        if password2 != password:
            print('Does not match.')
        else:
            break
        tag += 1
    user = User(username=username, is_superuser=True, is_active=True, email=email, is_confirmed=True)
    user.password = password
    db.session.add(user)
    db.session.commit()
    print('Your account created.')


@app.cli.command('createsuperuser')
def create_superuser():
    """
    create admin user
    :return:
    """
    try:
        __create_superuser()
    except click.exceptions.Abort:
        print('Aborted.')
        sys.exit()


@app.cli.command('send-email')
@click.option('--subject', help="email subject")
@click.option('--to', help="send email to who")
@click.option('--text', help="email content")
def __send_email(subject, to, text):
    """
    send test email
    """
    if subject is None or to is None or text is None:
        raise click.exceptions.ClickException('Please passing in subject, to and text content')
    return send_email(to=to, subject=subject, text=text)


if __name__ == '__main__':
    runserver()
