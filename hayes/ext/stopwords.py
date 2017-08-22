# -- encoding: UTF-8 --

finnish_stopwords = set((u"aiemmin", u"aika", u"aikaa", u"aikaan", u"aikaisemmin", u"aikaisin", u"aikajen", u"aikana",
                         u"aikoina", u"aikoo", u"aikovat", u"aina", u"ainakaan", u"ainakin", u"ainoa", u"ainoat",
                         u"aiomme", u"aion", u"aiotte", u"aist", u"aivan", u"ajan", u"alas", u"alemmas", u"alkuisin",
                         u"alkuun", u"alla", u"alle", u"aloitamme", u"aloitan", u"aloitat", u"aloitatte",
                         u"aloitattivat", u"aloitettava", u"aloitettevaksi", u"aloitettu", u"aloitimme", u"aloitin",
                         u"aloitit", u"aloititte", u"aloittaa", u"aloittamatta", u"aloitti", u"aloittivat", u"alta",
                         u"aluksi", u"alussa", u"alusta", u"annettavaksi", u"annetteva", u"annettu", u"antaa",
                         u"antamatta", u"antoi", u"aoua", u"apu", u"asia", u"asiaa", u"asian", u"asiasta", u"asiat",
                         u"asioiden", u"asioihin", u"asioita", u"asti", u"auki", u"avuksi", u"avulla", u"avun",
                         u"avutta", u"com", u"edelle", u"edelleen", u"edellä", u"edeltä", u"edemmäs", u"edes",
                         u"edessä", u"edestä", u"ehkä", u"ei", u"eikä", u"eilen", u"eivät", u"eli", u"ellei",
                         u"elleivät", u"ellemme", u"ellen", u"ellet", u"ellette", u"emme", u"en", u"enemmän", u"eniten",
                         u"ennen", u"ensi", u"ensimmäinen", u"ensimmäiseksi", u"ensimmäisen", u"ensimmäisenä",
                         u"ensimmäiset", u"ensimmäisiksi", u"ensimmäisinä", u"ensimmäisiä", u"ensimmäistä", u"ensin",
                         u"entinen", u"entisen", u"entisiä", u"entisten", u"entistä", u"enää", u"eri", u"erittäin",
                         u"erityisesti", u"eräiden", u"eräs", u"eräät", u"esi", u"esiin", u"esillä", u"esimerkiksi",
                         u"et", u"eteen", u"etenkin", u"ette", u"ettei", u"että", u"fax", u"halua", u"haluaa",
                         u"haluamatta", u"haluamme", u"haluan", u"haluat", u"haluatte", u"haluavat", u"halunnut",
                         u"halusi", u"halusimme", u"halusin", u"halusit", u"halusitte", u"halusivat", u"halutessa",
                         u"haluton", u"he", u"hei", u"heidän", u"heidät", u"heihin", u"heille", u"heillä", u"heiltä",
                         u"heissä", u"heistä", u"heitä", u"helposti", u"heti", u"hetkellä", u"hieman", u"hlö", u"hlöä",
                         u"html", u"http", u"huolimatta", u"huomenna", u"hyvien", u"hyviin", u"hyviksi", u"hyville",
                         u"hyviltä", u"hyvin", u"hyvinä", u"hyvissä", u"hyvistä", u"hyviä", u"hyvä", u"hyvät", u"hyvää",
                         u"hän", u"häneen", u"hänelle", u"hänellä", u"häneltä", u"hänen", u"hänessä", u"hänestä",
                         u"hänet", u"häntä", u"ihan", u"ilman", u"ilmeisesti", u"itse", u"itsensä", u"itseään", u"ja",
                         u"jo", u"johon", u"joiden", u"joihin", u"joiksi", u"joilla", u"joille", u"joilta", u"joina",
                         u"joissa", u"joista", u"joita", u"joka", u"jokainen", u"jokin", u"joko", u"joksi", u"joku",
                         u"jolla", u"jolle", u"jolloin", u"jolta", u"jompikumpi", u"jona", u"jonka", u"jonkin",
                         u"jonne", u"joo", u"jopa", u"jos", u"joskus", u"jossa", u"josta", u"jota", u"jotain", u"joten",
                         u"jotenkin", u"jotenkuten", u"jotka", u"jotta", u"jouduimme", u"jouduin", u"jouduit",
                         u"jouduitte", u"joudumme", u"joudun", u"joudutte", u"joukkoon", u"joukossa", u"joukosta",
                         u"joutua", u"joutui", u"joutuivat", u"joutumaan", u"joutuu", u"joutuvat", u"juuri", u"jälkeen",
                         u"jälleen", u"jää", u"kahdeksan", u"kahdeksannen", u"kahdella", u"kahdelle", u"kahdelta",
                         u"kahden", u"kahdessa", u"kahdesta", u"kahta", u"kahteen", u"kai", u"kaiken", u"kaikille",
                         u"kaikilta", u"kaikkea", u"kaikki", u"kaikkia", u"kaikkiaan", u"kaikkialla", u"kaikkialle",
                         u"kaikkialta", u"kaikkien", u"kaikkin", u"kaksi", u"kannalta", u"kannattaa", u"kanssa",
                         u"kanssaan", u"kanssamme", u"kanssani", u"kanssanne", u"kanssasi", u"kauan", u"kauemmas",
                         u"kaukana", u"kautta", u"kehen", u"keiden", u"keihin", u"keiksi", u"keille", u"keillä",
                         u"keiltä", u"keinä", u"keissä", u"keistä", u"keitten", u"keittä", u"keitä", u"keneen",
                         u"keneksi", u"kenelle", u"kenellä", u"keneltä", u"kenen", u"kenenä", u"kenessä", u"kenestä",
                         u"kenet", u"kenettä", u"kennessästä", u"kenties", u"kerran", u"kerta", u"kertaa", u"keskellä",
                         u"kesken", u"keskimäärin", u"ketkä", u"ketä", u"kiitos", u"klo", u"kohti", u"koko",
                         u"kokonaan", u"kolmas", u"kolme", u"kolmen", u"kolmesti", u"koska", u"koskaan", u"kovin",
                         u"kuin", u"kuinka", u"kuitenkaan", u"kuitenkin", u"kuka", u"kukaan", u"kukin", u"kumpainen",
                         u"kumpainenkaan", u"kumpi", u"kumpikaan", u"kumpikin", u"kun", u"kuten", u"kuuden", u"kuusi",
                         u"kuutta", u"kyllä", u"kymmenen", u"kyse", u"liian", u"liki", u"lisäksi", u"lisää", u"lla",
                         u"lue", u"luo", u"luona", u"lähekkäin", u"lähelle", u"lähellä", u"läheltä", u"lähemmäs",
                         u"lähes", u"lähinnä", u"lähtien", u"läpi", u"mahdollisimman", u"mahdollista", u"me", u"meidän",
                         u"meidät", u"meihin", u"meille", u"meillä", u"meiltä", u"meissä", u"meistä", u"meitä",
                         u"melkein", u"melko", u"menee", u"meneet", u"menemme", u"menen", u"menet", u"menette",
                         u"menevät", u"meni", u"menimme", u"menin", u"menit", u"menivät", u"mennessä", u"mennyt",
                         u"menossa", u"mihin", u"mikin", u"miksi", u"mikä", u"mikäli", u"mikään", u"mille", u"milloin",
                         u"milloinkaan", u"millä", u"miltä", u"minkä", u"minne", u"minua", u"minulla",
                         u"minulle", u"minulta", u"minun", u"minussa", u"minusta", u"minut", u"minuun", u"minä",
                         u"missä", u"mistä", u"miten", u"mitkä", u"mitä", u"mitään", u"moi", u"molemmat", u"mones",
                         u"monesti", u"monet", u"moni", u"moniaalla", u"moniaalle", u"moniaalta", u"monta", u"muassa",
                         u"muiden", u"muita", u"muka", u"mukaan", u"mukaansa", u"mukana", u"mutta", u"muu", u"muualla",
                         u"muualle", u"muualta", u"muuanne", u"muulloin", u"muun", u"muut", u"muuta", u"muutama",
                         u"muutaman", u"muuten", u"myöhemmin", u"myös", u"myöskin", u"myöskään", u"myötä", u"ne",
                         u"neljä", u"neljän", u"neljää", u"niiden", u"niihin", u"niiksi", u"niille", u"niillä",
                         u"niiltä", u"niin", u"niinä", u"niissä", u"niistä", u"niitä", u"noiden", u"noihin", u"noiksi",
                         u"noilla", u"noille", u"noilta", u"noin", u"noina", u"noissa", u"noista", u"noita",
                         u"nopeammin", u"nopeasti", u"nopeiten", u"nro", u"nuo", u"nyt", u"näiden", u"näihin",
                         u"näiksi", u"näille", u"näillä", u"näiltä", u"näin", u"näinä", u"näissä", u"näissähin",
                         u"näissälle", u"näissältä", u"näissästä", u"näistä", u"näitä", u"nämä", u"ohi", u"oikea",
                         u"oikealla", u"oikein", u"ole", u"olemme", u"olen", u"olet", u"olette", u"oleva", u"olevan",
                         u"olevat", u"oli", u"olimme", u"olin", u"olisi", u"olisimme", u"olisin", u"olisit",
                         u"olisitte", u"olisivat", u"olit", u"olitte", u"olivat", u"olla", u"olleet", u"olli", u"ollut",
                         u"oma", u"omaa", u"omaan", u"omaksi", u"omalle", u"omalta", u"oman", u"omassa", u"omat",
                         u"omia", u"omien", u"omiin", u"omiksi", u"omille", u"omilta", u"omissa", u"omista", u"on",
                         u"onkin", u"onko", u"ovat", u"paikoittain", u"paitsi", u"pakosti", u"paljon", u"paras",
                         u"paremmin", u"parempi", u"parhaillaan", u"parhaiten", u"perusteella", u"peräti", u"pian",
                         u"pieneen", u"pieneksi", u"pienelle", u"pienellä", u"pieneltä", u"pienempi", u"pienestä",
                         u"pieni", u"pienin", u"poikki", u"puh", u"puolesta", u"puolestaan", u"päälle", u"runsaasti",
                         u"saa", u"saada", u"saakka", u"saat", u"sadam", u"sama", u"samaa", u"samaan", u"samalla",
                         u"samallalta", u"samallassa", u"samallasta", u"saman", u"samat", u"samoin", u"sata", u"sataa",
                         u"satojen", u"se", u"seitsemän", u"sekä", u"sen", u"seuraavat", u"siellä", u"sieltä",
                         u"siihen", u"siinä", u"siis", u"siitä", u"sijaan", u"siksi", u"sille", u"silloin", u"sillä",
                         u"silti", u"siltä", u"sinne", u"sinua", u"sinulla", u"sinulle", u"sinulta", u"sinun",
                         u"sinussa", u"sinusta", u"sinut", u"sinuun", u"sinä", u"sis", u"sisäkkäin", u"sisällä",
                         u"siten", u"sitten", u"sitä", u"sivu", u"ssa", u"sta", u"suoraan", u"suuntaan", u"suuren",
                         u"suuret", u"suuri", u"suuria", u"suurin", u"suurten", u"taa", u"taas", u"taemmas", u"tahansa",
                         u"tai", u"takaa", u"takaisin", u"takana", u"takia", u"tapauksessa", u"tavalla", u"tavoitteena",
                         u"te", u"teidän", u"teidät", u"teihin", u"teille", u"teillä", u"teiltä", u"teissä", u"teistä",
                         u"teitä", u"tietysti", u"tms", u"todella", u"toinen", u"toisaalla", u"toisaalle", u"toisaalta",
                         u"toiseen", u"toiseksi", u"toisella", u"toiselle", u"toiselta", u"toisemme", u"toisen",
                         u"toisensa", u"toisessa", u"toisesta", u"toista", u"toistaiseksi", u"toki", u"tosin",
                         u"tuhannen", u"tuhat", u"tule", u"tulee", u"tulemme", u"tulen", u"tulet", u"tulette",
                         u"tulevat", u"tulimme", u"tulin", u"tulisi", u"tulisimme", u"tulisin", u"tulisit",
                         u"tulisitte", u"tulisivat", u"tulit", u"tulitte", u"tulivat", u"tulla", u"tulleet", u"tullut",
                         u"tuntuu", u"tuo", u"tuoda", u"tuohon", u"tuoksi", u"tuolla", u"tuolle", u"tuolloin",
                         u"tuolta", u"tuon", u"tuona", u"tuonne", u"tuossa", u"tuosta", u"tuota", u"tuskin", u"tykö",
                         u"tähän", u"täksi", u"tälle", u"tällä", u"tällöin", u"tältä", u"tämä", u"tämän", u"tänne",
                         u"tänä", u"tänään", u"tässä", u"tästä", u"täten", u"tätä", u"täysin", u"täytyvät", u"täytyy",
                         u"täällä", u"täältä", u"usea", u"useasti", u"useimmiten", u"usein", u"useita", u"uudeksi",
                         u"uudelleen", u"uuden", u"uudet", u"uusi", u"uusia", u"uusien", u"uusinta", u"uuteen",
                         u"uutta", u"vaan", u"vai", u"vaiheessa", u"vaikea", u"vaikean", u"vaikeat", u"vaikeilla",
                         u"vaikeille", u"vaikeilta", u"vaikeissa", u"vaikeista", u"vaikka", u"vain", u"varmasti",
                         u"varsin", u"varsinkin", u"varten", u"vasemmalla", u"vasen", u"vasta", u"vastaan",
                         u"vastakkain", u"vastan", u"verran", u"vielä", u"vierekkäin", u"vieressä", u"vieri", u"viiden",
                         u"viim", u"viime", u"viimeinen", u"viimeisen", u"viimeksi", u"viisi", u"voi", u"voida",
                         u"voidaan", u"voimme", u"voin", u"voisi", u"voit", u"voitte", u"voivat", u"vuoden", u"vuoksi",
                         u"vuosi", u"vuosien", u"vuosina", u"vuotta", u"vähemmän", u"vähintään", u"vähiten", u"vähän",
                         u"välillä", u"www", u"yhdeksän", u"yhden", u"yhdessä", u"yhteen", u"yhteensä", u"yhteydessä",
                         u"yhteyteen", u"yhtä", u"yhtäälle", u"yhtäällä", u"yhtäältä", u"yhtään", u"yhä", u"yksi",
                         u"yksin", u"yksittäin", u"yleensä", u"ylemmäs", u"yli", u"ylös", u"ympäri", u"yms", u"älköön",
                         u"älä",))
