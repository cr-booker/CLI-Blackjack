#/usr/bin/env python3

"""
Who doesnt like blackjack?
Some people id imagine but youre not one 
of the losers are you?

A commandline implementation of black jack with 
unicode cards and a funky ascii card table.
pretty straight forward.q

"""
from getpass import getpass as maskinput
import operator
import random

class Card():
    """
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
    """
    def __init__(self):
        self.deck = []
        
    def __str__(self):
        return [str(i) for i in self.deck]
        
    def __eq__(self, other):
        return len(self.deck) == len(other.deck)
    
    def build_deck(self):
        """
        Returns
        -------
        Output(None)
        """
        self.deck = [Card(rank,suit) for rank in Card.ranks for suit in Card.suits]
        
    def deck_count(self):
        """
        """
        return len(self.deck)
        
    def shuffle(self):
        """
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
        Parameters
        ----------
        Card(Card Object)
        
        Returns
        -------
        Output(None)
        """
        self.deck.remove(card)
    
    def pop_card(self, position=-1):
        """
        Parameters
        ----------
        """
        return self.deck.pop()
        
    def deal(self, hand, num_of_cards):
        """
        Parameters
        ----------
        hand(list)
        
        num_of_cards(int)
        
        
        Returns
        -------
        Output(None)
        """
        for i in range(num_of_cards):
            hand.append(self.pop_card())
              
              
