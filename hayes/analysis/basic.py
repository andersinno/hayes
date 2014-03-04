# -- encoding: UTF-8 --




"analysis": {
	"analyzer": {
		"ngram_analyzer": {
			"type": "custom",
			"tokenizer": "lowercase",
			"filter": ["haystack_ngram", "asciifolding"]
		},
		"edgengram_analyzer": {
			"type": "custom",
			"tokenizer": "lowercase",
			"filter": ["haystack_edgengram", "asciifolding"]
		}
	},
	"filter": {
		"haystack_ngram": {
			"type": "nGram",
			"min_gram": 3,
			"max_gram": 15
		},
		"haystack_edgengram": {
			"type": "edgeNGram",
			"min_gram": 2,
			"max_gram": 15
		}
	}
}
