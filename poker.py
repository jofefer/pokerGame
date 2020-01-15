# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:49:23 2020

Refrescando mis skills de programador.
Voy a hacer un juego de poker sencillo para
refrescar mi memoria

@author: JFEMENIAFERRER
"""
import random


class Card():

    RANK = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    SUITS = ('D','S','C','H')

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "Card({}, '{}'),".format(self.rank, self.suit)

    def __eq__(self, other):
        return self.suit == other.suit

    def __ne__(self, other):
        return not self.suit == other.suit


class Deck():

    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANK:
                self.deck.append(Card(rank,suit))

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self) == 0:
            return None
        else:
            return self.deck.pop(0)


class Poker():
    def __init__(self, numHands):
        self.deck = Deck()
        maxCardInHand = 5
        self.numHands = numHands
        self.hands = []
        self.tlist = []

        self.deck.shuffle()

        for handNum in range(0,self.numHands):
            hand = []
            for numcard in range(maxCardInHand):
                hand.append(self.deck.deal())

            hand = sorted(hand, key=lambda x: x.rank)
            self.hands.append(hand)
            
        for hand in self.hands:
            self.tlist.append(0)


    def isStraightFlush(self, hand):
        if self.isStraight(hand) == True and self.isFlush(hand) == True:
            return True
        else:
            return False

    def isStraight(self,hand):
        prevCard = hand[0]
        allConcatenate = True
        for card in hand[1:]:
            if card.rank - prevCard.rank == 1 and allConcatenate:
                allConcatenate = True
            else:
                allConcatenate = False
            prevCard = card

        #print("Is your hand a Straight?: ",str(allConcatenate))

        maxRank = max(card.rank for card in hand)
        pokerHand = 600
        self.points = pokerHand + maxRank
        return allConcatenate


    def isFlush(self,hand):
        prevCard = hand[0]
        allSameClub = True
        for card in hand[1:]:
            if card == prevCard and allSameClub:
                allSameClub = True
            else:
                allSameClub = False
            prevCard = card

        #print("Is your hand a Flush?: ",str(allSameClub))
        return allSameClub

    def printHand(self, hand):
        for card in hand:
            print(card)

    def is4ofKind(self, hand):
        prevCard = hand[0]
        fourSame = False
        howSame = 1
        
        for card in hand[1:]:
            if prevCard.rank == card.rank:
                howSame += 1
                if howSame == 4:
                    fourSame = True
            else:
                howSame = 1
            prevCard = card
        
            
        return fourSame
    
    
    def is3ofKind(self, hand):
        prevCard = hand[0]
        howSame = 1
        threeOfKind = False
        
        for card in hand[1:]:
            if prevCard.rank == card.rank:
                howSame += 1
                if howSame == 3:
                    threeOfKind = True
            else:
                howSame = 1
            
            prevCard = card

        return threeOfKind
    

    def isDoublePair(self, hand):
        prevCard = hand[0]
        howSame = 1
        doublePair = 0
        
        for card in hand[1:]:
            if prevCard.rank == card.rank:
                howSame += 1
            if howSame == 2:
                    doublePair += 1
            else:
                howSame = 1

            prevCard = card
        
        if doublePair == 2:
            return True
        else:
            return False
        

    def isPair(self, hand):
        prevCard = hand[0]
        howSame = 1
        
        for card in hand[1:]:
            if prevCard.rank == card.rank:
                howSame += 1

            prevCard = card
        if howSame == 2:
            return True
        else:
            return False

             
        

    def isFullHouse(self, hand):
        if self.isDoublePair(hand) and self.is3ofKind(hand):
            return True
        else:
            return False
    

    def game(self):
        for hand in self.hands:
            #print("this hand is: ")
            #for card in hand:
                #print(card)
                
            if self.isStraightFlush(hand):
                self.tlist[self.hands.index(hand)] = 800 + max(card.rank for card in hand)
            elif self.is4ofKind(hand):
                self.tlist[self.hands.index(hand)] = 700 + max(card.rank for card in hand)
            elif self.isFullHouse(hand):
                self.tlist[self.hands.index(hand)] = 600 + max(card.rank for card in hand)
            elif self.isFlush(hand):
                self.tlist[self.hands.index(hand)] = 500 + max(card.rank for card in hand)
            elif self.isStraight(hand):
                self.tlist[self.hands.index(hand)] = 400 + max(card.rank for card in hand)
            elif self.is3ofKind(hand):
                self.tlist[self.hands.index(hand)] = 300 + max(card.rank for card in hand)
            elif self.isDoublePair(hand):
                self.tlist[self.hands.index(hand)] = 200 + max(card.rank for card in hand)
            elif self.isPair(hand):
                self.tlist[self.hands.index(hand)] = 100 + max(card.rank for card in hand)
            else:
                self.tlist[self.hands.index(hand)] = max(card.rank for card in hand)
                
        print("Your best hand is: ")
        print((self.printHand(self.hands[self.tlist.index(max(self.tlist))])))
        print("and has {} points".format(max(self.tlist)))
        

deck1 = Deck()
deck1.shuffle()
pkr = Poker(4)
pkr.game()