swedish_stopwords = set((u"alla", u"allt", u"att", u"av", u"blev", u"bli", u"blir", u"blivit", u"de", u"dem", u"den",
                         u"denna", u"deras", u"dess", u"dessa", u"det", u"detta", u"dig", u"din", u"dina", u"ditt",
                         u"du", u"där", u"då", u"efter", u"ej", u"eller", u"en", u"er", u"era", u"ert", u"ett", u"från",
                         u"för", u"ha", u"hade", u"han", u"hans", u"har", u"henne", u"hennes", u"hon", u"honom", u"hur",
                         u"här", u"i", u"icke", u"ingen", u"inom", u"inte", u"jag", u"ju", u"kan", u"kunde", u"man",
                         u"med", u"mellan", u"men", u"mig", u"min", u"mina", u"mitt", u"mot", u"mycket", u"ni", u"nu",
                         u"när", u"någon", u"något", u"några", u"och", u"om", u"oss", u"på", u"samma", u"sedan", u"sig",
                         u"sin", u"sina", u"sitta", u"själv", u"skulle", u"som", u"så", u"sådan", u"sådana", u"sådant",
                         u"till", u"under", u"upp", u"ut", u"utan", u"vad", u"var", u"vara", u"varför", u"varit",
                         u"varje", u"vars", u"vart", u"vem", u"vi", u"vid", u"vilka", u"vilkas", u"vilken", u"vilket",
                         u"vår", u"våra", u"vårt", u"än", u"är", u"åt", u"över"))
