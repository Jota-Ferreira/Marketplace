#Create a marketplace for people and organizations to buy and sell pieces of art!

#In this project we’ll be developing classes and objects that represent the various responsibilities of art dealership software.

#A model or struture for art pieces
class Art:
  def __init__(self, artist, title, medium, year):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
  
  def __repr__(self):
    return '%s. "%s". %s, %s.'%(self.artist, self.title, self.year, self.medium)

#testing Art class
monalisa = Art('Da Vinci, Leonardo', 'Mona Lisa', 'oil and canvas', 1503)

the_scream = Art('Munch, Edvard', 'The scream', 'oil and canvas', 1893)
#print(monalisa)

class Marketplace:
  def __init__(self):
    self.listings = []
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)

  def show_listings(self):
    if self.listings == []:
      print('The list is empty.')
    else:
      for item in self.listings:
        print(item)

#testing add_listing method
moma = Marketplace()

#to add monalisa --> moma.add_listing(monalisa)
#moma.show_listings()
#it works! #printed monalisa object

moma.add_listing(monalisa)
moma.add_listing(the_scream)
moma.show_listings()
moma.remove_listing(monalisa)
moma.show_listings()