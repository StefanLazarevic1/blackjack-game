import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []  
        self.create_deck()  
        self.shuffle()  

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)  
                self.cards.append(card)   

    def shuffle(self):
        random.shuffle(self.cards)  

    def draw_card(self):
        return self.cards.pop() if self.cards else None

class Game:
    def __init__(self):
        self.deck = Deck()  
        self.player_hand = []  
        self.dealer_hand = []  

    def deal_initial_cards(self):
        for _ in range(2):
            self.player_hand.append(self.deck.draw_card())
            self.dealer_hand.append(self.deck.draw_card())

    def calculate_score(self, hand):
        score = 0
        aces = 0

        for card in hand:
            if card.rank in ['Jack', 'Queen', 'King']:
                score += 10
            elif card.rank == 'Ace':
                score += 11
                aces += 1
            else:
                score += int(card.rank)

        while score > 21 and aces:
            score -= 10
            aces -= 1

        return score

    def player_turn(self):
        while True:
            print(f"Your hand: {[str(card) for card in self.player_hand]}")
            action = input("Do you want to hit or stand? (h/s): ")
            if action.lower() == 'h':
                self.player_hand.append(self.deck.draw_card())
                if self.calculate_score(self.player_hand) > 21:
                    print("You bust! Dealer wins.")
                    return False
            elif action.lower() == 's':
                break
            else:
                print("Invalid input. Please enter 'h' to hit or 's' to stand.")
        return True

    def dealer_turn(self):
        while self.calculate_score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.draw_card())

    def determine_winner(self):
        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)
        print(f"Your score: {player_score}, Dealer's score: {dealer_score}")

        if player_score > 21:
            print("You bust! Dealer wins.")
        elif dealer_score > 21 or player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("Dealer wins.")
        else:
            print("It's a tie!")
    def play_game(self):
        while True:
            self.deck = Deck()  
            self.player_hand = []  
            self.dealer_hand = []  
            
            self.deal_initial_cards()  
            
            if self.player_turn():  
                self.dealer_turn()  
                self.determine_winner()  
            
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() != 'y':
                print("Thanks for playing!")
                break  
if __name__ == "__main__":
    game = Game()  
    game.play_game()  |