english_stopwords = set((
                        u"a", u"about", u"above", u"after", u"again", u"against", u"all", u"also", u"am", u"an", u"and",
                        u"another", u"any", u"are", u"aren't", u"as", u"at", u"back", u"be", u"because", u"been",
                        u"before", u"being", u"below", u"between", u"both", u"but", u"by", u"can't", u"cannot",
                        u"could", u"couldn't", u"did", u"didn't", u"do", u"does", u"doesn't", u"doing", u"don't",
                        u"down", u"during", u"each", u"even", u"ever", u"every", u"few", u"first", u"five", u"for",
                        u"four", u"from", u"further", u"get", u"go", u"goes", u"had", u"hadn't", u"has", u"hasn't",
                        u"have", u"haven't", u"having", u"he", u"he'd", u"he'll", u"he's", u"her", u"here", u"here's",
                        u"hers", u"herself", u"high", u"him", u"himself", u"his", u"how", u"how's", u"however", u"i",
                        u"i'd", u"i'll", u"i'm", u"i've", u"if", u"in", u"into", u"is", u"isn't", u"it", u"it's",
                        u"its", u"itself", u"just", u"least", u"less", u"let's", u"like", u"long", u"made", u"make",
                        u"many", u"me", u"more", u"most", u"mustn't", u"my", u"myself", u"never", u"new", u"no", u"nor",
                        u"not", u"now", u"of", u"off", u"old", u"on", u"once", u"one", u"only", u"or", u"other",
                        u"ought", u"our", u"ours", u"ourselves", u"out", u"over", u"own", u"put", u"said", u"same",
                        u"say", u"says", u"second", u"see", u"seen", u"shan't", u"she", u"she'd", u"she'll", u"she's",
                        u"should", u"shouldn't", u"since", u"so", u"some", u"still", u"such", u"take", u"than", u"that",
                        u"that's", u"the", u"their", u"theirs", u"them", u"themselves", u"then", u"there", u"there's",
                        u"these", u"they", u"they'd", u"they'll", u"they're", u"they've", u"this", u"those", u"three",
                        u"through", u"to", u"too", u"two", u"under", u"until", u"up", u"very", u"was", u"wasn't",
                        u"way", u"we", u"we'd", u"we'll", u"we're", u"we've", u"well", u"were", u"weren't", u"what",
                        u"what's", u"when", u"when's", u"where", u"where's", u"whether", u"which", u"while", u"who",
                        u"who's", u"whom", u"why", u"why's", u"with", u"won't", u"would", u"wouldn't", u"you", u"you'd",
                        u"you'll", u"you're", u"you've", u"your", u"yours", u"yourself", u"yourselves"))
