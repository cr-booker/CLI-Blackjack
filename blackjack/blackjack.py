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
import time

input()




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
        
    dealer(Player Obj):
        
    player(Player Obj):
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
        
    def player_bust(self):
        """
        Returns
        -------
        Output(None)
        """
        if self.get_value(self.player.hand) > 21:
            print('\nPlayer Bust!')
            maskinput('\nPress Enter To Continue.')
            self.table_wall = 30
            self.clean_up()
            print("\033c")
            return True
    
    def get_value(self, hand):
        """
        Totals values of cards in players hand.
        
        If the player's hand contains an ace,
        the total is checked to see if it is less than 11
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
   
    def blackjack_check(self, hand):
        """
        Returns
        -------
        Output(Bool)
        """
        return self.get_value(hand) == 21
            
    def dealer_action(self):
        """
        Returns
        -------
        Output(None):
        """
        while self.get_value(self.dealer.hand) <= 16:
            self.deck.deal(self.dealer.hand, 1)
            print('Dealer Hits.')
            time.sleep(1)
            print("\033c")
            self.display_table()
            if self.get_value(self.dealer.hand) > 21:
                print('Dealer Busts!')
                maskinput('\nPress Enter To Continue.')
                self.table_wall = 30
                self.clean_up()
                print("\033c")
                return
        print('Dealer Stays at {}'.format(self.get_value(self.dealer.hand)))
        time.sleep(1)
        if self.get_value(self.dealer.hand) > self.get_value(self.player.hand):
            print('Dealer wins!')
        else:
            print(self.player.player_id, 'wins!')
        maskinput('\nPress Enter To Continue.')
        self.table_wall = 30
        self.clean_up()
        print("\033c")
        
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
        for card in used_cards:
            self.deck.add_card(card)
        self.deck.shuffle()
        self.player.discard_hand()
        self.dealer.discard_hand()
        
    def display_table(self):
        p_wall = 37
        print('=-=' * 20,
               '\n|-Dealer-:', self.get_value(self.dealer.hand), ' ' * 45,'|',
               self.table_string* 4,
               '\n|', ' ' * 22, ' '.join([i.unicode for i in self.dealer.hand]) , ' ' * 30 +'|',
               '\n|', ' ' * 20, '=' *  13, ' ' * 21, '|',
               '\n|', ' ' * 22, ' '.join([i.unicode for i in self.player.hand]) , ' ' * self.table_wall +'|',
               self.table_string * 2,
               '\n|' + ' ' * 48,'A)Hit Me!' +'|',
               '\n|'+ ' ' * 50,'B)Stay!' + '|',
               '\n|-Player-:',self.get_value(self.player.hand), ' ' * p_wall, 'Q)Quit.'+ '|\n'+
               '=-=' * 20)
               
    def deal(self):
        """
        Returns
        -------
        Output(None)
        """
        self.deck.shuffle()
        self.deck.deal(self.player.hand, 2)
        self.deck.deal(self.dealer.hand, 2) 
        
    def game(self):
        """
        Returns
        -------
        Output(None)
        """
        table_string = '\n|'+ ' ' * 58 +'|' 
        #p_wall = 37   #player_text 
        self.deal()
        while True:            
            self.display_table()  
            if self.player_bust():  
                continue           
            choice = input('>>>')
            
            if choice == 'a': 
                self.table_wall -= 2
                self.deck.deal(self.player.hand, 1)

            elif choice == 'b':
                self.dealer_action()
                self.clean_up()
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
            print('\033c')

if __name__ == '__main__':
    bj = Black_jack()
    bj.menu()

    
        