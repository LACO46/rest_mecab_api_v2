# -*- coding:utf-8 -*-

from flask import jsonify

# import file
from logic import update_mecab_dict_logics

class update_mecab_dict_controller:
    def update_mecab_dict(self):
        # 変数を定義
        update_mecab_dict_logic = update_mecab_dict_logics.update_mecab_dict_logic()

        # logicの呼び出し
        result = update_mecab_dict_logic.update_mecab_dict()

        if(not result):
            return jsonify({'message': 'update mecab dict failed'}), 500

        return jsonify({'message': 'update mecab dict succeed'}), 200