russian_stopwords = set((u"и", u"в", u"во", u"не", u"что", u"он", u"на", u"я", u"с", u"со", u"как", u"а", u"то", u"все",
                         u"она", u"так", u"его", u"но", u"да", u"ты", u"к", u"у", u"же", u"вы", u"за", u"бы", u"по",
                         u"только", u"ее", u"мне", u"было", u"вот", u"от", u"меня", u"еще", u"нет", u"о", u"из", u"ему",
                         u"теперь", u"когда", u"даже", u"ну", u"вдруг", u"ли", u"если", u"уже", u"или", u"ни", u"быть",
                         u"был", u"него", u"до", u"вас", u"нибудь", u"опять", u"уж", u"вам", u"сказал", u"ведь", u"там",
                         u"потом", u"себя", u"ничего", u"ей", u"может", u"они", u"тут", u"где", u"есть", u"надо",
                         u"ней", u"для", u"мы", u"тебя", u"их", u"чем", u"была", u"сам", u"чтоб", u"без", u"будто",
                         u"человек", u"чего", u"раз", u"тоже", u"себе", u"под", u"жизнь", u"будет", u"ж", u"тогда",
                         u"кто", u"этот", u"говорил", u"того", u"потому", u"этого", u"какой", u"совсем", u"ним",
                         u"здесь", u"этом", u"один", u"почти", u"мой", u"тем", u"чтобы", u"нее", u"кажется", u"сейчас",
                         u"были", u"куда", u"зачем", u"сказать", u"всех", u"никогда", u"сегодня", u"можно", u"при",
                         u"наконец", u"два", u"об", u"другой", u"хоть", u"после", u"над", u"больше", u"тот", u"через",
                         u"эти", u"нас", u"про", u"всего", u"них", u"какая", u"много", u"разве", u"сказала", u"три",
                         u"эту", u"моя", u"впрочем", u"хорошо", u"свою", u"этой", u"перед", u"иногда", u"лучше",
                         u"чуть", u"том", u"нельзя", u"такой", u"им", u"более", u"всегда", u"конечно", u"всю",
                         u"между"))

