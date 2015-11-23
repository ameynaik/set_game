#!/usr/bin/python
# function name : card_functions.py
# 12 random cards spawner
# Find set combinations in those 12 cards.

# 81 possible combinations of cards in form of 4-tuples.
# (Shape,Color,Number,Pattern)
# Shape can be Rectangular-1, Oval-2, Diamond-3
# Color can be Red-1, Green-2, Blue-3
# Number can be 1, 2, 3
# Pattern can be Solid-1, Hatched-2, Outlined-3 

# This function doesn't have any inputs.

from Tkinter import *
from Tkinter import Tk, Canvas, Frame, BOTH
import itertools
import random

# Gather our code in a main() function
def card_list():

    shape = {'rect':1, 'oval':2, 'diam':3}
    color = {'red':1, 'green':2, 'blue':3}
    number = {'one':1, 'two':2, 'three':3}
    pattern = {'solid':1, 'hatch':2, 'outlined':3}
    card = {}; i = 1;
    for s_v in sorted(shape.values()):
		for c_v in sorted(color.values()):
			for n_v in sorted(number.values()):
				for p_v in sorted(pattern.values()):
					card[i] = (s_v,c_v,n_v,p_v)
					i = i + 1;
					
    return card
	
def rand_12_cards_generator(card):
	#print card[81]
	r12_list = random.sample(range(1, 81), 12)
	r12_cards = {}; i = 1;
	for r in r12_list:
		r12_cards[i] = card[r]
		i = i + 1
	
	#print r12_cards
	return r12_cards

def find_sets(r12_cards):
	# Generate 12C3 = 220 combinations for numbers from 1 to 12.
	print r12_cards
	a = range(1,13) # creates a list of numbers from 1 to 12
	comb = list(itertools.combinations(a,3))
	count = 1;
	sets = {}
	setscard = {}
	#print r12_cards[int(comb[0][0])]
	for c in comb:
		set = is_it_set(r12_cards[c[0]], r12_cards[c[1]], r12_cards[c[2]])
		if set == 1:
			sets[count] = (r12_cards[c[0]], r12_cards[c[1]], r12_cards[c[2]])
			setscard[count] = (c[0],c[1],c[2])
			count = count + 1
	return setscard
	#return sets	
		
		
	#return r12_cards
def is_it_set(card1,card2,card3):
	shape_list = [card1[0],card2[0],card3[0]]
	color_list = [card1[1],card2[1],card3[1]]
	numb_list = [card1[2],card2[2],card3[2]]
	patt_list = [card1[3],card2[3],card3[3]]
	
	if ((len(shape_list) == len(set(shape_list)) or len(set(shape_list)) == 1) and (len(color_list) == len(set(color_list)) or len(set(color_list)) == 1) and (len(patt_list) == len(set(patt_list)) or len(set(patt_list)) == 1) and (len(numb_list) == len(set(numb_list)) or len(set(numb_list)) == 1)):
		return 1
	else:
		return 0
	
	

def main():
    cards = card_list()
    r12_cards = rand_12_cards_generator(cards)
    sets = find_sets(r12_cards)
    
    
	
if __name__ == '__main__':
    main()