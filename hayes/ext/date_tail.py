# -*- coding: utf-8 -*-
import datetime

from hayes.search.queries import RangeQuery


def generate_date_tail_boost_queries(
        field, timedeltas_and_boosts, relative_to=None):
    """
    Generate a list of RangeQueries usable to boost the scores of more
    recent documents.

    Example:

    ```
    queries = generate_date_tail_boost_queries("publish_date", {
            timedelta(days=90): 1,
            timedelta(days=30): 2,
            timedelta(days=10): 4,
    })
    s = Search(BoolQuery(must=..., should=queries))
    # ...
    ```

    Refs:
    http://elasticsearch-users.115913.n3.nabble.com/Boost-recent-documents-td2126107.html#a2126317

    :param field: field name to generate the queries against
    :param timedeltas_and_boosts:
      dictionary of timedelta instances and their boosts. Negative or
      zero boost values will not generate rangequeries.
    :type timedeltas_and_boosts: dict[timedelta, float]
    :param relative_to: Relative to this datetime (may be None for "now")
    :return: List of RangeQueries
    """
    relative_to = relative_to or datetime.datetime.now()
    times = {}
    for timedelta, boost in timedeltas_and_boosts.items():
        date = (relative_to - timedelta).date()
        times[date] = boost
    times = sorted(times.items(), key=lambda i: i[0])
    queries = []

    for (x, time) in enumerate(times):
        kwargs = {"field": field, "boost": time[1]}
        if x == 0:
            kwargs["lte"] = time[0]
        else:
            kwargs["gt"] = time[0]
            if x < len(times) - 1:
                kwargs["lte"] = times[x + 1][0]

        if kwargs["boost"] > 0:
            q = RangeQuery()
            q.add_range(**kwargs)
            queries.append(q)

    return queries
