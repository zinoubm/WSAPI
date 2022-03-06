from flask import Blueprint, request, jsonify
from src.constants.http_status_codes import HTTP_200_OK

auth = Blueprint("auth", __name__, url_prefix = "/api/auth")


@auth.get('/register')
def register():
    return {'msg': 'not implemented'}, HTTP_200_OK

@auth.get('/login')
def login():
    return {'msg': 'this is login'}, HTTP_200_OK

@auth.get('/dashboard')
def dashboard():
    return {'msg': 'this is dash board'}, HTTP_200_OK