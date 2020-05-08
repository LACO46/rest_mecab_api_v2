  
# -*- coding:utf-8 -*-

# import file
from api import morphological_analysis_apis

class morphological_analysis_logic_model:
    def __init__(self, result: list):
        self.result = result

class morphological_analysis_logic:
    def morphological_analysis(self, word: str) -> morphological_analysis_logic_model:
        morphological_analysis_api = morphological_analysis_apis.morphological_analysis_api()
        result = morphological_analysis_api.mecab(word)
        return morphological_analysis_logic_model(result)