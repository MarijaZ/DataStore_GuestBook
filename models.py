from google.appengine.ext import ndb



class Sporocilo(ndb.Model):
    ime_priimek = ndb.StringProperty()
    email = ndb.StringProperty()
    tekst = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
# DataStore_GuestBook
