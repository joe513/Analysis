import re
import inspect


__author__ = 'Jabrail Lezgintsev (joe513)'
__github__ = 'https://github.com/joe513'
__email__ = 'lezgintsev13@yandex.ru'


class ModuleAnalysis:

    def __init__(self, _module):
        self.module = _module
        self.pattern = re.compile('__(.*)__')

    def display_available_functions(self):

        print('Function: ', ' ' * 37,'link:')
        for func in self.module.__dict__:
            if inspect.isfunction(getattr(self.module, func)):
                letters_c = len(repr(func))
                x = 50 - letters_c
                print('%s %s: %s' % (func, ' ' * x, getattr(self.module, str(func))))

    def get_all_classes(self):
        classes = [klass for klass in self.module.__dict__ if inspect.isclass(getattr(self.module, klass))]
        return classes

    def get_all_attrs(self):
        return self.module.__dict__

    def get_own_attrs(self, dict_or_list='dict'):

        own_attrs = {attr: getattr(self.module, attr) for attr in self.get_all_attrs()
                     if not re.match(self.pattern, str(attr))}

        return own_attrs if dict_or_list == 'dict' else list(own_attrs.keys())

    def get_all_attrs_beside_methods(self):
        attrs_beside_methods = [attr for attr in self.module.__dict__
                                if not inspect.ismethod(getattr(self.module, attr))
                                if not inspect.isfunction(getattr(self.module, attr))]
        return attrs_beside_methods



my = ModuleAnalysis(inspect)
print(my.get_all_classes())
