from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin
import os


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(length=30), nullable=False, unique=True)
    mail_id = db.Column(db.String(length=50), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=10000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    
    @property
    def pretty_budget(self):
        if len(str(self.budget)) >= 4:
            return f"{str(self.budget)[:-3]},{str(self.budget)[-3:]}"
        else:
            return f"{self.budget}"

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correct(self, attempt_password):
        return bcrypt.check_password_hash(self.password_hash, attempt_password)

    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

    def can_sell(self, item_obj):
        return item_obj in self.items


            

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2108), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'item {self.name}'

    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()
    
    def sell(self, users):
        self.user_id = None
        users.budget += self.price
        db.session.commit()

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        self.generate_barcode()

    def generate_barcode(self):
        barcode_bytes = os.urandom(12)
        barcode_hex = barcode_bytes.hex()
        self.barcode = barcode_hex
 