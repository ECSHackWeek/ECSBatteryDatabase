import datetime as dt
from flask import Blueprint, jsonify
from .orm import ElectrolyteComponent

api = Blueprint('api', __name__,
                static_folder="static/dist",
                template_folder="static")


@api.route('/addElectrolyte')
def addElectrolyte():
    ec = ElectrolyteComponent(created_date=dt.datetime.now(),
                              component='ethylene carbonate',
                              name='EC', smiles='something')

    return jsonify(ec)
