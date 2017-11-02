import validators
import subprocess

class U:
    def generate_url(url, url_id):
        validate_url(url)
        check_id_availability(url_id)
        # check git status, unclean state
        # create url
        # create folder, cp html file in that folder with format
        subprocess.check_output(['mkdir ' + url_id + '&& cd ' + url_id])
        subprocess.check_output(['echo "some data for the file" >> fileName']) # redirect code
        # return url from constants file, open url, return url to CL
  
    def validate_url(url):
        if validators.url(url):
            return True
        else:
            raise ValueError('Invalid URL format. Please try again.')
  
    def check_id_availability(url_id):
        # check branch, git status, git push
        # write current dir
        # check 404?
        subprocess.check_output(['[ -d "YOUR_DIR" ] && echo "is a dir"'])
        pass
  
    def update_all():
        #search directory
        #update all dir
        #update urls
        #list urls
        pass

if __name__ == "__main__":
    if (len(sys.argv) == 3):
        url = sys.argv[1]
        url_id = sys.argv[2]
        generate_url(url, url_id)
    else:
        raise ValueError('Invalid command. Try the following command\
                          format:\n \t u https://google.com google')
