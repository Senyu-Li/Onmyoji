import json
import sys
import csv
import re
import time
import ast
import math
import requests 



def main():
    
    print(requests.__version__)
    r = requests.get('https://raw.githubusercontent.com/Senyu-Li/Onmyoji/master/lab1.py')
    print(r.text)

if __name__ == '__main__':
    main()
