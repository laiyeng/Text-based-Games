from random import shuffle
##defining the classes
class Cards:
    suits = ["spades","hearts","clubs","diamonds"]
    values = [None,None,"2","3","4","5","6","7","8","9","10","Jack",
              "Queen","King","Ace"]
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]

    def num(self):
        if self.value <= 10:
            return self.value
        else:
            self.value = 10
            return self.value

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Cards(i,j))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cards = None
        self.hand = []
        self.score = 0
        self.chips = 0
        self.bet = 0

class Game:
    def __init__(self):
        name = input("Please enter your name: ")
        age = input("Please enter your age: ")
        self.deck = Deck()
        self.player = Player(name, age)
        self.dealer = Player("dealer", 20)

    def hOrS(self):
        while True:
            x = input("Press 'h' to hit, 's' to stand: ")
            if x == 'h':
                player_new_card = self.deck.remove_card()
                self.player.score += player_new_card.num()
                self.player.hand.append(player_new_card)
                print("Player's new card: ")
                print(player_new_card)
                if self.player.score>21:
                    print("You score is: ",self.player.score)
                    print("You are busted")
                    self.player.chips -= self.player.bet
                    print("You now have", self.player.chips,"chips left!")
                    break
                else:
                    print("You score is: ",self.player.score)
            elif x == 's':
                break
            else:
                print("Press only 'h' or 's'")

    def dealer_draw(self):
        while self.dealer.score<17:
            print("Dealer will now draw another card.")
            dealer_new_card = self.deck.remove_card()
            self.dealer.hand.append(dealer_new_card)
            self.dealer.score += dealer_new_card.num()
            print("Dealer's new card: ")
            print(dealer_new_card)

    def reveal_result(self):
        print("Dealer's score: ", self.dealer.score)
        print("Player's score: ", self.player.score)
        if self.dealer.score > self.player.score:
            if self.dealer.score < 22:
                print("You lost!")
                self.player.chips -= self.player.bet
                print("You now have", self.player.chips,"chips left!")
            else:
                print("Dealer has busted! You win!")
                self.player.chips += self.player.bet
                print("You now have", self.player.chips,"chips left!")
        elif self.dealer.score < self.player.score:
            print("You win!")
            self.player.chips += self.player.bet
            print("You now have", self.player.chips,"chips left!")
        else:
            print("It's a tie!")
            self.player.chips = self.player.chips
            print("You now have", self.player.chips,"chips left!")

    def play_game(self):
        print("Welcome to the game, " + self.player.name)
        print("Let's get STARTED!")
        response = None
        total_chip = input("ENTER Total Chip amount: ")
        self.player.chips = int(total_chip)
        print("Okay! You now have",self.player.chips,"chips!")
        while True and self.player.chips > 0:
            bet = int(input("How much are you betting this game? "))
            self.player.bet = bet
            cards = self.deck.cards #create the deck for the game under the name cards
            self.player.hand = []
            self.dealer.hand = []
            self.player.score = 0
            self.dealer.score = 0
            player_card = self.deck.remove_card()
            self.player.score += player_card.num()
            player_card2 = self.deck.remove_card()
            self.player.score += player_card2.num()
            dealer_card = self.deck.remove_card()
            self.dealer.score += dealer_card.num()
            self.player.hand.append(player_card)
            self.player.hand.append(player_card2)
            self.dealer.hand.append(dealer_card)
            print("Dealer's card: {} \nPlayer's cards: {} and {}".format(dealer_card,player_card, player_card2))
            print("Dealer's score: {} \nPlayer's score: {}".format(self.dealer.score, self.player.score))
            game.hOrS()
            if self.player.score <22:
                game.dealer_draw()
                game.reveal_result()
        restart = input("Do you want to start a new game? Press 'yes' if so! ")
        if restart == 'yes':
            game.play_game()
        

game = Game()
game.play_game()
