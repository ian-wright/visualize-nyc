from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["DEBUG"] = True # what does this do?
# dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ianwright:sbdbpw#2@ianwright.mysql.pythonanywhere-services.com:3306/ianwright$viznyc_atrain'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# ----------------------------------------
# ------------ DB MODEL SETUP ------------
# ----------------------------------------

# joint table
class Joint(db.Model):
    joint_int_id = db.Column(db.Integer, primary_key=True)
    joint_str_id = db.Column(db.String(80))
    address = db.Column(db.String(60))
    name = db.Column(db.String(80))

    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))

    stations = db.relationship('Station', secondary=station_joint,
        backref=db.backref('joints', lazy='select'))
        # maybe backref lazy should be joined

    categories = db.relationship('Station', secondary=station_joint,
        backref=db.backref('joints', lazy='select'))

    def __init__(self, joint_int_id, address, joint_id, name):
        self.joint_int_id = joint_int_id
        self.joint_str_id = joint_id
        self.address = address
        self.name = name

    def __repr__(self):
        return '<Joint: %r>' % self.name

# category table
class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20))
    parent_category = db.Column(db.String(20))

    def __init__(self, category_id, category, parent_category):
        self.category_id = category_id
        self.category = category
        self.parent_category = parent_category

    def __repr__(self):
        return '<Category: %r>' % self.category

# station table
class Station(db.Model):
    station_id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    name = db.Column(db.String(40))

    def __init__(self, station_id, lat, lon, name):
        self.station_id = station_id
        self.lat = lat
        self.lon = lon
        self.name = name

    def __repr__(self):
        return '<Station: %r>' % self.name

# station_joint map
station_joint = db.Table('station_joint',
    db.Column('station_id', db.Integer, db.ForeignKey('station.station_id')),
    db.Column('joint_int_id', db.Integer, db.ForeignKey('joint.joint_int_id')),
    db.PrimaryKeyConstraint('station_id', 'joint_int_id')
)

# joint_category map
joint_category = db.Table('joint_category',
    db.Column('category_id', db.Integer, db.ForeignKey('category.category_id')),
    db.Column('joint_int_id', db.Integer, db.ForeignKey('joint.joint_int_id')),
    db.PrimaryKeyConstraint('category_id', 'joint_int_id')
)



# ----------------------------------------
# ---------------- ROUTES ----------------
# ----------------------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/atrain/")
def atrain():
	return render_template("atrain.html",
		banana='Jeremiah')
	print('rendered a thing')

# don't need this when running app from pythonanywhere
#if __name__ = '__main__':
#    app.run()