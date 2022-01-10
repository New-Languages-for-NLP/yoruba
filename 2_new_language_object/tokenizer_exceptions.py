from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS
from spacy.symbols import ORTH, NORM, LEMMA
from spacy.util import update_exc

exclusions =[        
{'tani':[{ORTH: 'ta'},{ORTH: 'ni'}]},
{'kíni':[{ORTH: 'kí'},{ORTH: 'ni'}]},
{'kínni':[{ORTH: 'kín'},{ORTH: 'ni'}]},
{'èwoni':[{ORTH: 'èwo'},{ORTH: 'ni'}]},
{"jẹ́kí":[{ORTH: "jẹ́"},{ORTH: 'kí'}]},
{"wípé":[{ORTH: "wí"},{ORTH: 'pé'}]}
{'gégẹ́ḅí':[{ORTH: 'gégẹ́'},{ORTH: 'ḅí'}]},
{'ẹnití':[{ORTH: 'ẹni'},{ORTH: 'tí'}]},
{'ibití':[{ORTH: 'ibi'},{ORTH: 'tí'}]},
{'nítorínáà':[{ORTH: 'nítorí'},{ORTH: 'náà'}]},
{"nítorítí":[{ORTH: "nítorí"},{ORTH: 'tí'}]},
{"nígbàtí":[{ORTH: "nígbà"},{ORTH: 'tí'}]}
{'nígbànáà':[{ORTH: 'nígbà'},{ORTH: 'náà'}]},
{"nígbàgbogbo":[{ORTH: "nígbà"},{ORTH: 'gbogbo'}]},
{"léhìnnáà":[{ORTH: "léhìn"},{ORTH: 'náà'}]}
{"ẹnipé":[{ORTH: "ẹni"},{ORTH: 'pé'}]}
{'nígbànáà':[{ORTH: 'nígbà'},{ORTH: 'náà'}]},
{"nígbàgbogbo":[{ORTH: "nígbà"},{ORTH: 'gbogbo'}]},
{"léhìnnáà":[{ORTH: "léhìn"},{ORTH: 'náà'}]}
]

TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, *exclusions)
