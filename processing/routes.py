from flask import jsonify
from flask_restful import Resource

from .parser import proc_parser
from ..script import run_func


class RegisterResources(Resource):
    """
    Main Resource for RESTful API. Name was picked up randomly.
    get method could be used to test of proper working of app and endpoint from web-browser.
    post method could be used from postman or similar program to get the results of app work.
    """

    def get(self):
        return 'Hello world'

    def post(self):
        args = proc_parser.parse_args()
        link = args['link']
        commit = args['commit']
        number = args['number']
        return jsonify(run_func(link, commit, number))
