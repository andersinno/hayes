# -*- coding: utf-8 -*-


class _Ranges(object):
    def __init__(self):
        self.ranges = {}

    def add_range(self, field, gte=None, gt=None,
                  lte=None, lt=None, boost=1.0):
        out = {}
        if gte:
            out["gte"] = gte
        elif gt:
            out["gt"] = gt

        if lte:
            out["lte"] = lte
        elif lt:
            out["lt"] = lt

        if out:
            if boost is not None:
                out["boost"] = float(boost)
            self.ranges[field] = out
