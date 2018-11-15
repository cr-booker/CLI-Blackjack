#/usr/bin/env python3
"""
Who doesnt like blackjack?
Some people id imagine but youre not one 
of the losers are you?

This a command line version of blackjack with 
unicode cards and a funky ascii card table.
pretty straight forward.
"""
import card
from getpass import getpass as maskinput
import random
import time

class Black_jack():
    """
    Represents a game of blackjack
    
    Parameters
    ----------
    player_name(String)
        name for human player
        
    Attributes
    ----------
    values(Dict):
        Dictionary of Blackjack card values
        
    deck(Deck Obj)
        
        
    dealer(Player Obj):
        
        
    player(Player Obj):
    
    
    table_string(String):

    """
    def __init__(self, player_name='Player'):
        self.values = dict({str(i): i for i in range(2, 11)}, Ace=1,
                            Jack=10, Queen=10, King=10)
        self.deck = card.Deck()
        self.dealer = card.player('Dealer')
        self.player = card.player(player_name)
        self.table_wall = 30
        self.table_string = '\n|'+ ' ' * 58 +'|' 
      
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
        Prints text explaining the rules and objective 
        of blackjack.
        
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
            print('\033c')
        
    
    def get_value(self, hand):
        """
        Totals values of cards in players hand.
        
        If the player's hand contains an ace,
        the total is checked to verify it is less than 11
        adding 10 if True(Aces are counted as 1 by default).

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
    
    def display_table(self):
        """
        Displays ascii table.
        
        Returns
        -------
        Output(None)
        """
        p_wall = 37
        print('=-=' * 20,
               '\n|-Dealer-:', self.get_value(self.dealer.hand), ' '.rjust(45),'|',
               self.table_string* 4, #'\n|'+ ' ' * 58 +'|'
               '\n|', ' ' * 22, ' '.join([card.unicode for card in self.dealer.hand]) , ' ' * 30 +'|',
               '\n|', ' ' * 20, '=' *  13, ' ' * 21, '|',
               '\n|', ' ' * 22, ' '.join([card.unicode for card in self.player.hand]) , ' ' * self.table_wall +'|',
               self.table_string * 2,
               '\n|' + ' ' * 48,'A)Hit Me!' +'|',
               '\n|'+ ' ' * 50,'B)Stay!' + '|',
               '\n|-Player-:',self.get_value(self.player.hand), ' ' * p_wall, 'Q)Quit.'+ '|\n'+
               '=-=' * 20)
        
    def blackjack_check(self):
        """
        Checks if either player has Blackjack.
        
        Returns
        -------
        Output(Bool)
            Returns True if either player has 
            blackjack otherwise returns False.
        """
        blackjack = True
        if self.get_value(self.player.hand) != 21 and self.get_value(self.dealer.hand) != 21:
             blackjack = False
             return blackjack
        self.display_table()
        if self.get_value(self.player.hand) == 21 and self.get_value(self.dealer.hand) == 21:
            print("Double Blackjack, Its a tie!")
        elif self.get_value(self.player.hand) == 21:
            print("Blackjack! {} Wins!".format(self.player.player_id))
        elif self.get_value(self.dealer.hand) == 21:
            print("Blackjack! {} Wins!".format(self.dealer.player_id))  
        time.sleep(1)
        maskinput('\nPress Enter To Continue.')
        return blackjack
                  
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
        if self.get_value(player.hand) > 21:
            print('\n{} Bust!'.format(player.player_id))
            maskinput('\nPress Enter To Continue.')
            self.table_wall = 30
            self.clean_up()
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
            print('{} Stays at {}'.format(self.player.player_id, self.get_value(self.player.hand)))
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
        are returned to the deck, the deck is shuffled 
        and two cards are delt to the player and dealer.
        
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
        Returns
        -------
        Output(None)
        """
        self.deal()  
        while True:
            self.display_table()  
            if self.bust_check(self.player): #checks if user busts
                self.clean_up()
                self.deal()
                continue        
            choice = input('>>>')
            if choice == 'a': 
                self.table_wall -= 2
                self.deck.deal(self.player.hand, 1)
                print('\033c')
                continue

            elif choice == 'b':             
                self.dealer_action()
                self.deal()
                continue
                          
            elif choice == 'q':
                while True:
                    print('Are you sure you want to quit(Y/N)?')
                    quit_choice = input()
                    if quit_choice in ('y', 'yes', 'ya' , 'yeah'):
                        self.clean_up()
                        print("\033c")
                        return
                    break
            print('\033c') #clears screen so new table can be printed 

if __name__ == '__main__':
    bj = Black_jack()
    bj.menu()        
