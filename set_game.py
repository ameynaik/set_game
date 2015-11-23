# Copyright AN. November 2015
#!/usr/local/bin/python

import Tkinter as tk
import Tkinter as Tkinter
from Tkinter import Frame, Label, Button
from PIL import Image, ImageTk
import card_functions

def reset_buttons(bf,set_selected,found):
    bf = [True,True,True,True,True,True,True,True,True,True,True,True]
    for i in set_selected:
		if found == 1:
			button[i].config(bg="green")
		else:
			button[i].config(bg="red")
    return bf
		
def color_white(card_sel):
	for i in card_sel:
		button[i].config(bg="white")
		
def click(count):
    global bf
    global set_found
    global sets_backup
    global b1
    global b2
    global b3
    global b4
    global win
	
    if (win == 1):
		root.quit()
    
    if bf[count-1]:
        button[count].config(bg="gray1")
        bf[count-1] = False
    else:
        button[count].config(bg="white")
        bf[count-1] = True
    if sum(bf) == 11:
		card_sel = [i for i, x in enumerate(bf) if x == True]
		card_sel = [x+1 for x in card_sel]
		color_white(card_sel)
			
    if sum(bf) == 12:
		b4.config(text="Select 3 cards")
    if sum(bf) == 11:
		b4.config(text="Select 2 more cards")
    if sum(bf) == 10:
		b4.config(text="Select 1 more cards")	
		
    if sum(bf)==9:
		# call a function to check if its a set
		(bf,set_indicator) = is_it_set(bf)
		if set_indicator[1]:
			set_found = set_found + 1 
			b4.config(text="You got it!")
			b3.config(text="The sets you have found so far are: " + str(set_found) + " which are : " + str(found_sets))
			if (len(sets_backup) == 0):
				b1.config(text="SET GAME- YOU WON!!!",font="Helvetica 10 bold",foreground="lime green",bg = "yellow")
				win = 1;
				
				#start_game()
			
		else:
			b4.config(text="Andhe ho kya?")
			
		


def is_it_set(bf):
	global sets
	set_selected = [i for i, x in enumerate(bf) if x == False]
	set_selected = [x+1 for x in set_selected]
	
	for s in sets:
		if set(list(sets[s])) == set(set_selected):
			found_sets[s] = sets[s]
			del sets[s]
			found = 1# return the set that was found
			bf = reset_buttons(bf,set_selected,found)# Reset all the buttons (function)
			return (bf,set_selected)
			# Delete the set which was found from the list.
		else:
			found = 0
	if found == 1:
		return (bf,set_selected)
	else:
		bf = reset_buttons(bf,set_selected,found)# Reset all the buttons (function)
		return (bf,[0,0,0])
		
		
			

def gen_card_file_name(card):
	file_str = 'cards/test'+str(card[0])+str(card[1])+str(card[2])+str(card[3])+'.jpg'
	pil_image = Image.open(file_str)
	image = ImageTk.PhotoImage(pil_image)
	return image

def start_game():
	global sets
	global bf
	global set_found
	global b1
	global b2
	global b3
	global b4
	global sets_backup
	global root
	set_found = 0;
	bf = [True,True,True,True,True,True,True,True,True,True,True,True]

	
	# create and pack containers
	top = Tkinter.Frame(root, background="dark slate gray")
	top.pack(fill="x")
	b1 = Tkinter.Label(top, text="SET GAME",font="Helvetica 10 bold",foreground="SystemHighlight")
	b1.pack(side="top", expand="yes", fill="x", padx=3, pady=3)
	b4 = Tkinter.Label(top, text="Please select 3 cards ",font="Helvetica 8")
	b4.pack(side="left", expand="yes", fill="x", padx=3, pady=3)
	b3 = Tkinter.Label(top, text="The sets you have found so far are: None",font="Helvetica 8")
	b3.pack(side="left", expand="yes", fill="x", padx=3, pady=3)

	bottom = Tkinter.Frame(root, background="cornsilk")
	bottom.pack(expand="yes", fill="both")

	# Get 12 random cards

	# create pil images function and put it in a for loop of 12.
	cards = card_functions.card_list()
	r12_cards = card_functions.rand_12_cards_generator(cards)
	sets = card_functions.find_sets(r12_cards)
	sets_backup = sets
	found_sets = {}
	print sets_backup

	b2 = Tkinter.Label(top, text="There are " + str(len(sets)) + " sets in this pack of cards",font="Helvetica 8")
	b2.pack(side="left", expand="yes", fill="x", padx=3, pady=3)
	images = {}
	for i in range(1,13):
		images[i] = gen_card_file_name(r12_cards[i])
	 
	count = 1;

	 
	# use grid on the bottom
	for x in range(3):
		for y in range(4):
			button[count] = tk.Button(bottom, compound=tk.TOP,relief = "raised",state = "normal", image=images[count], text=count, bg='white',font="Helvetica 10 bold italic")
			button[count].pack(side=tk.LEFT, padx=2, pady=2)
			button[count].image = images[count]
			button[count].grid(row=x, column=y, sticky="news", padx=2, pady=2)
			count = count + 1;

	button[1].config(command=lambda: click(1))
	button[2].config(command=lambda: click(2))
	button[3].config(command=lambda: click(3))
	button[4].config(command=lambda: click(4))		

	button[5].config(command=lambda: click(5))
	button[6].config(command=lambda: click(6))
	button[7].config(command=lambda: click(7))
	button[8].config(command=lambda: click(8))

	button[9].config(command=lambda: click(9))
	button[10].config(command=lambda: click(10))
	button[11].config(command=lambda: click(11))
	button[12].config(command=lambda: click(12))

	for i in range(4):
		bottom.columnconfigure(i, weight=1)
		bottom.rowconfigure(i, weight=1)


root = Tkinter.Tk()
bf = [True,True,True,True,True,True,True,True,True,True,True,True]
	# create and pack containers
top = Tkinter.Frame(root, background="dark slate gray")
top.pack(fill="x")
b1 = Tkinter.Label(top, text="SET GAME",font="Helvetica 10 bold",foreground="SystemHighlight")
b4 = Tkinter.Label(top, text="Please select 3 cards ",font="Helvetica 8")
b3 = Tkinter.Label(top, text="The sets you have found so far are: None",font="Helvetica 8")

	
#cards = card_functions.card_list()
#r12_cards = card_functions.rand_12_cards_generator(cards)
sets = {}
sets_backup = sets
found_sets = {}
print sets_backup
button=  [0 for x in xrange(13)]
win = 0;
start_game()		
root.mainloop()