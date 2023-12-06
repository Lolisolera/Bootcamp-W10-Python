from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__, static_url_path="/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filmflix.db'
db = SQLAlchemy(app)
api = Api(app)

class Film(db.Model):
    filmID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    duration = db.Column(db.Integer)
    genre = db.Column(db.String(255))

    def __repr__(self):
        return f"<Film {self.filmID}: {self.title}>"

# Existing routes for rendering HTML pages and handlers endpoints

@app.route("/")
def base():
    return render_template("base.html")



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Handle POST request
        # ...
        return "Add a film."
    else:
        # Handle GET request (render template, etc.)
        return render_template("add.html")



@app.route("/delete", methods=["GET", "DELETE"])
def delete():
    return render_template("delete.html")



@app.route("/menu", methods=["GET"])
def menu():
    return render_template("menu.html")


@app.route("/reports", methods=["GET"])
def reports():
    return render_template("reports.html")


@app.route("/update", methods= ["GET", "PUT"])
def update():
    return render_template("update.html")


@app.route("/read", methods=["GET", "DELETE"])
def read():
    return render_template("read.html")

@app.route("/exit", methods=["GET"])
def exit():
        return render_template("exit.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


# Create your API resources
class FilmResource(Resource):
    def get(self, film_id):
        film = Film.query.get_or_404(film_id)
        # You can customize the response format as needed
        return {'filmID': film.filmID, 'title': film.title, 'year': film.year, 'rating': film.rating,
                'duration': film.duration, 'genre': film.genre}

    def delete(self, film_id):
        film = Film.query.get_or_404(film_id)
        db.session.delete(film)
        db.session.commit()
        return '', 204

class FilmListResource(Resource):
    def get(self):
        films = Film.query.all()
        return [{'filmID': film.filmID, 'title': film.title, 'year': film.year, 'rating': film.rating,
                 'duration': film.duration, 'genre': film.genre} for film in films]

    def post(self):
        data = request.get_json()
        new_film = Film(title=data.get('title'), year=data.get('year'), rating=data.get('rating'),
                        duration=data.get('duration'), genre=data.get('genre'))
        db.session.add(new_film)
        db.session.commit()
        return {'filmID': new_film.filmID, 'title': new_film.title, 'year': new_film.year,
                'rating': new_film.rating, 'duration': new_film.duration, 'genre': new_film.genre}, 201

# Add resources to the API
api.add_resource(FilmListResource, '/films')
api.add_resource(FilmResource, '/films/<int:film_id>')

if __name__ == '__main__':
    with app.app_context():
        # Create the database tables
        db.create_all()
    # Run the Flask app
    app.run(debug=True, host="0.0.0.0")
