import webbrowser


class ModuleAnalysis:

    def __init__(self, _module):
        self.module = _module

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


my = ModuleAnalysis(webbrowser)
my.display_available_functions()
