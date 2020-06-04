import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from flask.views import MethodView
from werkzeug.exceptions import abort
from ..models.Photos import Photo


photooapi = Blueprint('photoapi', __name__, url_prefix='/photo')

