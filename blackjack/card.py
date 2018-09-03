#/usr/bin/env python3
"""
Who doesnt like blackjack?
Some people id imagine but youre not one 
of the losers are you?

This a command line version of blackjack with 
unicode cards and a funky ascii card table.
pretty straight forward.
"""
import operator
import random

class Card():
    """
    Represents a standard playing card.
        
    Parameters
    ----------
    rank(String):
        A string representing the card objects 
        rank i.e 'King','Queen', etc.
           
    suit(String):
        A string representing the card objects 
        Suit i.e 'Club','Diamond', etc.
        
    Attributes
    ----------
    rank(String):
        A string representing the card objects 
        rank i.e 'King','Queen', etc.
    
    suit(String):
         A string representing the card objects 
         Suit i.e 'Club','Diamond', etc.
    
    unicode(String)
        Unicode character for displaying the 
        'front' of card, showing suit and rank.
    
    unicodeBack(String)
        Unicode character for displaying the back of card.
    """
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs', )
    
    ranks = ('Ace', '2', '3', '4', '5', '6', '7',
        	 '8', '9', '10', 'Jack', 'Queen', 'King')
        	 
    uni_strings = {"Ace of Spades": "\U0001F0A1", "Ace of Hearts": "\U0001F0B1", 
                   "Ace of Diamonds": "\U0001F0C1", "Ace of Clubs": "\U0001F0D1", 
                   "2 of Spades": "\U0001F0A2", "2 of Hearts": "\U0001F0B2", 
                   "2 of Diamonds": "\U0001F0C2", "2 of Clubs": "\U0001F0D2", 
                   "3 of Spades": "\U0001F0A3", "3 of Hearts": "\U0001F0B3", 
                   "3 of Diamonds": "\U0001F0C3", "3 of Clubs": "\U0001F0D3", 
                   "4 of Spades": "\U0001F0A4", "4 of Hearts": "\U0001F0B4", 
                   "4 of Diamonds": "\U0001F0C4", "4 of Clubs": "\U0001F0D4", 
                   "5 of Spades": "\U0001F0A5", "5 of Hearts": "\U0001F0B5", 
                   "5 of Diamonds": "\U0001F0C5", "5 of Clubs": "\U0001F0D5", 
                   "6 of Spades": "\U0001F0A6", "6 of Hearts": "\U0001F0B6", 
                   "6 of Diamonds": "\U0001F0C6", "6 of Clubs": "\U0001F0D6", 
                   "7 of Spades": "\U0001F0A7", "7 of Hearts": "\U0001F0B7", 
                   "7 of Diamonds": "\U0001F0C7", "7 of Clubs": "\U0001F0D7", 
                   "8 of Spades": "\U0001F0A8", "8 of Hearts": "\U0001F0B8", 
                   "8 of Diamonds": "\U0001F0C8", "8 of Clubs": "\U0001F0D8", 
                   "9 of Spades": "\U0001F0A9", "9 of Hearts": "\U0001F0B9", 
                   "9 of Diamonds": "\U0001F0C9", "9 of Clubs": "\U0001F0D9", 
                   "10 of Spades": "\U0001F0AA", "10 of Hearts": "\U0001F0BA", 
                   "10 of Diamonds": "\U0001F0CA", "10 of Clubs": "\U0001F0DA", 
                   "Jack of Spades": "\U0001F0AB", "Jack of Hearts": "\U0001F0BB", 
                   "Jack of Diamonds": "\U0001F0CB", "Jack of Clubs": "\U0001F0DB", 
                   "Queen of Spades": "\U0001F0AD", "Queen of Hearts": "\U0001F0BD", 
                   "Queen of Diamonds": "\U0001F0CD", "Queen of Clubs": "\U0001F0DD", 
                   "King of Spades": "\U0001F0AE", "King of Hearts": "\U0001F0BE", 
                   "King of Diamonds": "\U0001F0CE", "King of Clubs": "\U0001F0DE"}	 
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.unicode = self.uni_strings[str(self)]
        self.unicode_back = '\U0001F0A0'
        
    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)
    
    def __eq__(self, other):
        return (self.rank, self.suit) == (other.rank, other.suit)
        

class Deck():
    """
    Represents standard 52 card playing card deck.
    
    Attributes
    ----------
    deck(List):
        List of 52 card objects built using list 
        comprehension
    """
    def __init__(self):
        self.deck = [Card(rank,suit) for rank in Card.ranks for suit in Card.suits]
        
    def __str__(self):
        return [str(i) for i in self.deck]
        
    def __eq__(self, other):
        return len(self.deck) == len(other.deck)
        
    def shuffle(self):
        """
        Scrambles the list of card objects.
        
        Returns
        -------
        Output(None)
        """
        random.shuffle(self.deck)
    
    def add_card(self,card):
        """
        Appends a card object to deck 
        list attribute.
        
        Parameters
        ----------
        Card(Card Object)
            The card to be added to the deck
        
        Returns
        -------
        Output(None)
        """
        self.deck.append(card)
    
    def remove_card(self, card):
        """
        Removes a card from self.deck list attribute.
        
        Parameters
        ----------
        Card(Card Object)
            Card object to remove from deck
        
        Returns
        -------
        Output(None)
        """
        self.deck.remove(card)
    
    def pop_card(self, position=-1):
        """
        Removes and returns a card from the deck
        
        Parameters
        ----------
        position(int):
           The index of the card to be removed.
           
        Returns
        -------
        Output(Card Object)
            The card object in the self.deck list attribute
            at the given index(position).
        """
        return self.deck.pop()
        
    def deal(self, hand, num_of_cards):
        """
        
        Parameters
        ----------
        hand(list)
            The list to append the cards to.
        
        num_of_cards(int)
            The Number of cards to remove from 
            the self.deck list attribute and append to the 
            hand parameter.
        
        Returns
        -------
        Output(None)
        """
        for i in range(num_of_cards):
            hand.append(self.pop_card())
              
              
class player():
    """
    Represents a player
        
    Parameters
    ----------
    player_id(String):
         Name assigned to player
        
    Attributes
    ----------
    player_id(String):
        Name assigned to player
        
    hand(List):
        List of cards owned by player       
    """   
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = []
        
    def sort_hand(self):
        """
        Returns
        -------
        Output:(None)
        """
        #sorted(self.hand.sort(key=operator.attrgetter('player.hand'))
    
    def discard_hand(self):
        """
        Empties the self.hand list attribute.
        
        Returns
        -------
        Output:(None)
        """
        del self.hand[:]
        
    def add_card(self, card):
        """
        Appends a new card object 
        to the self.hand attribute.
        
        Parameters
        ----------
        card(string)
        
        Returns
        -------
        Output:(None)
        """
        self.hand.append(card)
        
    def remove_card(self, card):
        """
        removes card object 
        from self.hand list attribute.
        
        Parameters
        ----------
        Card(string)
            Card object to be removed from 
            the deck.
              
        Returns
        -------
        Output:(None)
        """
        self.hand.remove(card)
        
    def pop_card(self, position=-1):
        """
        Removes and returns card object from deck
        Parameters
        ----------
        position(int):
           The index of the card to be removed.
           
        Returns
        -------
        Output(Card Object)
            The card object in the self.hand list 
            at the given index(position).
        """
        return self.hand.pop()




    
        
