import db

for language in db.languages.get():
    print(language)