  
# -*- coding:utf-8 -*-

# import file
from api import morphological_analysis_apis

class morphological_analysis_logic_model:
    def __init__(self, result: list):
        self.result = result

class morphological_analysis_logic:
    def morphological_analysis(self, word: str) -> morphological_analysis_logic_model:
        # 変数の定義
        morphological_analysis_api = morphological_analysis_apis.morphological_analysis_api()

        # MeCab APIの呼び出し
        result = morphological_analysis_api.mecab(word)
        return morphological_analysis_logic_model(result)