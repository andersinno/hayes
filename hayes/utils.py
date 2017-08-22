# -*- coding: utf-8 -*-


def object_to_dict(obj, keys=None):
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

    def allowed_key_and_value(k, v):
        k_in_keys = (not keys or k in keys)
        k_not_internal = (not k.startswith("__"))
        v_not_callable = (not callable(v))
        return k_in_keys and k_not_internal and v_not_callable

    return dict(
        (k, v)
        for (k, v) in src.items()
        if allowed_key_and_value(k, v)
    )


def batch_iterable(iterable, count):
    """
    Yield batches of `count` items from the given iterable.

    >>> for x in batch([1, 2, 3, 4, 5, 6, 7], 3):
    >>>   print(x)
    [1, 2, 3]
    [4, 5, 6]
    [7]

    :param iterable: An iterable
    :type iterable: Iterable
    :param count: Number of items per batch. If <= 0, nothing is yielded.
    :type count: int
    :return: Iterable of lists of items
    :rtype: Iterable[list[object]]
    """
    if count <= 0:
        return
    current_batch = []
    for item in iterable:
        if len(current_batch) == count:
            yield current_batch
            current_batch = []
        current_batch.append(item)
    if current_batch:
        yield current_batch
