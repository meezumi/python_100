from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)
# this func should access the id of the user stored in our database


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():

    if request.method == "POST":

        email = request.form.get("email")
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user:
            flash("you have already signed in using this email, login in.")
            return redirect(url_for('login'))

        passEntered = request.form.get("password")
        hashedPass = generate_password_hash(passEntered, method="pbkdf2:sha256", salt_length=8)
        new_user = User(
            email=request.form.get("email"),
            password=hashedPass,
            name=request.form.get("name"),
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        # this is so the user who registered just now is logged in.
        # return render_template("secrets.html", name=request.form.get("name"))
        return redirect(url_for("secrets"))
        # we want to display the name entered in the form to the secret.html page, so we return the name

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # we can find the user by checking the email entered:
        # which should already be present in the db, if they registered earlier
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # now we need to check if the password entered is correct, as per the email or not:
        # if check_password_hash(user.password, password):
        #     load_user(user)
        #     # where user.password is the hashed password stored in the db and,
        #     # password is what we have entered here (not-hashed)
        #     return redirect(url_for("secrets"))

        if not user:
            flash("you sure buddy u registered earlier with this?")
            # i.e email doesnt exist in the db:
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, password):
            flash("ayo turn the sneaky mode on correctly")
            # i.e entered the wrong password:
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("secrets"))

    return render_template("login.html")


@app.route('/secrets')
@login_required
# this means that secrets.html will only be rendered,
# if the user has logged in
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf", as_attachment=True)
    # as_attachment: directly opens in your downloads to save as, else in new page


if __name__ == "__main__":
    app.run(debug=True)
