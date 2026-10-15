import re

with open("inject_full_engine.py", "r", encoding="utf-8") as f:
    text = f.read()

contractions = [
    ("hasn't", r"hasn\'t"),
    ("didn't", r"didn\'t"),
    ("don't", r"don\'t"),
    ("won't", r"won\'t"),
    ("isn't", r"isn\'t"),
    ("aren't", r"aren\'t"),
    ("wasn't", r"wasn\'t"),
    ("weren't", r"weren\'t"),
    ("couldn't", r"couldn\'t"),
    ("shouldn't", r"shouldn\'t"),
    ("wouldn't", r"wouldn\'t"),
    ("it's", r"it\'s"),
    ("that's", r"that\'s"),
    ("what's", r"what\'s"),
    ("there's", r"there\'s"),
    ("here's", r"here\'s"),
    ("let's", r"let\'s"),
    ("we'll", r"we\'ll"),
    ("they'll", r"they\'ll"),
    ("I'm", r"I\'m"),
    ("you're", r"you\'re"),
    ("they're", r"they\'re"),
    ("haven't", r"haven\'t"),
    ("doesn't", r"doesn\'t"),
    ("can't", r"can\'t"),
    ("It's", r"It\'s"),
    ("Don't", r"Don\'t"),
    ("Won't", r"Won\'t"),
    ("Didn't", r"Didn\'t"),
    ("Haven't", r"Haven\'t"),
    ("Doesn't", r"Doesn\'t"),
    ("Can't", r"Can\'t"),
    ("Let's", r"Let\'s"),
    ("What's", r"What\'s"),
    ("customer's", r"customer\'s"),
    ("company's", r"company\'s"),
    ("manager's", r"manager\'s"),
    ("yesterday's", r"yesterday\'s"),
    ("today's", r"today\'s"),
    ("week's", r"week\'s"),
    ("director's", r"director\'s"),
    ("world's", r"world\'s")
]

for old, new in contractions:
    text = re.sub(r'(?<!\\)' + re.escape(old), new, text)

with open("inject_full_engine.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Finished fixing contractions in inject_full_engine.py")