unicode_punctuation_chars = (
    u"\u0021\u0022\u0023\u0025\u0026\u0027\u0028\u0029\u002a\u002c\u002d"
    u"\u002e\u002f\u003a\u003b\u003f\u0040\u005b\u005c\u005d\u005f\u007b"
    u"\u007d\u00a1\u00ab\u00b7\u00bb\u00bf\u037e\u0387\u055a\u055b\u055c"
    u"\u055d\u055e\u055f\u0589\u058a\u05be\u05c0\u05c3\u05c6\u05f3\u05f4"
    u"\u0609\u060a\u060c\u060d\u061b\u061e\u061f\u066a\u066b\u066c\u066d"
    u"\u06d4\u0700\u0701\u0702\u0703\u0704\u0705\u0706\u0707\u0708\u0709"
    u"\u070a\u070b\u070c\u070d\u07f7\u07f8\u07f9\u0830\u0831\u0832\u0833"
    u"\u0834\u0835\u0836\u0837\u0838\u0839\u083a\u083b\u083c\u083d\u083e"
    u"\u0964\u0965\u0970\u0df4\u0e4f\u0e5a\u0e5b\u0f04\u0f05\u0f06\u0f07"
    u"\u0f08\u0f09\u0f0a\u0f0b\u0f0c\u0f0d\u0f0e\u0f0f\u0f10\u0f11\u0f12"
    u"\u0f3a\u0f3b\u0f3c\u0f3d\u0f85\u0fd0\u0fd1\u0fd2\u0fd3\u0fd4\u104a"
    u"\u104b\u104c\u104d\u104e\u104f\u10fb\u1361\u1362\u1363\u1364\u1365"
    u"\u1366\u1367\u1368\u1400\u166d\u166e\u169b\u169c\u16eb\u16ec\u16ed"
    u"\u1735\u1736\u17d4\u17d5\u17d6\u17d8\u17d9\u17da\u1800\u1801\u1802"
    u"\u1803\u1804\u1805\u1806\u1807\u1808\u1809\u180a\u1944\u1945\u19de"
    u"\u19df\u1a1e\u1a1f\u1aa0\u1aa1\u1aa2\u1aa3\u1aa4\u1aa5\u1aa6\u1aa8"
    u"\u1aa9\u1aaa\u1aab\u1aac\u1aad\u1b5a\u1b5b\u1b5c\u1b5d\u1b5e\u1b5f"
    u"\u1b60\u1c3b\u1c3c\u1c3d\u1c3e\u1c3f\u1c7e\u1c7f\u1cd3\u2010\u2011"
    u"\u2012\u2013\u2014\u2015\u2016\u2017\u2018\u2019\u201a\u201b\u201c"
    u"\u201d\u201e\u201f\u2020\u2021\u2022\u2023\u2024\u2025\u2026\u2027"
    u"\u2030\u2031\u2032\u2033\u2034\u2035\u2036\u2037\u2038\u2039\u203a"
    u"\u203b\u203c\u203d\u203e\u203f\u2040\u2041\u2042\u2043\u2045\u2046"
    u"\u2047\u2048\u2049\u204a\u204b\u204c\u204d\u204e\u204f\u2050\u2051"
    u"\u2053\u2054\u2055\u2056\u2057\u2058\u2059\u205a\u205b\u205c\u205d"
    u"\u205e\u207d\u207e\u208d\u208e\u2329\u232a\u2768\u2769\u276a\u276b"
    u"\u276c\u276d\u276e\u276f\u2770\u2771\u2772\u2773\u2774\u2775\u27c5"
    u"\u27c6\u27e6\u27e7\u27e8\u27e9\u27ea\u27eb\u27ec\u27ed\u27ee\u27ef"
    u"\u2983\u2984\u2985\u2986\u2987\u2988\u2989\u298a\u298b\u298c\u298d"
    u"\u298e\u298f\u2990\u2991\u2992\u2993\u2994\u2995\u2996\u2997\u2998"
    u"\u29d8\u29d9\u29da\u29db\u29fc\u29fd\u2cf9\u2cfa\u2cfb\u2cfc\u2cfe"
    u"\u2cff\u2e00\u2e01\u2e02\u2e03\u2e04\u2e05\u2e06\u2e07\u2e08\u2e09"
    u"\u2e0a\u2e0b\u2e0c\u2e0d\u2e0e\u2e0f\u2e10\u2e11\u2e12\u2e13\u2e14"
    u"\u2e15\u2e16\u2e17\u2e18\u2e19\u2e1a\u2e1b\u2e1c\u2e1d\u2e1e\u2e1f"
    u"\u2e20\u2e21\u2e22\u2e23\u2e24\u2e25\u2e26\u2e27\u2e28\u2e29\u2e2a"
    u"\u2e2b\u2e2c\u2e2d\u2e2e\u2e30\u2e31\u3001\u3002\u3003\u3008\u3009"
    u"\u300a\u300b\u300c\u300d\u300e\u300f\u3010\u3011\u3014\u3015\u3016"
    u"\u3017\u3018\u3019\u301a\u301b\u301c\u301d\u301e\u301f\u3030\u303d"
    u"\u30a0\u30fb\ua4fe\ua4ff\ua60d\ua60e\ua60f\ua673\ua67e\ua6f2\ua6f3"
    u"\ua6f4\ua6f5\ua6f6\ua6f7\ua874\ua875\ua876\ua877\ua8ce\ua8cf\ua8f8"
    u"\ua8f9\ua8fa\ua92e\ua92f\ua95f\ua9c1\ua9c2\ua9c3\ua9c4\ua9c5\ua9c6"
    u"\ua9c7\ua9c8\ua9c9\ua9ca\ua9cb\ua9cc\ua9cd\ua9de\ua9df\uaa5c\uaa5d"
    u"\uaa5e\uaa5f\uaade\uaadf\uabeb\ufd3e\ufd3f")
