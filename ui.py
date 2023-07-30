import wx
import wx.lib.intctrl as wxint
from random import randint

# TODO add more choices for other games
# TODO create selection that shows specific panels.

class DicePanel(wx.Panel):
  def __init__(self, parent):
    super().__init__(parent)
    header_font = wx.Font(wx.FontInfo(18).Family(wx.FONTFAMILY_ROMAN).Italic().Underlined())
    header2_font = wx.Font(wx.FontInfo(16).Family(wx.FONTFAMILY_ROMAN).Italic())
    # sizers
    sizer = wx.BoxSizer(wx.VERTICAL)
    # horizontal sizers
    hs = wx.BoxSizer(wx.HORIZONTAL)
    hs2 = wx.BoxSizer(wx.HORIZONTAL)
    hs3 = wx.BoxSizer(wx.HORIZONTAL)
    hs4 = wx.BoxSizer(wx.HORIZONTAL)
    # title
    self.title_header = wx.StaticText(self, label="Dice Roller")
    self.title_header.SetFont(header_font)
    sizer.Add(self.title_header, 0, wx.ALL | wx.CENTER, 5)

    # roll d20
    self.d20_header = wx.StaticText(self, label="Roll a D20")
    self.d20_header.SetFont(header2_font)
    sizer.Add(self.d20_header, 0, wx.ALL, 5)
    # checkbox buttons adv, dis (only one can be checked)
    self.advantage = wx.CheckBox(self, label="Advantage")
    hs.Add(self.advantage, 0, wx.ALL | wx.ALIGN_CENTER, 5)
    self.disadvantage = wx.CheckBox(self, label="Disadvantage")
    hs.Add(self.disadvantage, 0, wx.ALL | wx.ALIGN_CENTER, 5)
    sizer.Add(hs, 0, wx.ALL, 5)
    d20_btn = wx.Button(self, label="Roll Dice!")
    d20_btn.Bind(wx.EVT_BUTTON, self.roll_d20)
    hs3.Add(d20_btn, 0, wx.ALL | wx.ALIGN_LEFT, 5)
    # display d20 result
    self.d20_result = wx.StaticText(self, label=f"")
    hs3.Add(self.d20_result, 0, wx.ALL | wx.CENTER, 5)
    sizer.Add(hs3, 0, wx.ALL, 5)
   
    # roll other dice
    self.dice_header = wx.StaticText(self, label="Roll Other Dice")
    self.dice_header.SetFont(header2_font)
    sizer.Add(self.dice_header, 0, wx.ALL, 5)
    self.dice_face = wx.RadioBox(self, label="Choose Your Dice!", choices=["d4", "d6", "d8", "d10", "d12", "d100"])
    sizer.Add(self.dice_face, 0, wx.ALL | wx.EXPAND, 5)
    # amount entry
    self.amount_label = wx.StaticText(self, label="How many dice are you rolling?")
    hs2.Add(self.amount_label, 0, wx.ALL | wx.EXPAND, 5)
    self.dice_amount = wxint.IntCtrl(self, size=(50, 20))
    hs2.Add(self.dice_amount, 0, wx.ALL | wx.ALIGN_LEFT, 5)
    sizer.Add(hs2, 0, wx.ALL, 5)

    # roll button
    btn = wx.Button(self, label="Roll Dice!")
    btn.Bind(wx.EVT_BUTTON, self.roll_dice)
    hs4.Add(btn, 0, wx.ALL | wx.ALIGN_LEFT, 5)

    # display total
    self.total_text = wx.StaticText(self, label=f"")
    hs4.Add(self.total_text, 0, wx.ALL | wx.CENTER, 5)
    sizer.Add(hs4, 0, wx.ALL, 5)
    self.SetSizer(sizer)
    self.Show()


# Controllers
  def roll_dice(self, event):
    face = self.dice_face.GetString(self.dice_face.GetSelection())
    face_value = int(face.replace('d', ''))
    amount = int(self.dice_amount.GetValue())

    total = 0
    random_num = []
    i = 0
    while i < amount:
      number = randint(1, face_value)
      random_num.append(number)
      i+= 1

    for num in random_num: 
      total += num   
    self.total_text.SetLabel(f"You rolled {amount} {face} for a total of {total}!")

    self.dice_amount.SetValue(0)


  def roll_d20(self, event):
    if self.advantage.IsChecked() == True and self.disadvantage.IsChecked() == True:
      self.d20_result.SetLabel("Check only one box.")
      self.advantage.SetValue(False)
      self.disadvantage.SetValue(False)
      return
    elif self.advantage.IsChecked() == True:
      roll1 = randint(1, 20)
      roll2 = randint(1, 20)
      self.d20_result.SetLabel(f"You rolled a {roll1} and {roll2}. Your best roll was a {max(roll1, roll2)}!")
    elif self.disadvantage.IsChecked() == True:
      roll1 = randint(1, 20)
      roll2 = randint(1, 20)
      self.d20_result.SetLabel(f"You rolled a {roll1} and {roll2}. Your worst roll was a {min(roll1, roll2)}!")
    else:
      roll = randint(1, 20)
      self.d20_result.SetLabel(f"You rolled a {roll}!") 

    self.advantage.SetValue(False)
    self.disadvantage.SetValue(False)
 
 
class DiceFrame(wx.Frame):
  def __init__(self):
    super().__init__(parent=None, title="Dice Roller", size=(360,640))
    self.Panel = DicePanel(self)
    ICON_PATH = r"C:\Users\Carl\Desktop\Python\diceroller\Twenty_sided_dice.ico"
    self.SetIcon(wx.Icon(ICON_PATH, wx.BITMAP_TYPE_ICO))
    self.Show()
    self.Centre()

if __name__ == '__main__':
  app = wx.App()   
  frame = DiceFrame() 
  app.MainLoop()