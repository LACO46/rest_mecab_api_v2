# -*- coding:utf-8 -*-
from enum import Enum
import os
import subprocess


class update_mecab_result(Enum):
    fail = 1
    success = 2

class update_mecab_dict_api:
    base_dir = '/'
    api_dir = 'home/'
    mecab_dict_dir = 'mecab-ipadic-neologd/'

    def update_mecab_dict(self) -> update_mecab_result:
        os.chdir(self.base_dir)
        os.chdir(self.mecab_dict_dir)

        try:
            subprocess.check_call('pwd')
            subprocess.check_call('git pull origin master', shell=True)
            subprocess.check_call('bin/install-mecab-ipadic-neologd -n -y', shell=True)
        except:
            return update_mecab_result.fail
        return update_mecab_result.success
