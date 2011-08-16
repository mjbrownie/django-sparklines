import datetime
from dateutil.relativedelta import relativedelta

now = datetime.datetime.now().date()
default_start = now - relativedelta(years = 1)

# Utility Functions {{{1
def get_object_date_period(queryset, date_field, start = None,end = None,
        step = 1, mode='weeks'):

    d = start or default_start
    end = end or now

    period = []
    delta = relativedelta(**{mode:step})
    date_field = str(date_field)

    while d <= end:
        period.append(
                (d,
                    queryset.filter(**{
                        date_field + '__gte' :d,
                        date_field + '__lte' :d + delta
                        })
                ))

        d += delta

    return period


def get_object_date_count_list(*args,**kwargs):
    return [str( p[1].count() ) for p in get_object_date_period(*args,**kwargs)]
