from market import app
from flask import render_template,url_for,redirect, flash,request
from market.models import Item, User
from market.forms import Register_form,login_form, purchaseItemForm, SellItemForm
from market import db
from flask_login import login_user , logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')




@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = purchaseItemForm()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!", category='danger')

        

    items = Item.query.all()
    return render_template('market.html', items=items, purchase_form=purchase_form)


    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = Register_form()
    if form.validate_on_submit():
        user_to_create = User(
            user_name=form.user_name.data,
            mail_id=form.mail_id.data,
            password=form.password1.data
        )
        db.session.add(user_to_create)  # Add the user to the session
        db.session.commit()  # Commit the user to the database
        login_user(user_to_create)
        flash(f"Account created successfully! you are logged in as {user_to_create.user_name}",category='success')

        return redirect(url_for('market_page'))

    if form.errors:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)



@app.route('/login', methods=['GET','POST'])
def login_page():
    form = login_form()
    if form.validate_on_submit():
        attempt_user = User.query.filter_by(user_name=form.user_name.data).first()
        # if attempt_user and attempt_user.check_password_correct(attempt_password=form.password.data):
        if attempt_user and attempt_user.check_password_correct(
                attempt_password=form.password.data
        ):
            login_user(attempt_user)
            flash(f'Success! You are logged in as: {attempt_user.user_name}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash("Username and password do not match", category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('home_page'))

@app.route('/terms')
def terms_of_service():
    return render_template('terms.html')

@app.route('/privacy ')
def privacy_policy():
    return render_template('privacy.html')
