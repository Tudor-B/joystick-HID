'''
Created on May 1, 2013

@author: Tudor
'''

import win32api, win32con

class MouseInterface(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def SetPosition(self, x, y):
        win32api.SetCursorPos((x, y))
        
    def GetPosition(self):
        return win32api.GetCursorPos()
    
    def ClickLeft(self):
        #     def Lclick(x, y):
        x, y = self.GetPosition()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x, y)
         
    def ClickRight(self):
        x, y = self.GetPosition()
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x, y)
        
    def MovementUp(self):
        x, y = self.GetPosition()
        y = y-1
        self.SetPosition(x, y)
        
    def MovementDown(self):
        x, y = self.GetPosition()  
        y= y+1
        self.SetPosition(x, y)
        
    def MovementLeft(self):
        x, y = self.GetPosition()
        x = x-1
        self.SetPosition(x, y)
        
    def MovementRight(self):
        x, y = self.GetPosition()
        x = x+1
        self.SetPosition(x, y)