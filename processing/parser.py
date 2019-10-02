"""
Here incoming data structure is described.
To add parameter to income JSON, .add_argument function should be used.
"""

from flask_restful import reqparse

proc_parser = reqparse.RequestParser()
proc_parser.add_argument('link')
proc_parser.add_argument('commit')
proc_parser.add_argument('number')
