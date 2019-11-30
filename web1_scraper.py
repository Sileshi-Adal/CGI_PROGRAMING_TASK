#!/usr/bin/env python
# coding: utf-8

import re, ssl
import os
import sys
import urllib.request as request
from signal import signal, SIGINT
from datetime import datetime
import time
import yaml


class Web_scraper():
    """
    Web_scraper accepts .yaml file as an argument.
    """

    def __init__(self, input_file, url_access, regex_access, output_file='Result_output.txt'):
        """Initializing web_scraper class 

        Args: 
            input_file: an input file in .yaml format, which lists of URLs and regex will be given 
            url_access: access to retrieve URLs from input_file 
            regex_access: access to retrieve REGEXs from input_file
            output_file: file name that will be saved as an output

        """
        self.input_file = input_file
        self.url_access = url_access
        self.regex_access = regex_access
        self.output_file = output_file

    def fetch_web_cont(self):

        with open(self.input_file) as input_file:
            data = yaml.load(input_file, yaml.FullLoader)
            url_list = data.get(self.url_access)
            regex_list = data.get(self.regex_access)

        print('Fetching data:')

        for url in url_list:
            # This restores the same behavior as before.
            context = ssl._create_unverified_context()
            
            run_time = datetime.now().strftime("Date: %d-%m-%Y Time: %I:%M:%S:%f_%p")
            start = time.perf_counter()
            # web_req = request.Request(url)
            web_resp = request.urlopen(url, context=context)
            respData = web_resp.read()
            resp_time = '%0.2f s' % (time.perf_counter() - start)

            for regex in regex_list:
                contents = re.findall(regex, str(respData))
                with open(self.output_file, 'a') as file:
                    if not contents:
                        print(run_time, ' | URL: ', url, '| content not found with this regex: ', regex,
                              file=file)

                    else:
                        for content in contents:
                            print(run_time, ' | URL: ', url, ' | Response Time: ', resp_time,
                                  url, ' | Contents: ', content, file=file)
        with open(self.output_file, 'a') as file:
            
            print('\n#################################\n', file=file)


def main():
    input_ = sys.argv[1]
    result = Web_scraper(input_, 'URLs', 'RegEx')
    result.fetch_web_cont()

    


if __name__ == '__main__':
    fetch_count = {'fetch_count': 1}
    def handler(signal_received, frame):
        print(' Program terminated after %d web Scraping round.' %
              fetch_count['fetch_count'])
        sys.exit(0)
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)
    print(' Web scraping starting... "CTRL - C" to terminate scraping.')
    # Runs the program every 5 seconds.
    while True:
        main()
        print(' Web Fetching  {} complete.'.format(fetch_count['fetch_count']))
        fetch_count['fetch_count'] += 1
        time.sleep(5)
