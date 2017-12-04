import re

__author__ = "Jabrail Lezgintsev ( joe513 )"
__github__ = 'https://github.com/joe513'
__email__ = 'lezgintsev13@yandex.ru'


class ObjectAnalysis:

    def __init__(self, obj):
        self.obj = obj  # Processed object
        self.pattern = re.compile('__(.*)__')
        self.class_of_object = self.obj.__class__  # This is the class of the object

    # Checking: is object callable
    is_callable = lambda _object, attr: callable(getattr(_object, '%s' % attr))

    # Returns all object methods
    def get_all_object_methods(self):

        methods = [attr for attr in dir(self.obj) if ObjectAnalysis.is_callable(self.obj, attr) \
                   if not re.match(self.pattern, str(attr))]

        return methods

    #  Returns all object attrs
    def get_all_object_attrs(self):
        return dir(self.obj)

    #display docs about the class
    def display_docs_of_class(self):
        help(self.obj.__class__)

    def get_all_own_object_attrs(self):

        own_attrs = [attr for attr in dir(self.obj) if not re.match(self.pattern, attr)]

        return own_attrs

    def get_all_own_methods(self):
        own_attrs = self.get_all_own_object_attrs()

        own_object_methods = [attr for attr in own_attrs if callable(getattr(self.obj, attr))]

        return own_object_methods

    def get_all_attrs_except_methods(self):
        all_attrs = ObjectAnalysis.get_all_object_attrs(self)

        except_methods = [attr for attr in all_attrs if not ObjectAnalysis.is_callable(self.obj, attr)]

        return except_methods


# Checks is object able to be ...
class IsObjectAbleAnalysis:

    def __init__(self, obj):
        self.obj = obj

    def is_iterable(self):
        return hasattr(self.obj, '__iter__')

    def is_indexable(self):
        return hasattr(self.obj, '__getitem__')
        
    def is_callable(self):
        return hasattr(self.obj, '__call__')


# Wrapper
class UniversalAnalysis:

    def __init__(self, obj):
        self.Able = IsObjectAbleAnalysis(obj)
        self.object_analysis = ObjectAnalysis(obj)

    def __getattribute__(self, item):
        for klass in (object.__getattribute__(self, 'Able'), object.__getattribute__(self, 'object_analysis')):
            if hasattr(klass, '%s' % item):
                return getattr(klass, item)


# In my opinion this is the most important object info ( this will be completed )
def the_most_important_info_of_object(obj):

    width = 150

    testing_obj = UniversalAnalysis(obj)
    print('_-'*width, '\n')
    print('The object to be analyzed       : %s' % obj,
          '\nThe class of the object         : %s' % testing_obj.class_of_object,
          '\nIs indexable                    : %s' % testing_obj.is_indexable(),
          '\nIs iterable                     : %s' % testing_obj.is_iterable(),
          '\nIs callable                     : %s' % testing_obj.is_callable(),
          '\nOwn attributes (Not class attrs): %s' % testing_obj.get_all_own_object_attrs(),
          '\nOwn methods (Not class methods) : %s' % testing_obj.get_all_own_methods(),
          '\nAll attributes                  : %s' % testing_obj.get_all_object_attrs(),
          '\nAll methods                     : %s' % testing_obj.get_all_object_methods(),
          '\nAll attributes besides methods  : %s' % testing_obj.get_all_attrs_except_methods(),

          )
    print('\n', '_-'*width)


if __name__ == '__main__':
    the_most_important_info_of_object('Testing')
