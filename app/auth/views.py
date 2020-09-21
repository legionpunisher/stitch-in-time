from flask import render_template
from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from ..models import Pitches, User, Comments
from . import main
from .. import db,photos
from .forms import PitchForm,CommentForm, UpdateProfile