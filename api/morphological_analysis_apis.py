# -*- coding:utf-8 -*-

import MeCab

class morphological_analysis_api_model:
    def __init__(self, 
            word: str, 
            part_of_speech: str,
            part_of_speech_classification_one: str,
            part_of_speech_classification_two: str,
            part_of_speech_classification_three: str,
            practical_type: str,
            practical: str,
            origin_word: str,
            reading: str,
            phonation: str
        ):
        self.word = word
        self.part_of_speech: str = part_of_speech
        self.part_of_speech_classification_one = part_of_speech_classification_one
        self.part_of_speech_classification_two = part_of_speech_classification_two
        self.part_of_speech_classification_three = part_of_speech_classification_three
        self.practical_type = practical_type
        self.practical = practical
        self.origin_word = origin_word
        self.reading = reading
        self.phonation = phonation

class morphological_analysis_api:
    def mecab(self, word: str) -> list:
        mecab = MeCab.Tagger()
        result_list = []

        for result in mecab.parse(word).split("\n"):
            to_put_mecab_result_in_order = self.__to_put_mecab_result_in_order__(result)
            if(to_put_mecab_result_in_order == None):
                break
            
            result_list.append(to_put_mecab_result_in_order.__dict__)

        return result_list
        

    def __to_put_mecab_result_in_order__(self, mecab_result: str) -> morphological_analysis_api_model:
        if(mecab_result == 'EOS'):
            return None

        mecab_result_detail = mecab_result.split("\t")
        if(len(mecab_result_detail) != 2):
            return None

        part_of_speech_detail = mecab_result_detail[1].split(",")
        if(len(part_of_speech_detail) != (9 or 7)):
            return None

        return morphological_analysis_api_model(
            mecab_result_detail[0],
            part_of_speech_detail[0],
            part_of_speech_detail[1],
            part_of_speech_detail[2],
            part_of_speech_detail[3],
            part_of_speech_detail[4],
            part_of_speech_detail[5],
            part_of_speech_detail[6],
            "*" if len(part_of_speech_detail) == 7 else part_of_speech_detail[7],
            "*" if len(part_of_speech_detail) == 7 else part_of_speech_detail[8]
        )