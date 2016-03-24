from application import app
import os, requests, json, datetime
from flask import Flask, request, abort, redirect, url_for, Response, jsonify
from random import randint

@app.route('/raise', methods = ['GET', 'POST'])
def test():
    test = 'test'
    return Response(json.dumps({'rfc': str(randint(0,99999))}),  mimetype='application/json')


@app.route('/check_service/<service>', methods = ['GET', 'POST'])
def check_service(service):
    return Response(json.dumps({'status': 'Ok'}),  mimetype='application/json')
