from flask import Blueprint, request, jsonify
from src.constants.http_status_codes import HTTP_200_OK

compare = Blueprint('compare', __name__, url_prefix='/api/compare')

@compare.get('/search')
def search():
    return {'msg': 'what you want to compare'}, HTTP_200_OK

@compare.get('/history')
def history():
    return {'msg': 'your history'}, HTTP_200_OK