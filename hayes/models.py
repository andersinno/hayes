# -*- coding: utf-8 -*-

from __future__ import with_statement

from six import text_type

from pyes.es import ResultSet
from pyes.models import ElasticSearchModel


class DjangoElasticSearchModel(ElasticSearchModel):
    django_model = None

    def get_object(self, using=None):
        return self.django_model.objects.using(using).get(pk=self.django_id)

    def _get_pk(self):
        return self.django_id

    pk = property(_get_pk)


class DjangoResultSet(ResultSet):
    def get_objects(self, queryset=None):
        """
        Return an iterator of Django model objects in Elasticsearch order,
        optionally using the given Django queryset.  If no queryset is
        given, a default queryset (Model.objects.all) is used.

        :param queryset: Optional queryset to filter in.
        :return:
        """
        if not self:
            return
        if not queryset:
            queryset = self[0].django_model.objects.all()

        pks = [res.pk for res in self if res.django_model == queryset.model]
        object_map = dict((text_type(obj.pk), obj)
                          for obj in queryset.filter(pk__in=pks))
        result_map = dict((res.pk, res)
                          for res in self if res.pk in object_map)

        for pk in pks:
            obj = object_map.get(pk)
            if obj:
                obj._es = result_map.get(pk)
                try:
                    obj._score = obj._es._meta.score
                except AttributeError:
                    obj._score = None
                yield obj
