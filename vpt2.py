"""
Virtual Page Turner, a program to help musicians view and turn pages using a computer.

    Copyright (C) 2008  Michael Toth

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import wx
import wx.lib.dialogs
import os
import string
import re
import sys
import traceback
import wx.html
import commands
from program import *


class vptFrame(wx.Frame):
    """ 
    Top Level Frame for Virtual Page Turner

    Inherits from wx.Frame, 
    Sets screen size to be display size.
    Uses the file "Welcome.gif" as the initial page image.
    Creates menus and binds menu items.
    Creates status bar. 
    Sets options to their initial default values.
    (To Do: Allow for options to be saved and restored when running again)
    page1 is the current page
    page2 is the next page

    """

    def __init__(self, parent=None, id=-1, pos=wx.DefaultPosition, title='Virtual Page Turner'):
        self.version = "1.0"
        self.priorSelection = None
        self.title = "Virtual Page Turner 2"
        print 'pos is ' + str(pos)
        self.screenSize = wx.Size(425,550)
        wx.Frame.__init__(self,None,id,title,pos,size=self.screenSize)

        # set up the menus
        self.setupMenus()

    def selectPiece(self):
        self.directoryDialog = wx.DirDialog( None, style = wx.OPEN, message = 'Select Piece to Load' )
        if self.directoryDialog.ShowModal() == wx.ID_OK:
            self.priorSelection = self.directoryDialog.GetPath()
        print 'piece selected is ' + self.directoryDialog.GetPath()
        return self.priorSelection

    def setupMenus(self):
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        menuBar.Append(menu,'&File')
        self.SetMenuBar(menuBar)
        
        
def main():
    app = wx.App(False)
    frame = vptFrame()
        
    frame.Show(True)
        
    app.MainLoop()    

if __name__ == '__main__':
    main()
