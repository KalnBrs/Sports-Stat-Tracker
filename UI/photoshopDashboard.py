import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox
import ttkbootstrap as ttk
from collections import deque
from Data.game import gameData
from Methods.functions import *
from Methods.photoFunct import *
from Methods.statObj import *


class dashboard(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Dashboard")
    self.geometry("500x500")
    self.minsize(300, 300)
    self.label_intro = ttk.Label(self, text="Paste Path to Graphic: ").pack()
    self.pathEntry = ttk.Entry(self)
    self.pathEntry.pack()

    dataOptions = loadOptions()

    dropDownFrame = ttk.Frame(self)
    dropDownFrame.columnconfigure(0, weight=1)
    dropDownFrame.columnconfigure(1, weight=1)
    dropDownFrame.columnconfigure(2, weight=1)
    dropDownFrame.columnconfigure(3, weight=1)


    # Allows you to change the text showing on the drop down
    self.homeLeft = StringVar()
    self.homeLeft.set("None")

    self.homeRight = StringVar()
    self.homeRight.set("None")

    self.awayLeft = StringVar()
    self.awayLeft.set("None")

    self.awayRight = StringVar()
    self.awayRight.set("None")
    
    homeLeftLabel = ttk.Label(dropDownFrame, text="Home Left: ").grid(row=0, column=0)
    statPickMenu1 = OptionMenu(dropDownFrame, self.homeLeft, *dataOptions["statPick"])
    statPickMenu1.grid(row=1, column=0)

    homeLeftLabel = ttk.Label(dropDownFrame, text="Home Right: ").grid(row=0, column=1)
    statPickMenu2 = OptionMenu(dropDownFrame, self.homeRight, *dataOptions["statPick"])
    statPickMenu2.grid(row=1, column=1)

    homeLeftLabel = ttk.Label(dropDownFrame, text="Away Left: ").grid(row=0, column=2)
    statPickMenu3 = OptionMenu(dropDownFrame, self.awayLeft, *dataOptions["statPick"])
    statPickMenu3.grid(row=1, column=2)

    homeLeftLabel = ttk.Label(dropDownFrame, text="Away Right: ").grid(row=0, column=3)
    statPickMenu4 = OptionMenu(dropDownFrame, self.awayRight, *dataOptions["statPick"])
    statPickMenu4.grid(row=1, column=3)

    dropDownFrame.pack(fill="x", pady=10)

    # To check if value is stored
    try: 
      a = gameData.homeColor
    except AttributeError:
      gameData.homeColor = "#435058"

    try: 
      b = gameData.awayColor
    except AttributeError:
      gameData.awayColor = "#435058"


    style = ttk.Style()
    style.configure("HomeShip.TButton", background=gameData.homeColor)
    style.configure("AwayShip.TButton", background=gameData.awayColor)

    shipFrame = ttk.Frame(self)
    shipFrame.columnconfigure(0, weight=1)
    shipFrame.columnconfigure(1, weight=1)

    # Example of the choices
    self.homeStringUpdateLeft = StringVar()
    self.homeStringUpdateRight = StringVar()
    self.awayStringUpdateLeft = StringVar()
    self.awayStringUpdateRight = StringVar()

    self.expHome = ttk.Label(shipFrame, text="None")
    self.expHome.grid(row=0, column=0)
    self.expAway = ttk.Label(shipFrame, text="None")
    self.expAway.grid(row=0, column=1)

    homeShipButton = ttk.Button(shipFrame, style="HomeShip.TButton", text="Send To Photoshop", command=lambda: shipHome(self.homeLeft.get(), self.homeRight.get()))
    homeShipButton.grid(row=1, column=0)

    awayShipButton = ttk.Button(shipFrame, style="AwayShip.TButton", text="Send To Photoshop", command=lambda: shipAway(self.awayLeft.get(), self.awayRight.get()))
    awayShipButton.grid(row=1, column=1)

    homeTimeButton = ttk.Button(shipFrame, style="HomeShip.TButton", text="Timeout", command=lambda: updateTimeHome())
    homeTimeButton.grid(row=2, column=0)

    awayTimeButton = ttk.Button(shipFrame, style="AwayShip.TButton", text="Timeout", command=lambda: updateTimeAway())
    awayTimeButton.grid(row=2, column=1)

    shipFrame.pack(fill="x", pady=10)

    self.Away = Stats("away")
    self.Home = Stats("home")

    self.renderExamples()

  def renderExamples(self):
    dataOptions = loadOptions()

    # Home Left 
    homeLeftStatID = dataOptions["statPick"][self.homeLeft.get()]
    self.homeStringUpdateLeft.set(self.Home.getValueOfStat(homeLeftStatID))
    # Home Right
    homeRightStatID = dataOptions["statPick"][self.homeRight.get()]
    self.homeStringUpdateRight.set(self.Home.getValueOfStat(homeRightStatID))
    self.expHome.config(text=self.homeStringUpdateLeft.get() + " - " + self.homeLeft.get() + "   " + self.homeStringUpdateRight.get() + " - " + self.homeRight.get())

    # Home Left 
    awayLeftStatID = dataOptions["statPick"][self.awayLeft.get()]
    self.awayStringUpdateLeft.set(self.Away.getValueOfStat(awayLeftStatID))
    # Home Right
    awayRightStatID = dataOptions["statPick"][self.awayRight.get()]
    self.awayStringUpdateRight.set(self.Away.getValueOfStat(awayRightStatID))
    self.expAway.config(text=self.awayStringUpdateLeft.get() + " - " + self.awayLeft.get() + "   " + self.awayStringUpdateRight.get() + " - " + self.awayRight.get())

    self.after(300, self.renderExamples)
    