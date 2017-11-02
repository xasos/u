#!/usr/bin/python
import validators
import os
import sys
  
class U:
    def _get_file_path_for_url_id(self, url_id, file_name):
      return '{}/{}'.format(url_id, file_name)
   
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
  
        # return url from constants file, open url, return url to CL

    def validate_url(self, url):
        if validators.url(url):
            return True
        else:
            raise ValueError('Invalid URL format. Please try again.')
  
    def check_id_availability(self, url_id):
        # check branch, git status, git push
        # write current dir
        # check 404?
        return not os.path.exists(url_id)
  
    def update_all(self):
        #search directory
        #update all dir
        #update urls
        #list urls
        pass

if __name__ == "__main__":
    if (len(sys.argv) == 3):
        url = sys.argv[1]
        url_id = sys.argv[2]
        u = U()
        u.generate_url(url, url_id)
    else:
        raise ValueError('Invalid command. Try the following command\
                          format:\n \t u https://google.com google')
