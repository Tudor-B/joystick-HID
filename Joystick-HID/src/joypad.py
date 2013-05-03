#!/usr/bin/python
# Project Network - Logitech G27 / Xbox 360 controller and others

import os
import pygame 

import sys		# Imports pygame library that are made for developing games
if os.name == 'nt':
	from WinMouseInterface import MouseInterface
	from WinKBInterface import KBInterface
	pass
elif os.name == 'posix':
	from LinMouseInterface import MouseInterface
	from LinKBInterface import KBInterface
	pass

pygame.init()			# Starts pygame
t = pygame.time.Clock()		# Make a tracker
keyboard = KBInterface()
mouse = MouseInterface()

# TODO: change the default value to something dynamic
os.system('cls' if os.name=='nt' else 'clear')# Clear terminal // remove "there is no soundcard"
try: 
	
	print "Number of Devices:", pygame.joystick.get_count()
	d = pygame.joystick.Joystick(0)
	d.init()			# Start pygame.joystick.Joystick(0)
	

# Gives info about the device
	print "Connected device", d.get_name()
	print d.get_name(), "have"
	print "Buttons:", d.get_numbuttons()
	print "Axes:", d.get_numaxes()
	print "Hats:", d.get_numhats()
	print "Balls:", d.get_numballs()
	print "The device ID is", d.get_id()
	print "Press button 0 to exit"
	
# Start showing the info in terminal

	def loop():
		global d, t

		while pygame.event.get(pygame.QUIT) == []:
			xy =pygame.event.get(pygame.JOYAXISMOTION)
			#xy_True=[] # call the infomation to
		# Axes Part
			if xy != []:
				xy_data = []
				for c in range(0, d.get_numaxes()):
					xy_data+= [str(round(d.get_axis(c),1))]
					if int(float(xy_data[0])) == 1:
						mouse.MovementRight()
						
					elif int(float(xy_data[0])) == -1:
						mouse.MovementLeft()
#				
# 					elif int(float(xy_data[1])) == 1:
#  						mouse.MovementDown()
# 					elif int(float(xy_data[1])) == -1:
# 						mouse.MovementUp()
#					
# 					if int(float(xy_data[1])) == -1:
# 						mouse.MovementUp()
# 					print x,y
# 					print int(float(xy_data[0]))
#					#xy_True+= [int(xy_data)]
#     					if xy_data[0] == "1.0":
#     						x=x+1
#     					if xy_data[0] == "-1.0":
#     						x=x-1
					#if xy_data[1] == "1.0":
					#	y=y+1
					#if xy_data[1] == "-1.0":
					#	y=y-1
#				
# 				mouse.SetPosition( x, y )
#				print "Works?"
#				print xy_data
				
			
			# Button Part Down
			downbutton = pygame.event.get(pygame.JOYBUTTONDOWN)
			for button in downbutton:
#				print "Pressed button is", button.button
				if button.button == 0:			# The exit button
					return
				elif button.button == 2:
					mouse.ClickLeft()
				elif button.button == 3:
					mouse.ClickRight()
				elif button.button == 4:
					keyboard.KeyUp_Down()
				elif button.button == 5:
					keyboard.KeyRight_Down()
				elif button.button == 6:
					keyboard.KeyDown_Down()
				elif button.button == 7:
					keyboard.KeyLeft_Down()
			
#				print (pygame.mouse.get_pos())
		
		# Button Part Up
			upbutton = pygame.event.get(pygame.JOYBUTTONUP)
			for button in upbutton:
#				print "Button released was", button.button
				if button.button == 4:
					keyboard.KeyUp_Up()
				elif button.button == 5:
					keyboard.KeyRight_Up()
				elif button.button == 6:
					keyboard.KeyDown_Up()
				elif button.button == 7:
					keyboard.KeyLeft_Up()
			
			t.tick(80)
	loop()

except Exception, e:
	print "Unhandled exception: %s"%e
	print "Shutting down now"