from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for,make_response
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.login import login_required,current_user,logout_user

from apps import db,loginmanager,app
from apps.Account.forms import RegisterForm, LoginForm
from apps.Account.models import User
#from apps.Account.decorators import requires_login

bp_user = Blueprint('account', __name__, url_prefix='/account',template_folder='templates')

@loginmanager.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user


@bp_user.route('/profile/')
@login_required
def home():
	return render_template("profile.html", user=g.user)

@bp_user.route('/logout/',methods=['GET'])
@login_required
def logout():
	logout_user()
	return redirect('/')

@bp_user.route('/login/', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		login_user(user)
		flash("Logged in successfully.")
		return redirect(request.args.get("next") or url_for("index"))
	return render_template("login.html", form=form)

@bp_user.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User(name=form.username.data,email=form.email.data,password=generate_password_hash(form.password.data))
			db.session.add(user)
			db.session.commit()
			session['user_id'] = user.id
			flash('Thanks for registering')
			return redirect(url_for('account.home'))
	return render_template("register.html", form=form)