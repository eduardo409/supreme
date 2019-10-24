import sys
sys.path.append('./common') #required so that i can import my modules
sys.path.append('./model')
from item import Item
from purchase import Purchase
from client import Client 
from credit import Credit
import json

cred = json.load(open('../cred.json'))
creditCard = Credit(cred)
# Client(credit)
eduardo = Client(creditCard,'jr@gmail.com', '1234567890')
# Item (name, color, size, item_type)
item = Item('Duffle Bag','Dark Orange', 'XLarge', 'bags')
# page reload frequency
frequency = 5
bot = Purchase(item,eduardo, frequency)
bot.start()

def test(bot):
    print('keep alive')