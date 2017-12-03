import webbrowser
import sys
import re


class ModuleAnalysis:

    def __init__(self, _module):
        self.module = _module
        self.pattern = re.compile('__(.*)__')

    def display_available_functions(self):

        print('Function: ', '                  Result:')
        for func in self.module.__dict__:
            if type(getattr(self.module, str(func))) == "<class 'builtin_function_or_method'>":
                try:
                    letters_c = len(repr(func))
                    x = 30 - letters_c
                    print('%s %s: %s' % (func, ' ' * x, getattr(self.module, str(func))()))
                except (TypeError, IndexError):
                    continue

    def get_all_attrs(self):
        return self.module.__dict__

    def get_own_attrs(self):
        own_attrs = {}
        for attr in self.get_all_attrs():
            if not re.match(self.pattern, str(attr)):
                own_attrs[attr] = getattr(self.module, '%s' % attr)


        return own_attrs


my = ModuleAnalysis(sys.modules[__name__])
print(my.get_own_attrs())
