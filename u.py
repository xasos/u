#!/usr/bin/python

from math import floor
import string
import validators
import os
import sys

class U:
    def __init__(self):
        pass

    def _get_file_path_for_url_id(self, url_id, file_name):
      return '{}/{}'.format(url_id, file_name)

    def toBase62(self, num, b = 62):
        if b <= 0 or b > 62:
            return 0
        base = string.digits + string.lowercase + string.uppercase
        r = num % b
        res = base[r];
        q = floor(num / b)
        while q:
            r = q % b
            q = floor(q / b)
            res = base[int(r)] + res
        return res
    
    def toBase10(self, num, b = 62):
        base = string.digits + string.lowercase + string.uppercase
        limit = len(num)
        res = 0
        for i in xrange(limit):
            res = b * res + base.find(num[i])
        return res

    def generate_url(self, url, url_id):
        self.validate_url(url)
        self.check_id_availability(url_id)
        # check git status, unclean state
        # create url
        # create folder, cp html file in that folder with format
        directory_name = url_id
        # TODO: @xasos: implement file name logic
        file_name = 'fileName'
        if not os.path.exists(url_id):
            os.makedirs(url_id)
        file_path = self._get_file_path_for_url_id(url_id, file_name)
        with open(file_path, 'w') as f:
            # TODO: @xasos implement this to actually save real data
            f.write('data')

    def generate_url(self, url, url_id):
        validate_url(url)
        check_id_availability(url_id)
        # check git status, unclean state
        # create url
        # create folder, cp html file in that folder with format
        subprocess.check_output(['mkdir ' + url_id + '&& cd ' + url_id])
        subprocess.check_output(['echo "some data for the file" >> fileName']) # redirect code
        # return url from constants file, open url, return url to CL

    def create_file(self):
        pass

    def read_file(self, value):
        pass

    def write_file(self, value):
        pass

    def validate_url(self, url):
        if validators.url(url):
            return True
        else:
            raise ValueError('Invalid URL format. Please try again.')

    def check_id_availability(self, url_id):
        # check branch, git status, git push
        # write current dir
        # check 404?
        subprocess.check_output(['[ -d "YOUR_DIR" ] && echo "is a dir"'])
        pass

    def validate_url(self, url):
        if validators.url(url):
            return True
        else:
            raise ValueError('Invalid URL. Please try again.')

    def check_id_availability(self, url_id):
        # check file
        return not os.path.exists(url_id)

    def update_all(self):
        #search directory
        #update all dir
        #update urls
        #list urls
        pass

if __name__ == "__main__":
    u_client = U()
    #if (len(sys.argv) == 3):
    #    url = sys.argv[1]
    #    url_id = sys.argv[2]
    #    u = U()
    #    u.generate_url(url, url_id)
    #else:
    #    raise ValueError('Invalid command. Try the following command\
    #                      format:\n \t u https://google.com google')
