# -*- coding: utf-8 -*-

finnish_stopwords = set(
    u"""
    aiemmin aika aikaa aikaan aikaisemmin aikaisin aikajen aikana aikoina
    aikoo aikovat aina ainakaan ainakin ainoa ainoat aiomme aion aiotte
    aist aivan ajan alas alemmas alkuisin alkuun alla alle aloitamme
    aloitan aloitat aloitatte aloitattivat aloitettava aloitettevaksi
    aloitettu aloitimme aloitin aloitit aloititte aloittaa aloittamatta
    aloitti aloittivat alta aluksi alussa alusta annettavaksi annetteva
    annettu antaa antamatta antoi aoua apu asia asiaa asian asiasta asiat
    asioiden asioihin asioita asti auki avuksi avulla avun avutta com
    edelle edelleen edellä edeltä edemmäs edes edessä edestä ehkä ei eikä
    eilen eivät eli ellei elleivät ellemme ellen ellet ellette emme en
    enemmän eniten ennen ensi ensimmäinen ensimmäiseksi ensimmäisen
    ensimmäisenä ensimmäiset ensimmäisiksi ensimmäisinä ensimmäisiä
    ensimmäistä ensin entinen entisen entisiä entisten entistä enää eri
    erittäin erityisesti eräiden eräs eräät esi esiin esillä esimerkiksi
    et eteen etenkin ette ettei että fax halua haluaa haluamatta haluamme
    haluan haluat haluatte haluavat halunnut halusi halusimme halusin
    halusit halusitte halusivat halutessa haluton he hei heidän heidät
    heihin heille heillä heiltä heissä heistä heitä helposti heti hetkellä
    hieman hlö hlöä html http huolimatta huomenna hyvien hyviin hyviksi
    hyville hyviltä hyvin hyvinä hyvissä hyvistä hyviä hyvä hyvät hyvää
    hän häneen hänelle hänellä häneltä hänen hänessä hänestä hänet häntä
    ihan ilman ilmeisesti itse itsensä itseään ja jo johon joiden joihin
    joiksi joilla joille joilta joina joissa joista joita joka jokainen
    jokin joko joksi joku jolla jolle jolloin jolta jompikumpi jona jonka
    jonkin jonne joo jopa jos joskus jossa josta jota jotain joten
    jotenkin jotenkuten jotka jotta jouduimme jouduin jouduit jouduitte
    joudumme joudun joudutte joukkoon joukossa joukosta joutua joutui
    joutuivat joutumaan joutuu joutuvat juuri jälkeen jälleen jää
    kahdeksan kahdeksannen kahdella kahdelle kahdelta kahden kahdessa
    kahdesta kahta kahteen kai kaiken kaikille kaikilta kaikkea kaikki
    kaikkia kaikkiaan kaikkialla kaikkialle kaikkialta kaikkien kaikkin
    kaksi kannalta kannattaa kanssa kanssaan kanssamme kanssani kanssanne
    kanssasi kauan kauemmas kaukana kautta kehen keiden keihin keiksi
    keille keillä keiltä keinä keissä keistä keitten keittä keitä keneen
    keneksi kenelle kenellä keneltä kenen kenenä kenessä kenestä kenet
    kenettä kennessästä kenties kerran kerta kertaa keskellä kesken
    keskimäärin ketkä ketä kiitos klo kohti koko kokonaan kolmas kolme
    kolmen kolmesti koska koskaan kovin kuin kuinka kuitenkaan kuitenkin
    kuka kukaan kukin kumpainen kumpainenkaan kumpi kumpikaan kumpikin kun
    kuten kuuden kuusi kuutta kyllä kymmenen kyse liian liki lisäksi lisää
    lla lue luo luona lähekkäin lähelle lähellä läheltä lähemmäs lähes
    lähinnä lähtien läpi mahdollisimman mahdollista me meidän meidät
    meihin meille meillä meiltä meissä meistä meitä melkein melko menee
    meneet menemme menen menet menette menevät meni menimme menin menit
    menivät mennessä mennyt menossa mihin mikin miksi mikä mikäli mikään
    mille milloin milloinkaan millä miltä minkä minne minua minulla
    minulle minulta minun minussa minusta minut minuun minä missä mistä
    miten mitkä mitä mitään moi molemmat mones monesti monet moni
    moniaalla moniaalle moniaalta monta muassa muiden muita muka mukaan
    mukaansa mukana mutta muu muualla muualle muualta muuanne muulloin
    muun muut muuta muutama muutaman muuten myöhemmin myös myöskin
    myöskään myötä ne neljä neljän neljää niiden niihin niiksi niille
    niillä niiltä niin niinä niissä niistä niitä noiden noihin noiksi
    noilla noille noilta noin noina noissa noista noita nopeammin nopeasti
    nopeiten nro nuo nyt näiden näihin näiksi näille näillä näiltä näin
    näinä näissä näissähin näissälle näissältä näissästä näistä näitä nämä
    ohi oikea oikealla oikein ole olemme olen olet olette oleva olevan
    olevat oli olimme olin olisi olisimme olisin olisit olisitte olisivat
    olit olitte olivat olla olleet olli ollut oma omaa omaan omaksi omalle
    omalta oman omassa omat omia omien omiin omiksi omille omilta omissa
    omista on onkin onko ovat paikoittain paitsi pakosti paljon paras
    paremmin parempi parhaillaan parhaiten perusteella peräti pian pieneen
    pieneksi pienelle pienellä pieneltä pienempi pienestä pieni pienin
    poikki puh puolesta puolestaan päälle runsaasti saa saada saakka saat
    sadam sama samaa samaan samalla samallalta samallassa samallasta saman
    samat samoin sata sataa satojen se seitsemän sekä sen seuraavat siellä
    sieltä siihen siinä siis siitä sijaan siksi sille silloin sillä silti
    siltä sinne sinua sinulla sinulle sinulta sinun sinussa sinusta sinut
    sinuun sinä sis sisäkkäin sisällä siten sitten sitä sivu ssa sta
    suoraan suuntaan suuren suuret suuri suuria suurin suurten taa taas
    taemmas tahansa tai takaa takaisin takana takia tapauksessa tavalla
    tavoitteena te teidän teidät teihin teille teillä teiltä teissä teistä
    teitä tietysti tms todella toinen toisaalla toisaalle toisaalta
    toiseen toiseksi toisella toiselle toiselta toisemme toisen toisensa
    toisessa toisesta toista toistaiseksi toki tosin tuhannen tuhat tule
    tulee tulemme tulen tulet tulette tulevat tulimme tulin tulisi
    tulisimme tulisin tulisit tulisitte tulisivat tulit tulitte tulivat
    tulla tulleet tullut tuntuu tuo tuoda tuohon tuoksi tuolla tuolle
    tuolloin tuolta tuon tuona tuonne tuossa tuosta tuota tuskin tykö
    tähän täksi tälle tällä tällöin tältä tämä tämän tänne tänä tänään
    tässä tästä täten tätä täysin täytyvät täytyy täällä täältä usea
    useasti useimmiten usein useita uudeksi uudelleen uuden uudet uusi
    uusia uusien uusinta uuteen uutta vaan vai vaiheessa vaikea vaikean
    vaikeat vaikeilla vaikeille vaikeilta vaikeissa vaikeista vaikka vain
    varmasti varsin varsinkin varten vasemmalla vasen vasta vastaan
    vastakkain vastan verran vielä vierekkäin vieressä vieri viiden viim
    viime viimeinen viimeisen viimeksi viisi voi voida voidaan voimme voin
    voisi voit voitte voivat vuoden vuoksi vuosi vuosien vuosina vuotta
    vähemmän vähintään vähiten vähän välillä www yhdeksän yhden yhdessä
    yhteen yhteensä yhteydessä yhteyteen yhtä yhtäälle yhtäällä yhtäältä
    yhtään yhä yksi yksin yksittäin yleensä ylemmäs yli ylös ympäri yms
    älköön älä""".strip().split())

