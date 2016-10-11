from app import app, database
import model
from flask import (
    render_template, redirect,
    url_for, flash, request)
from contextlib import contextmanager

@contextmanager
def database_session():
    """Provide a clean way to access our database."""
    session = database.session()
    try:
        yield session
        session.commit()
        session.flush()
    except:
        session.rollback()
        raise
    finally:
        session.close()

@app.route('/',
           methods=['GET', 'POST'])
def rsvp():
    with database_session() as session:
        form = model.UserForm(request.form)
        if request.method == 'POST':
            form.validate_on_submit()
            guest = model.Guest(form.name.data,
            form.email.data,
            form.plusone.data,
            form.address.data,
            form.limitations.data,
            form.rsvp.data)
            session.add(guest)
        return render_template('index.html', form=form)

@app.route('/guests/',
           methods=['GET', 'POST'])
def guest_list():
    with database_session() as session:
        guests = model.Guest.query.all()
