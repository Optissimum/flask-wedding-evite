from app import app, database
import model
from flask import (
    render_template, redirect,
    url_for, flash, request,
    jsonify, abort)

@app.route('/',
           methods=['GET', 'POST'])
def rsvp():
    form = model.UserForm(request.form)
    return render_template('index.html', form=form)
