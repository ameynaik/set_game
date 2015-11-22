# Copyright (c) 2015 Amey Naik
#!/usr/bin/python
# function name : card_generator.py
# The function gives out list of 81 possible combinations of cards in form of 4-tuples.
# (Shape,Color,Number,Pattern)
# Shape can be Rectangular-1, Oval-2, Diamond-3
# Color can be Red-1, Green-2, Blue-3
# Number can be 1, 2, 3
# Pattern can be Solid-1, Hatched-2, Outlined-3 

# This function doesn't have any inputs.

import sys
from Tkinter import *
from Tkinter import Tk, Canvas, Frame, BOTH
from PIL import ImageGrab
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

def card_image_generator(cards):
	#fig3 = plt.figure()
	#ax3 = fig3.add_subplot(111, aspect='equal')
	#p = patches.Rectangle((0.1, 0.1), 0.8, 0.5,facecolor='none')
	#plotcard(1,1,1,1)
	#p2 = patches.Ellipse((0.3, 0.35), 0.1, 0.3,hatch='\\',fill=True,edgecolor = "red")
	#p3 = patches.Rectangle((0.45, 0.2), 0.1, 0.3,hatch='\\',fill=True)
	#p4 = patches.Polygon([[0.7, 0.2], [0.65, 0.35], [0.7, 0.5], [0.75, 0.35]], closed=True,hatch='\\',fill=True)
	#ax3.add_patch(p1)
	#ax3.add_patch(p2)
	#plt.show()
	#savename = 'test'
	#ImageGrab.grab((538,365,845,557)).save(savename + '.jpg')
     for card in cards:
		plotcard(cards[card][0],cards[card][1],cards[card][2],cards[card][3])
		savename = 'test'+str(cards[card][0])+str(cards[card][1])+str(cards[card][2])+str(cards[card][3])
		ImageGrab.grab((538,365,845,557)).save(savename + '.jpg')	
		

    
def plotcard(shape,color,number,pattern):
	shape_enum = {1:'rect', 2:'oval', 3:'diam'}
	color_enum = {1:'red', 2:'green', 3:'blue'}
	number_enum = {1:1, 2:2, 3:3}
	pattern_enum = {1:'solid', 2:'', 3:'outlined'} #stipple
    
	col =color_enum[color]
	
	if pattern == 1:
		fill_param = True
		hatch_param = ''
	elif pattern == 2:
		fill_param = False
		hatch_param = '///'
	else:
		fill_param = False
		hatch_param = ''
    
	fig3 = plt.figure()
	ax3 = fig3.add_subplot(111, aspect='equal')
	p = patches.Rectangle((0.1, 0.1), 0.8, 0.5,facecolor='none')
	ax3.add_patch(p)
	if shape_enum[shape] == 'rect':
		if number == 3:
			p1 = patches.Rectangle((0.25, 0.2), 0.1, 0.3,hatch=hatch_param,fill=fill_param,edgecolor = col,color=col,lw=2)
			ax3.add_patch(p1)
		if number == 1 or number == 3:
			p2 = patches.Rectangle((0.45, 0.2), 0.1, 0.3,hatch=hatch_param,fill=fill_param,edgecolor = col,color=col,lw=2)
			ax3.add_patch(p2)
		if number == 3:
			p3 = patches.Rectangle((0.65, 0.2), 0.1, 0.3,hatch=hatch_param,fill=fill_param,edgecolor = col,color=col,lw=2)
			ax3.add_patch(p3)
		if number == 2:
			p1 = patches.Rectangle((0.35, 0.2), 0.1, 0.3,hatch=hatch_param,fill=fill_param,edgecolor = col,color=col,lw=2)
			ax3.add_patch(p1)
			p2 = patches.Rectangle((0.55, 0.2), 0.1, 0.3,hatch=hatch_param,fill=fill_param,edgecolor = col,color=col,lw=2)
			ax3.add_patch(p2)
	elif shape_enum[shape] == 'oval':
		if number == 3:
			p1 = patches.Ellipse((0.3, 0.35), 0.1, 0.3,hatch=hatch_param,fill=fill_param,edgecolor = col,color = col,lw=2)
			ax3.add_patch(p1)
		if number == 1 or number == 3:
			p2 = patches.Ellipse((0.5, 0.35), 0.1, 0.3,hatch=hatch_param,fill=fill_param,edgecolor = col,color = col,lw=2)
			ax3.add_patch(p2)
		if number == 3:
			p3 = patches.Ellipse((0.7, 0.35), 0.1, 0.3,hatch=hatch_param,fill=fill_param,edgecolor = col,color = col,lw=2)
			ax3.add_patch(p3)
		if number == 2:
			p1 = patches.Ellipse((0.4, 0.35), 0.1, 0.3,hatch=hatch_param,fill=fill_param,edgecolor = col,color = col,lw=2)
			ax3.add_patch(p1)
			p2 = patches.Ellipse((0.6, 0.35), 0.1, 0.3,hatch=hatch_param,fill=fill_param,edgecolor = col,color = col,lw=2)
			ax3.add_patch(p2)
	else:
		
		if number == 3:
			p1 = patches.Polygon([[0.3, 0.2], [0.25, 0.35], [0.3, 0.5], [0.35, 0.35]], closed=True,hatch=hatch_param,fill=fill_param,color=col,edgecolor=col,lw=2)
			ax3.add_patch(p1)
		if number == 1 or number == 3:
			p2 = patches.Polygon([[0.5, 0.2], [0.45, 0.35], [0.5, 0.5], [0.55, 0.35]], closed=True,hatch=hatch_param,fill=fill_param,color=col,edgecolor=col,lw=2)
			ax3.add_patch(p2)
		if number == 3:
			p3 = patches.Polygon([[0.7, 0.2], [0.65, 0.35], [0.7, 0.5], [0.75, 0.35]], closed=True,hatch=hatch_param,fill=fill_param,color=col,edgecolor=col,lw=2)
			ax3.add_patch(p3)
		if number == 2:
			p1 = patches.Polygon([[0.4, 0.2], [0.35, 0.35], [0.4, 0.5], [0.45, 0.35]], closed=True,hatch=hatch_param,fill=fill_param,color=col,edgecolor=col,lw=2)
			ax3.add_patch(p1)
			p2 = patches.Polygon([[0.6, 0.2], [0.55, 0.35], [0.6, 0.5], [0.65, 0.35]], closed=True,hatch=hatch_param,fill=fill_param,color=col,edgecolor=col,lw=2)
			ax3.add_patch(p2)
	
	
	plt.show()
	
	
def main():
    card = card_list()
    card_image_generator(card)
	
if __name__ == '__main__':
    main()