# -*- coding:utf-8 -*-

# import file
from api import update_mecab_dict_apis

class update_mecab_dict_logic:
    def update_mecab_dict(self) -> bool:
        # 変数を定義
        update_mecab_dict_api = update_mecab_dict_apis.update_mecab_dict_api()

        # apiの呼び出し
        result = update_mecab_dict_api.update_mecab_dict()
        return update_mecab_dict_apis.update_mecab_result.success == result