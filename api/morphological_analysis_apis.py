# -*- coding:utf-8 -*-

import MeCab

class part_of_speech:
    def __init__(self,
                 one: str,
                 two: str,
                 three: str):
        self.one = one
        self.two = two
        self.three = three

class morphological_analysis_api_model:
    def __init__(self,
            hiragana: str,
            kana: str,
            kanji: str,
            part_of_speech: part_of_speech
        ):
        self.hiragana = hiragana
        self.kana = kana
        self.kanji = kanji
        self.part_of_speech = part_of_speech


class morphological_analysis_api:
    def mecab(self, word: str) -> list:
        mecab = MeCab.Tagger()
        result_list = []

        for result in mecab.parse(word).split("\n"):
            to_put_mecab_result_in_order = self.__to_put_mecab_result_in_order__(result)
            if(to_put_mecab_result_in_order):
                result_list.append(to_put_mecab_result_in_order.__dict__)
        return result_list

    def __to_put_mecab_result_in_order__(self, mecab_result: str) -> morphological_analysis_api_model:
        if(len(mecab_result) == 0):
            return None
        if(mecab_result == 'EOS'):
            return None

        mecab_result_detail = mecab_result.split("\t")
        if(len(mecab_result_detail) != 8):
            return None

        part_of_speech = self.__to_put_part_of_speech_result__(mecab_result_detail[4])
        result = morphological_analysis_api_model(
            hiragana = mecab_result_detail[0],
            kana = mecab_result_detail[1],
            kanji = mecab_result_detail[3],
            part_of_speech = part_of_speech.__dict__)
        return result

    def __to_put_part_of_speech_result__(self, part_of_speechs: str) -> part_of_speech:
        part = part_of_speechs.split("-")
        if(len(part) == 1):
            return part_of_speech(one=part[0], two=None, three=None)
        if(len(part) == 2):
            return part_of_speech(one=part[0], two=part[1], three=None)
        if(len(part) == 3):
            return part_of_speech(one=part[0], two=part[1], three=part[2])
        return None