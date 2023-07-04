from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Beverage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))


    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/beverage')
def get_beverages():
    beverages = Beverage.query.all()
    output = []
    for beverage in beverages:
        beverage_data = {'name': beverage.name, 'description': beverage.description}
        output.append(beverage_data)

    return {'beverage': output}


@app.route('/beverages/<id>')
def get_beverages(id):
    beverage = Beverage.query.get_or_404(id)
    return {'name': beverage.name, "description": beverage.description}


@app.route('/beverages', methods = ['POST'])
def add_beverage():
    beverage = Beverage(name = request.json['name'], description = request.json['description'])
    db.session.add(beverage)
    db.session.commit()
    return {'id': beverage.id}

@app.route('/beverages/<id>', methods = ['DELETE'])
def delete_beverage():
    beverage = Beverage.query.get(id)
    if beverage is None:
        return  {'error': 'not found'}
    db.session.delete(beverage)
    db.session.commit()
    return {'message': 'Done..!!'}


           

