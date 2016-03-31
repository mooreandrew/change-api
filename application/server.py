from application import app
import os, requests, json, datetime
from flask import Flask, request, abort, redirect, url_for, Response, jsonify
from random import randint

notes = ''

@app.route('/', methods = ['GET', 'POST'])
def test():
    return(notes)

@app.route('/raise', methods = ['GET', 'POST'])
def raiseweb():
    request_data = request.get_json(force=True)

    test = 'test'
    rfc = str(randint(0,99999))

    add_note('RFC ' + rfc + ' raised with title "' + request_data['description'] + '"')
    return Response(json.dumps({'rfc': rfc}),  mimetype='application/json')


@app.route('/check_service/<service>', methods = ['GET', 'POST'])
def check_service(service):
    add_note('Checking status of ' + service)
    return Response(json.dumps({'status': 'Ok'}),  mimetype='application/json')

@app.route('/change_id/<rfc>', methods = ['GET'])
def get_change_id(rfc):
    rfc = str(randint(0,99999))
    return Response(json.dumps({'status': 'Ok', 'change_id': rfc}),  mimetype='application/json')

@app.route('/update/add_note', methods = ['GET', 'POST'])
def add_note():
    request_data = request.get_json(force=True)
    print(request_data['rfc'])
    print(request_data['note'])
    add_note('Adding Note "' + request_data['note'] + '" for rfc ' + str(request_data['rfc']))

    return Response(json.dumps({'status': 'Ok'}),  mimetype='application/json')

@app.route('/close', methods = ['GET', 'POST'])
def close():
    request_data = request.get_json(force=True)
    print(request_data['rfc'])
    add_note('Closing rfc ' + str(request_data['rfc']))
    return Response(json.dumps({'status': 'Ok'}),  mimetype='application/json')

def add_note(note):
    global notes
    notes = notes + note + '<br><br>'
    print(notes)

@app.route('/update/add_outcome', methods = ['GET', 'POST'])
def add_outcome():
    request_data = request.get_json(force=True)
    print(request_data['rfc'])
    add_note('Adding Outcome "' + request_data['outcome'] + '" for rfc ' + str(request_data['rfc']))
    return Response(json.dumps({'status': 'Ok'}),  mimetype='application/json')

@app.route('/update/description', methods = ['GET', 'POST'])
def update_description():
    request_data = request.get_json(force=True)
    print(request_data['rfc'])
    add_note('Updateing Description for ' + str(request_data['rfc']) + ' - "' + request_data['description'] + '"')
    return 'ok'