swedish_stopwords = set(
    u"""
    alla allt att av blev bli blir blivit de dem den denna deras dess
    dessa det detta dig din dina ditt du där då efter ej eller en er era
    ert ett från för ha hade han hans har henne hennes hon honom hur här i
    icke ingen inom inte jag ju kan kunde man med mellan men mig min mina
    mitt mot mycket ni nu när någon något några och om oss på samma sedan
    sig sin sina sitta själv skulle som så sådan sådana sådant till under
    upp ut utan vad var vara varför varit varje vars vart vem vi vid vilka
    vilkas vilken vilket vår våra vårt än är åt över""".strip().split())

english_stopwords = set(
    u"""
    a about above after again against all also am an and another any are
    aren't as at back be because been before being below between both but
    by can't cannot could couldn't did didn't do does doesn't doing don't
    down during each even ever every few first five for four from further
    get go goes had hadn't has hasn't have haven't having he he'd he'll
    he's her here here's hers herself high him himself his how how's
    however i i'd i'll i'm i've if in into is isn't it it's its itself
    just least less let's like long made make many me more most mustn't my
    myself never new no nor not now of off old on once one only or other
    ought our ours ourselves out over own put said same say says second
    see seen shan't she she'd she'll she's should shouldn't since so some
    still such take than that that's the their theirs them themselves then
    there there's these they they'd they'll they're they've this those
    three through to too two under until up very was wasn't way we we'd
    we'll we're we've well were weren't what what's when when's where
    where's whether which while who who's whom why why's with won't would
    wouldn't you you'd you'll you're you've your yours yourself
    yourselves""".strip().split())

russian_stopwords = set(
    u"""
    и в во не что он на я с со как а то все она так его но да ты к у же
    вы за бы по только ее мне было вот от меня еще нет о из ему теперь
    когда даже ну вдруг ли если уже или ни быть был него до вас нибудь
    опять уж вам сказал ведь там потом себя ничего ей может они тут где
    есть надо ней для мы тебя их чем была сам чтоб без будто человек
    чего раз тоже себе под жизнь будет ж тогда кто этот говорил того
    потому этого какой совсем ним здесь этом один почти мой тем чтобы
    нее кажется сейчас были куда зачем сказать всех никогда сегодня
    можно при наконец два об другой хоть после над больше тот через эти
    нас про всего них какая много разве сказала три эту моя впрочем
    хорошо свою этой перед иногда лучше чуть том нельзя такой им более
    всегда конечно всю между""".strip().split())

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
