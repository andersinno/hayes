# -*- coding: utf-8 -*-

try:
    import importlib
except ImportError:
    from django.utils import importlib


def load(specification, context_explanation="Load"):
    module_name, object_name = specification.split(":", 1)
    try:
        module = importlib.import_module(module_name)
    except ImportError as ie:
        raise ValueError(
            u"%s: Could not import module %r to load %r from. (%r)" %
            (context_explanation, module_name, object_name, ie)
        )
    obj = getattr(module, object_name, None)
    if obj is None:
        raise ValueError(
            u"%s: Module %r does not have a name %r, or its value is None." %
            (context_explanation, module, object_name)
        )
    return obj
