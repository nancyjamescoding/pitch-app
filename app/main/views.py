from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Pitch, Comment
from .forms import PitchForm, CommentForm, UpdateProfile
from .. import db, photos
from flask_login import login_required, current_user


@main.route('/')
def index():
    technology = Pitch.get_pitches('technology')
    travels = Pitch.get_pitches('travels')
    sports = Pitch.get_pitches('sports')

    return render_template('index.html', technology=technology, travels=travels, sports=sports)


@main.route('/pitches/technology')
def technology():
    pitches = Pitch.get_pitches('technology')

    return render_template('tech.html', pitches=pitches)


@main.route('/pitches/travels')
def travels():
    pitches = Pitch.get_pitches('travels')

    return render_template('travels.html', pitches=pitches)


@main.route('/pitches/sports')
def sports():
    pitches = Pitch.get_pitches('sports')

    return render_template('sports.html', pitches=pitches)


@main.route('/new/pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data

        new_pitch = Pitch(body=title, content=pitch, category=category,
                          user=current_user, likes=0, dislikes=0)

        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'new.pitch'

    return render_template('newpitch.html', title=title, pitch_form=pitch_form)


@main.route('/pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def pitch(id):
    pitch = Pitch.get_pitch(id)
    posted_date = pitch.timestamp.strftime('%b %d,%Y')

    if request.args.get('likes'):
        pitch.likes = pitch.likes+1

        db.session.add(pitch)
        db.session.commit()
        return redirect('/pitch/{pitch_id}'.format(pitch_id=pitch.id))

    elif request.args.get('dislikes'):
        pitch.dislikes = pitch.dislikes+1

        db.session.add(pitch)
        db.session.commit()
        return redirect('/pitch/{pitch_id}'.format(pitch_id=pitch.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data
        new_comment = Comment(
            comment=comment, user=current_user, pitch_id=pitch)
        new_comment.save_comments()

    comments = Comment.get_comments(pitch)
    return render_template('action.html', pitch=pitch, comment_form=comment_form, comment=comments, date=posted_date)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))
