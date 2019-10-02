"""
Here routes of the current blueprint are initializing.
For adding new endpoint, add new resource with the reference to specific class (in routes.py) and path.
"""

from flask import Blueprint
from flask_restful import Api

from .routes import RegisterResources

processing = Blueprint('processing', __name__)
processing_api = Api(processing)

processing_api.add_resource(RegisterResources, '/')
