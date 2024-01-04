from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # a function in the class to convert the table into a dictionary
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)

        return dictionary


# creating the tables
with app.app_context():
    db.create_all()

# the database already contains a lot of entries in it by default, so
# no need to enter records


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def get_random_cafe():
    # to select a cafe from the table we fetch it using:
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    print(random_cafe)
    # return f"<h3> Random Cafe is: {random_cafe.name} </h3>"
    #                           OR
    # manually creating a json
    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    # })
    #                           OR
    return jsonify(random_cafe.to_dict())

# in most cases, you might just want to return all the data you
# have on a particular record, and it would drive you crazy if you had
# to write out all that code for every route.
#
# So another method of serialising our database row Object to
# JSON is by first converting it to a dictionary and
# then using jsonify() to convert the dictionary
# (which is very similar in structure to JSON) to a JSON.


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record

@app.route('/all', methods=["GET"])
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    list_of_cafes = []
    for cafe in all_cafes:
        list_of_cafes.append(cafe.to_dict())
    return jsonify(cafes=list_of_cafes)
    # or we could have used list comprehension i.e:
    # return jsonify(cafes=[cafe.to_dict() fro cafe in all_cafes])


@app.route('/search')
def get_cafe_at_location():
    query_loc = request.args.get("loc")
    # the args can be found mentioned in the url too
    # here loc is the parameter added to the url by the user, for exp:
    # & to join words and ? to define a parameter is being added
    # 127.0.0.1/5000/search?loc=London&Bridge

    all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == query_loc)).scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Dont have cafes at this location"})


@app.route('/add', methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(

        # what is the difference between request.form["name"] and
        # request.form.get("name") ?

        # name=request.form["name"] OR
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
# if we are using /<something_value> in the url, then it is passed as
# parameter in the function of the route, exp:
def coffee_price_update(cafe_id):
    new_prize = request.args.get("new_prize")
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_prize
        db.session.commit()
        return jsonify(response={"success": "successfully updated"}), 200
        # OK
    else:
        return jsonify(response={"error": "the cafe id is not present"}), 404
        # NOT FOUND


@app.route('/report-closed/<int:cafe_id>', methods=["DELETE"])
def delete_cafe_info(cafe_id):
    check_api = request.args.get("api-key")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        if check_api == "TopSecretAPIKey":
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(responce={"success": "successfully deleted the cafe"}), 200
        else:
            return jsonify(responce={"error": "wrong api-key entered"}), 403
    else:
        return jsonify(responce={"error": "id not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
