class France:
    def language(self):
        print('French')
    def capital(self):
        print('Italy')
    def type(self):
        print('Developed country')
class Indonesia:
    def language(self):
        print("Indonesian")
    def capital(self):
        print('Jakarta')
    def type(self):
        print("Dveloping country")
obj=France()
obj1=Indonesia()
for country in (obj,obj1):
    country.language()
    country.capital()
    country.type()