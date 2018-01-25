import re

__author__ = "Jabrail Lezgintsev ( joe513 )"
__github__ = 'https://github.com/joe513'
__email__ = 'lezgintsev13@yandex.ru'


class ObjectAnalysis:

    pattern = re.compile('__(.*)__')

    def __init__(self, obj):
        self.obj = obj  # Processed object
        self.class_of_object = self.obj.__class__  # This is the class of the object

    # Checking: is object callable
    is_callable = lambda _object, attr: callable(getattr(_object, attr))

    # Returns all object methods
    def get_all_object_methods(self):
        return [attr for attr in dir(self.obj) if ObjectAnalysis.is_callable(self.obj, attr)
                   if not re.match(self.pattern, str(attr))]

    #  Returns all object attrs
    def get_all_object_attrs(self):
        return dir(self.obj)

    # display docs about the class
    def display_docs_of_class(self):
        help(self.obj.__class__)

    def get_all_own_object_attrs(self):
        return [attr for attr in dir(self.obj) if not re.match(self.pattern, attr)]

    def get_all_own_methods(self):
        return [attr for attr in self.get_all_own_object_attrs() if callable(getattr(self.obj, attr))]

    def get_all_attrs_except_methods(self):
        return [attr for attr in
                ObjectAnalysis.get_all_object_attrs(self) if not ObjectAnalysis.is_callable(self.obj, attr)]


# Checks is object able to be ...
class IsObjectAbleAnalysis:
    def __init__(self, obj):
        self.obj = obj

    def is_iterable(self):
        return hasattr(self.obj, '__iter__')

    def is_indexable(self):
        return hasattr(self.obj, '__getitem__')

    def is_callable(self):
        return callable(self.obj)


# Wrapper
class UniversalAnalysis:
    def __init__(self, obj):
        self.Able = IsObjectAbleAnalysis(obj)
        self.object_analysis = ObjectAnalysis(obj)

    def __getattribute__(self, item):
        for klass in (object.__getattribute__(self, 'Able'), object.__getattribute__(self, 'object_analysis')):
            if hasattr(klass, item):
                return getattr(klass, item)


# In my opinion this is the most important object info ( this will be completed )
def the_most_important_info_of_object(obj, width=150):
    testing_obj = UniversalAnalysis(obj)
    print('_-' * width, '\n')
    print('The object to be analyzed       : %s' % testing_obj.obj,
          'The class of the object         : %s' % testing_obj.class_of_object,
          'Is indexable                    : %s' % testing_obj.is_indexable(),
          'Is iterable                     : %s' % testing_obj.is_iterable(),
          'Is callable                     : %s' % testing_obj.is_callable(),
          'Own attributes (Not class attrs): %s' % testing_obj.get_all_own_object_attrs(),
          'Own methods (Not class methods) : %s' % testing_obj.get_all_own_methods(),
          'All attributes                  : %s' % testing_obj.get_all_object_attrs(),
          'All methods                     : %s' % testing_obj.get_all_object_methods(),
          'All attributes besides methods  : %s' % testing_obj.get_all_attrs_except_methods(),
          sep='\n',

          )
    print('\n', '_-' * width)


def is_able_info(obj, width=150):
    testing_obj = UniversalAnalysis(obj)
    print('_-' * width, '\n')
    print('Is object indexable              : %s' % testing_obj.is_indexable(),
          'Is object callable               : %s' % testing_obj.is_callable(),
          'Is object iterable               : %s' % testing_obj.is_iterable(),
          )

if __name__ == '__main__':
    the_most_important_info_of_object('Bye')
