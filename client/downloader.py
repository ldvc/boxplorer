#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 sw=4 ts=4 et:

"""
    Download content from boxplorer webui
"""

from __future__ import (unicode_literals, absolute_import,
                                print_function, division)

# standard libs
import sys
from urllib import unquote

try:
    import requests
except ImportError:
    print("requests module not found")

import config
URL_CHOICES = config.url['choices']
USER = config.auth['user']
PWD = config.auth['password']
DEST_DIR = config.dest_dir


#http://stackoverflow.com/a/3041990
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


#http://stackoverflow.com/a/16696317
def download_file(urls):
    for url in urls:
        print(url) 
        local_filename = unquote(url.split('/')[-1])
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True, auth=(USER,PWD))
        with open(DEST_DIR+local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    #f.flush() commented by recommendation from J.F.Sebastian
    #return local_filename


if __name__ == '__main__':
    response = requests.get(URL_CHOICES+USER,verify=True, auth=(USER,PWD))  
    print(URL_CHOICES+USER)
    json_data = response.json()

    if json_data:
        print("\nDownload dir: {}".format(DEST_DIR))
        print("URL: {}".format(URL_CHOICES+USER))
        for k, v in json_data.iteritems():
            print("\n\u2192", k)
            [print("   "+f) for f in v]
        if query_yes_no("Would you like to start downloading?"):
            for tname, urls in json_data.iteritems():
                print("== Start downloading {}".format(tname))
                download_file(urls)
    else:
        print("No choices found, please go to {}".format(config.url['base']))
