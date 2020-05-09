# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request, Response

# import file
from controller import (morphological_analysis_controllers, update_mecab_dict_controllers)

class urls:
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    @app.route('/', methods=['GET'])
    def index():
        return "Hello World\n"

    @app.route('/v1/morphological-analysis/', methods=['POST'])
    def morphological_analysis():
        morphological_analysis_controller = morphological_analysis_controllers.morphological_analysis_controller()
        return morphological_analysis_controller.morphological_analysis(request)

    @app.route('/v1/update/mecab-dict/', methods=['GET'])
    def update_mecab_dict():
        update_mecab_dict_controller = update_mecab_dict_controllers.update_mecab_dict_controller()
        return update_mecab_dict_controller.update_mecab_dict()

    @app.errorhandler(400)
    @app.errorhandler(404)
    @app.errorhandler(500)
    def error_handler(error):
        response = jsonify(
            {
                "code": error.code,
                "status": error.code,
                "result": {
                    'error_name': error.name,
                    'type': error.description
                }
            }
        )
        return response