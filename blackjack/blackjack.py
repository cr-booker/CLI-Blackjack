#/usr/bin/env python3
"""
Who doesnt like blackjack?
Some people id imagine but you're not one 
of the losers are you?

This a pretty straight forward command line version 
of blackjack with unicode cards and
a funky ascii card table.
"""
import card
from getpass import getpass as maskinput
import random
import time

class Black_jack():
    """
    Represents a game of blackjack.
    
    Parameters
    ----------
    player_name(String)
        name for human player
        
    Attributes
    ----------
    values(Dict):
        Dictionary of Blackjack card values.
        
    deck(Deck Obj)
        List of card objects.
        
    dealer(Player Obj):
        Computer player.
            
    player(Player Obj):
        Human player.
    
    table_string(String):

    """
    def __init__(self, player_name='Player'):
        self.values = dict({str(i): i for i in range(2, 11)}, Ace=1,
                            Jack=10, Queen=10, King=10)
        self.deck = card.Deck()
        self.dealer = card.player('Dealer')
        self.player = card.player(player_name)
        self.table_wall = 30
        self.table_string = '\n|{:>49}|'  
      
    def menu(self):
        """
        Displays ascii menu.
        
        Returns
        -------
        Output:(None)
        """
        while True:
            
            print("""
            ____________________________________________________
           |   ____  _            _         _            _      |
           |  | __ )| | __ _  ___| | __    | | __ _  ___| | __  |
           |  |  _ \| |/ _` |/ __| |/ / _  | |/ _` |/ __| |/ /  |
           |  | |_) | | (_| | (__|   < | |_| | (_| | (__|   <   |
           |  |____/|_|\__,_|\___|_|\_\ \___/ \__,_|\___|_|\_\\  |
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
        Prints text explaining the rules 
        and objective of blackjack.
        
        https://www.bicyclecards.com/how-to-play/blackjack/
        
        Returns
        -------
        Output:(None)
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
              '\u2022Aces are worth 1 or 11.\n'
              '\u2022Face cards are worth 10.\n' 
              '\u2022Any other card is its pip value.\n')
              
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
     
    def deal(self):
        """
        Shuffles deck and distributes 
        cards to players. 
        If either player
        has blackjack, the winner is determined, 
        all cards are returned to the deck and a new 
        hand is delt.
   
        Returns
        -------
        Output(None)
        """ 
        self.deck.shuffle()
        self.deck.deal(self.dealer.hand, 2)
        self.deck.deal(self.player.hand, 2)
        if self.blackjack_check(): 
            self.clean_up()
            self.deal()
        
    def get_value(self, hand):
        """
        Totals values of cards in players hand.
        
        If the player's hand contains an ace,
        the total is checked to verify it is less than 11
        adding 10 if True(Aces are counted as 1 by default).

        Parameters
        ----------
        hand(list)
            List of cards to total
        
        Returns
        -------
        Output(Int):
            Returns the total value of the cards 
            in players hand
        """
        ranks_in_hand = [i.rank for i in hand]
        total = sum([self.values[i] for i in  ranks_in_hand])
        if 'Ace' in  ranks_in_hand and total<= 11: #Ace Check
            total += 10
        if total <= 9:
            return str(total).zfill(2)
        return total   
    
    def display_table(self):
        """
        Displays ascii cards/table.
        
        Returns
        -------
        Output(None)
        """        
        print('=-=' * 17)
        print("|-Dealer-:{}{:>38}|".format(self.get_value(self.dealer.hand), ''),end='')
        print(self.table_string.format('') * 3)       
        print('|{:>21}{}{:>25}|'.format('', ' '.join([card.unicode for card in self.dealer.hand]), ''))
        print('|{0:>20}{1}{0:>}|'.format('', '=' * 11, self.table_string))
        print('|{:>21}{}{:>25}|'.format('', ' '.join([card.unicode for card in self.player.hand]), ''))
        print(self.table_string.format('') * 2) 
        print('|{0:>40}A)Hit Me!|'.format(''))
        print('|{0:>40}B)Stay!  |'.format(''))
        print('|-Player-:{0}{1:>29}Q)Quit.  |'.format(self.get_value(self.player.hand),''))
        print('=-=' * 17)
        
    def blackjack_check(self):
        """
        Checks if either player has Blackjack.
        
        Returns
        -------
        Output(Bool)
            Returns True if either player has 
            blackjack otherwise returns False.
        """
        if self.get_value(self.player.hand) != 21 and self.get_value(self.dealer.hand) != 21:
             return False
        self.display_table()
        if self.get_value(self.player.hand) == 21 and self.get_value(self.dealer.hand) == 21:
            print("Double Blackjack, Its a tie!")
        elif self.get_value(self.player.hand) == 21:
            print("Blackjack! {} Wins!".format(self.player.player_id))
        elif self.get_value(self.dealer.hand) == 21:
            print("Blackjack! {} Wins!".format(self.dealer.player_id))  
        time.sleep(1)
        maskinput('\nPress Enter To Continue.')
        return True
                  
    def bust_check(self,player):
        """
        Checks if a players hand value is greater 
        than 21.
        
        Parameters
        ----------
        player(Player Obj)
            Players hand to check
        
        Returns
        -------
        Output(Bool)
        """
        if int(self.get_value(player.hand)) > 21:
            print('\n{} Bust!'.format(player.player_id))
            maskinput('\nPress Enter To Continue.')
            self.table_wall = 30
            return True
       
    def dealer_action(self):
        """
        Returns
        -------
        Output(None):
        """
        time.sleep(1)
        while self.get_value(self.dealer.hand) <= 16:
            self.deck.deal(self.dealer.hand, 1)
            print('Dealer Hits.')
            time.sleep(1)
            print("\033c")
            self.display_table() 
            if self.bust_check(self.dealer):
                return
        print('Dealer Stays at {}'.format(self.get_value(self.dealer.hand)))
        time.sleep(1)
        if self.get_value(self.dealer.hand) > self.get_value(self.player.hand):
            print('Dealer wins!')
        elif self.get_value(self.dealer.hand) == self.get_value(self.player.hand):
            print('Its a tie!.')
        else:
            print(self.player.player_id, 'wins!')
        maskinput('\nPress Enter To Continue.')
        self.table_wall = 30
        self.clean_up()
    
    def clean_up(self):
        """
        Returns game to its original state.
        
        The Function is called after the round has ended in some fashion
        (Bust, Blackjack, etc).
        Both players hands are emptied and all cards
        are returned to the deck.
        
        Returns
        -------
        Output(None):
        """
        used_cards = self.player.hand + self.dealer.hand
        self.player.discard_hand()
        self.dealer.discard_hand()
        for card in used_cards:
            self.deck.add_card(card)
        print("\033c")
        
    def game(self):
        """
        The Main game method.
        
        Returns
        -------
        Output(None)
        """
        self.deal()  
        while True:
            self.display_table()  
            if self.bust_check(self.player): 
                self.clean_up()
                self.deal()
                self.display_table()  

            choice = input('>>>').lower()
            if choice == 'a': #Player hits
                self.table_wall -= 2
                self.deck.deal(self.player.hand, 1)
               
            elif choice == 'b': #Player stays         
                self.dealer_action()
                self.deal()
                          
            elif choice == 'q': #Player quits
                while True:
                    print('Are you sure you want to quit(Y/N)?')
                    quit_choice = input().lower()
                    if quit_choice in ('y', 'yes', 'ya', 'yeah'):
                        self.clean_up()
                        return
                    elif quit_choice in ('n', 'no', 'nah', 'nope'):
                        break
            print('\033c')

if __name__ == '__main__':
    bj = Black_jack()
    bj.menu()        
