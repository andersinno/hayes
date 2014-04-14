# -- encoding: UTF-8 --


def object_to_dict(obj, keys=None):
    out = {}

    if hasattr(obj, "as_dict"):
        obj = obj.as_dict()

    if hasattr(obj, "to_dict"):
        obj = obj.to_dict()

    if isinstance(obj, dict):
        if not keys:
            return obj
        src = obj
    else:
        src = vars(obj)

    return dict((k, v) for (k, v) in src.iteritems() if ((not keys or k in keys) and not k.startswith("__") and not callable(v)))