class player():
    
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
           
        Returns
        -------
        Output:(None)
        """
        self.hand.remove(card)
        
    
class Black_jack():
    """
    """
    def __init__(self, player_name= 'Player'):
        """
        """
        self.values = dict({str(i): i for i in range(2, 11)}, Ace=1,
                            Jack=10, Queen=10, King=10)
        self.deck = Deck()
        self.dealer = player('Dealer')
        self.player = player(player_name)
        self.player_total = 0
        self.dealer_total = 0
    
    def menu(self):
        
        while True:
            
            print("""
            ____________________________________________________
           |   ____  _            _          _            _     |
           |  | __ )| | __ _  ___| | __     | | __ _  ___| | __ |
           |  |  _ \| |/ _` |/ __| |/ /  _  | |/ _` |/ __| |/ / |
           |  | |_) | | (_| | (__|   <  | |_| | (_| | (__|   <  |
           |  |____/|_|\__,_|\___|_|\_\  \___/ \__,_|\___|_|\_\\ |
           |____________________________________________________|
             
                \   / \ / \ / \ / \ 
               1 ) ( P   L   A   Y )
                /   \_/ \_/ \_/ \_/ 
                
                \   / \ / \ / \ / \ / \ 
               2 ) ( R   U   L   E   S )
                /   \_/ \_/ \_/ \_/ \_/ 
                
                \   / \ / \ / \ / \ 
               3 ) ( Q   U   I   T ) 
                /   \_/ \_/ \_/ \_/ 

             """)
            choice = input('>>>')
            if choice == '1':
               print("\033c")
               self.game()
               
            elif choice == '2':
                print("\033c")
                self.rules()
               
            elif choice == '3':
                print("  ____                 _ _                _\n"
                      " / ___| ___   ___   __| | |__  _   _  ___| |\n"
                     "| |  _ / _ \ / _ \ / _` | '_ \| | | |/ _ \ |\n"
                     "| |_| | (_) | (_) | (_| | |_) | |_| |  __/_|\n"
                     " \____|\___/ \___/ \__,_|_.__/ \__, |\___(_)\n"
                     "                               |___/")
                return
                
            else:
                print("\033c")
   
    def rules(self):
        """
        Prints text explaing the rules and objective 
        of the game.
        
        Output(None):
        """
        print(' _____________________________\n'
              '|  |  _ \ _   _| | ___  ___   |\n'
              '|  | |_) | | | | |/ _ \/ __|  |\n'
              '|  |  _ <| |_| | |  __/\__ \  |\n'
              '|  |_| \_\\\__,_|_|\___||___/  |\n'
              '|_____________________________|\n')

        print('Object of the Game\n'
              '===================\n'
              'The player must attempt to beat the dealer by getting\n'
              'a count as close to 21 as possible, without going over.\n'
              
              '\nCard Values/Scoring\n'
              '===================\n'
              'Aces are worth 1 or 11.\n'
              'Face cards are 10 and.\n' 
              'Any other card is its pip value.\n')
              
        maskinput('\nPress Enter To Continue.')
        print('\033c')
        print('The Deal\n'
              '========\n'
              'The dealer will give two cards to the player\n'
              'and two cards to himself.\n' 
              'Only One of the dealers cards is dealt face up.\n'
              
              '\nIf the players first two cards are an ace and a "ten-card"(a picture card or 10),\n'
              'totaling 21 , this is called a "blackjack", \n'
              'counting as a win for the player.\n'
                     
              '\nIf the dealer has a ten or an ace showing\n,'
              'then he will check the facedown card to see if he has a blackjack.\n'
              'If the dealer has a blackjack, then the player loses,\n'
              'unless the player also has a blackjack, resulting in a tie.\n')
        maskinput('\nPress Enter To Continue.')
        print('\033c')
        
        print('The Play\n'
              '========\n'
              'The following are the choices available to the player:\n'
              '\u2022Hit: Asking for another card in an attempt to get closer to 21\n'
              '\u2022Stay: not ask for another card keeping your current count\n'
              '\nThe player may stay on the two cards originally dealt him,\n'
              'or he may ask the dealer for additional cards, one at a time,\n'
              'until he either decides to stay on the total (under 21),\n'
              'or goes "bust" (over 21)\n'
              
              "\nThe Dealer's Play\n"
              '=================\n'
              'the dealer will reveal is face down card.\n'
              'If the total is 17 or more, he must stand. If the total is 16 or under,\n' 
              'he must take a card. He must continue to take cards\n'
              'until the total is 17 or more\n'             
              '\nThe Player wins if the dealer goes over 21 points(busts)\n'
              'or stays at a lesser total than the player.\n')

             
        maskinput('\nPress Enter To Return To Menu.')
        print('\033c')
      
    def get_value(self, hand):
        """
        
        Parameters
        ----------
        hand(list)
            List containing card objects to total
        
        Returns
        -------
        Output(Int):
            Returns the total value of the cards 
            in players hand
        """
        hand_ranks = [i.rank for i in hand]
        total = sum([self.values[i] for i in hand_ranks])
        if 'Ace' not in hand_ranks:
            return total
        if total <= 11:
            return total + 10
        return total
        
    def dealer_action(self):
        """
        """
        pass
    
    def deal(self):
        self.player.discard_hand()
        self.dealer.discard_hand()
        self.deck.deal(self.player.hand, 2)
        self.deck.deal(self.dealer.hand, 2)
        self.player_total = self.get_value(self.player.hand)
        self.dealer_total = self.get_value(self.dealer.hand)
       
    def game(self):
        """
        Returns
        -------
        Output:
        """
        self.deck.build_deck()
        self.deck.shuffle()
        self.deal()
        table_string = '\n|'+ ' ' * 58 +'|' 
        table_wall = 30
        while True:
            
            print('=-=' * 20,
                  '\n|-Dealer-:'+ str(self.dealer_total) + ' ' * 46,'|',
                  table_string* 4,
                  '\n|', ' ' * 22, ' '.join([i.unicode for i in self.dealer.hand]) , ' ' * 30 +'|',
                  
                 
                  '\n|', ' ' * 20, '=' *  13, ' ' * 21, '|',
                  '\n|', ' ' * 22, ' '.join([i.unicode for i in self.player.hand]) , ' ' * table_wall +'|',
                  table_string * 2,
                  '\n|' + ' ' * 48,'A)Hit Me!' +'|',
                  '\n|'+ ' ' * 50,'B)Stay!' + '|',
                  '\n|-Player-:' + str(self.player_total), ' ' * 38, 'Q)Quit.' + '|')
                  
            print('=-=' * 20)
            if self.player_total > 21:
                table_wall -= 2
                print('\nPlayer Bust!')
                maskinput('\nPress Enter To Continue.')
                table_wall = 30
                self.deal()
                print("\033c")
                continue
                
            choice = input()
            
            if choice == 'a':
                
                table_wall -= 2
                self.deck.deal(self.player.hand, 1)
                self.player_total = self.get_value(self.player.hand)
            
                    
                
            elif choice == 'b':
                self.dealer_play()
                
            elif choice == 'q':
                while True:
                    print('Are you sure you want to quit(Y/N)?')
                    quit_choice = input()
                    if quit_choice in ('y', 'yes', 'ya' , 'yeah'):
                        print("\033c")
                        return
                    break
            print('\033c')

        
            
    


if __name__ == '__main__':
    
    bj = Black_jack()
    bj.menu()

    
        
