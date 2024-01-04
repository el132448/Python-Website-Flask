from flask import Blueprint, render_template, request, flash, jsonify
# current_user: can get data of current user when login
from flask_login import  login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

# methods=['GET', 'POST']: allows this page to use GET, POST
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short.', category='error')
        else:
            # add the new note to database
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added.', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    # take in some data from POST request
    # and turn the string into a python dictionary
    note = json.loads(request.data)
    # access the noteId attribute from JavaScript
    noteId = note['noteId']
    note = Note.query.get(noteId)
    # check if the note with that noteId exist
    if note:
        # check if the note is owned by the current user
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted.', category='success')

    # return an empty response (just need to return something as requirement of Flask)
    return jsonify({})