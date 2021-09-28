## 1) This file is missing imports. Debug and add the missing imports.
## 2) Change this to draw 5 cards instead of 2,
## 3) using the reference, change the deck so it is shuffled
## https://deckofcardsapi.com/


url = 'https://deckofcardsapi.com/api/deck/'	#### this is the base url
resp=requests.get(url+'new/')                                 

deck=json.loads(resp.text)
decknumber=deck['deck_id']

drawurl=url+decknumber+'/draw/?count=2'
                           
cards=requests.get(drawurl)				############ get   2 cards from deck

jsoncards=json.loads(cards.text)			######## load it into json

for card in jsoncards['cards']:
  print(card['value'],card['suit'])
