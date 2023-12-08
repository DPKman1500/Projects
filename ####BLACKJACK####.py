
####BLACKJACK####
import random

cards = {1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Queen", 12:"Jack", 13:"King"}
dealer_score = 0
player_score = 0

def draw_card_number():
    drawn_card = random.randint(1,13)
    card = cards.get(drawn_card)
    return card

def draw_card_suit():
    card_suit_number = random.randint(1,4)
    if card_suit_number == 1:
        card_suit = "Spades"
    if card_suit_number == 2:
        card_suit = "Clubs"
    if card_suit_number == 3:
        card_suit = "Diamonds"
    if card_suit_number == 4:
        card_suit = "Hearts"
    return card_suit



   

