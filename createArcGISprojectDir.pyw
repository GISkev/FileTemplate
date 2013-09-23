#myWXfromScratch.py
#my first wx GUI on my own.
#DATE: 11-29-2006
#AUTHOR: Kevin Bell

#Cool Additions:
#   - make the combobox reorder itself based on a pickled dictionary

import wx, sys, os, shutil, time, arcpy

class myTestApp(wx.Frame):
	
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "Create Project Directory", size=(300,250))
		panel = wx.Panel(self, -1)
		
		myProjectLabel = wx.StaticText(panel, -1, "Project Name: ", pos=(10,10))
		self.tc = wx.TextCtrl(panel, -1, "Enter a project name here", size=(175,-1), pos=(90,10))
		
		path = ("E:\\gis")
		l=os.listdir(path)
		myChoices = [x for x in l if os.path.isdir(os.path.join(path, x))]
		
		myChoiceLabel = wx.StaticText(panel, -1, "Who's it for? ", pos=(10,50))
		self.myChoice = wx.Choice(panel, -1, pos=(90,50), choices=myChoices)
		self.Bind(wx.EVT_CHOICE, self.OnChoose, self.myChoice)
		
		self.requestee = None 
	
		self.myChk= wx.CheckBox(panel, -1, "Open the directory?", pos=(90,90), size=wx.DefaultSize, name="chkOpenDir")
		self.myChk.SetValue(True)
		
		self.myChk2= wx.CheckBox(panel, -1, "Open the MXD?", pos=(90,130), size=wx.DefaultSize, name="chkOpenMap")
		self.myChk2.SetValue(True)
		
		self.button =  wx.Button(panel, -1, "BUILD THE PROJECT", pos=(90, 160))
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
		
		
	def OnChoose(self, event):
		self.requestee = event.GetString()
	
	def OnClick(self, event):
		#self.button.SetLabel("clicked")
		requestee = self.requestee
		projectName = self.tc.GetValue()
		today = time.strftime("%Y%m%d")
		prjnamedate = str(today) + "_" + projectName
		
		os.makedirs("E:\\gis" + "\\" + requestee + "\\" + prjnamedate)
		os.makedirs("E:\\gis" + "\\" + requestee + "\\" + prjnamedate + "\\Temp")
		os.makedirs("E:\\gis" + "\\" + requestee + "\\" + prjnamedate + "\\FinalData")
		os.makedirs("E:\\gis" + "\\" + requestee + "\\" + prjnamedate + "\\OriginalData")
		txtfile = file("E:\\gis" + "\\" + requestee + "\\" + prjnamedate + "\\notes.txt", "wt")
		
		
		#copy a basemap as a new map named date_projectName
		newMxd = "E:\\gis" + "\\" + requestee + "\\" + prjnamedate + "\\" + prjnamedate + ".mxd"
		shutil.copyfile ("G:\\gisProject" + "\\000.mxd", newMxd)
		#open the new map
		if self.myChk2.GetValue() == True:
			os.startfile("E:\\gis" + "\\" + requestee + "\\" + prjnamedate + "\\" + prjnamedate + ".mxd")
		if self.myChk.GetValue() == True:
			os.startfile("E:\\gis" + "\\" + requestee + "\\" + prjnamedate)
			
		arcpy.CreateFileGDB_management("E:\\gis" + "\\" + requestee + "\\" + prjnamedate, 'default.gdb')
		
		#close app here
		wx.Exit()

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = myTestApp()
	frame.Center(direction=wx.BOTH)
	frame.Show()
	app.MainLoop()
	
