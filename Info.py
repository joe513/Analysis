import inspect
import Analysis.ObjectAnalysis as ObjectAnalysis


def object_attrs(obj):
    try:
        return obj.__dict__

    except AttributeError:
        return dir(obj)


def info(obj):

    obje = ObjectAnalysis.IsObjectAbleAnalysis(obj)


    print(
          "-"*40,
          "              Common:",
          "Object's name          : %s" % obj,
          "Object's class         : %s" % type(obj),
          "Object's               : ",
          "Object's attributess   : %s" % object_attrs(obj),
          "-"*40,
          "              IS ABLE: ",
          "Is iterabel            : %s" % obje.is_iterable(),
          "Is indexable           : %s" % obje.is_indexable(),
          "Is callable            : %s" % obje.is_callable(),


          sep='\n'


          )


info('Bye')
