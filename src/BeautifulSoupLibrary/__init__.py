#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

__version__ = '0.1'

from bs4 import BeautifulSoup
import re

class BeautifulSoupLibrary(object):

    __all__ = ['find', 'findAll', 'select', 'create_regex']

    def __init__(self):
        pass

    def find(self, search_text, name=None, attrs={}, recursive=True, text=None, **kwargs):
        soup = BeautifulSoup(search_text)
        return soup.find(name, attrs, recursive, text, **kwargs)

    def findAll(self, search_text, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs):
        soup = BeautifulSoup(search_text)
        return soup.findAll(name, attrs, recursive, text, limit, **kwargs)

    def select(self, search_obj, expr=None, attrs={}):
        return search_obj.select(expr)

    def create_regex(self, string):
        return re.compile(string)

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
