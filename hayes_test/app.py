# -- encoding: UTF-8 --

from django.conf.urls import patterns, url
import json
from django import forms
from django.http import HttpResponse
from django.views.generic import TemplateView
from hayes.django_interop import get_connection, get_index_by_name
from hayes.search import Search
from hayes.search.filters import PrefixFilter
from hayes.search.queries import QueryStringQuery, BoolQuery, RangeQuery, MatchAllQuery, MatchQuery


class SearchForm(forms.Form):
	q = forms.CharField(label=u"Search", required=False)
	use_match_query = forms.BooleanField(label="Match Query", help_text=u"Better results, but no query strings", required=False, initial=True)
	only_people = forms.BooleanField(label=u"Only search people", required=False)
	person_height_min = forms.IntegerField(label=u"Person height minimum", required=False)
	person_height_max = forms.IntegerField(label=u"Person height maximum", required=False)

class SearchView(TemplateView):
	template_name = "search.html"

	def get_context_data(self, **kwargs):
		context = super(SearchView, self).get_context_data(**kwargs)
		context["form"] = form = SearchForm(data=self.request.GET if self.request.GET else None)
		if form.is_bound and form.is_valid():
			conn = get_connection()
			query_string = (form.cleaned_data["q"] or "").strip()
			if query_string:
				if form.cleaned_data.get("use_match_query"):
					query = MatchQuery("_all", query_string)
				else:
					query = QueryStringQuery("*" + query_string + "*")
			else:
				query = MatchAllQuery()

			if form.cleaned_data["only_people"]:
				min_h = form.cleaned_data.get("person_height_min")
				max_h = form.cleaned_data.get("person_height_max")
				if min_h is not None or max_h is not None:
					rq = RangeQuery()
					rq.add_range("height", gte=min_h, lte=max_h)
					query = BoolQuery(must=[query, rq])

				context["results"] = conn.search(Search(
					query=query,
					filter=PrefixFilter(_type="people"),
				    fields=["name", "street", "height"]
				))

			else:
				context["results"] = conn.search(query)

		return context

	def get(self, request, *args, **kwargs):
		complete = request.GET.get("complete")
		if complete:
			page_index = get_index_by_name("pages")
			result = get_connection().completion_suggest(page_index, complete, fuzzy=2)
			return HttpResponse(content=json.dumps(result.options), content_type="application/json")
		return super(SearchView, self).get(request, *args, **kwargs)


urlpatterns = patterns('',
	url(r'^$', SearchView.as_view(), name='search'),
)

_application = None

def application(environ, start_response):
	global _application
	if not _application:
		from django.core.wsgi import get_wsgi_application
		_application = get_wsgi_application()
	return _application(environ, start_response)
