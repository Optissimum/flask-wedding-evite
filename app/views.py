from app import app, database
import model
from flask import (
    render_template, redirect,
    url_for, flash, request)
from contextlib import contextmanager

color_scheme = model.Settings.query.first()


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
        saved_info = model.Settings.query.order_by(
            model.Settings.id.desc()).first()
        try:
            ptrlist = saved_info.partners
            partners = [x.strip() for x in ptrlist.split(',')]
            print partners
        except:
            return redirect(url_for('settings'))
        if request.method == 'POST' and form.validate_on_submit():
            guest = model.Guest(form.name.data,
                                form.email.data,
                                form.plusone.data,
                                form.address.data,
                                form.limitations.data,
                                form.rsvp.data)
            session.add(guest)
        return render_template('evite.html',
                               form=form,
                               colors=scheme_creator(),
                               partners=partners,
                               date=saved_info.date,
                               time=saved_info.time,
                               address=saved_info.address)


@app.route('/guests/',
           methods=['GET', 'POST'])
def guest_list():
    with database_session() as session:
        guests = model.Guest.query.all()
        return render_template('guestlist.html',
                               guests=guests,
                               colors=scheme_creator())


@app.route('/settings/',
           methods=['GET', 'POST'])
def settings():
    with database_session() as session:
        saved_info = model.Settings.query.order_by(
            model.Settings.id.desc()).first()
        options = model.SettingsForm(obj=saved_info)
        if request.method == "POST" and options.validate_on_submit():
            setting = model.Settings(
                options.partners.data,
                options.date.data,
                options.time.data,
                options.address.data,
                options.color_main.data,
                options.color_acc1.data,
                options.color_acc2.data,
                options.color_acc3.data,
                options.color_acc4.data)
            session.add(setting)
        return render_template('settings.html',
                               options=options,
                               colors=scheme_creator(),
                               date=saved_info.date,
                               time=saved_info.time)


def scheme_creator():
    settings = model.Settings.query.order_by(
        model.Settings.id.desc()).first()
    if (settings):
        palette = [settings.color_main,
                   settings.color_acc1,
                   settings.color_acc2,
                   settings.color_acc3,
                   settings.color_acc4]
    else:
        palette = ['#735425',
                   '#53380F',
                   '#BD8A3D',
                   '#B59565',
                   '#321E01']
    compliments = [color_match_gen(x) for x in palette]
    return {'palette': palette, 'compliments': compliments}


def color_match_gen(color):
    rgb_list = [color[x:x + 2] for x in [1, 3, 5]]
    new_rgb = [int(color, 16) + 65 for color in rgb_list]
    new_rgb = [min([255, max([0, i])]) for i in new_rgb]
    return "#" + "".join([hex(i)[2:] for i in new_rgb])
