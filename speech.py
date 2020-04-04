import wolframalpha as wa
import wikipedia as wiki
import wx
import speech_recognition as sr
from gtts import gTTS

app_id = "YRRQ8V-P93VL22LR2"   #wolframalpha_api_id

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(600, 400),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Assitant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Assitant the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        bmp = wx.Bitmap("robo.BMP", wx.BITMAP_TYPE_BMP)
        self.bmpbtn = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp, size=(bmp.GetWidth() + 40, bmp.GetHeight() + 40))

        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))

        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        inp = self.txt.GetValue()
        inp = inp.lower()
        if inp == '':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        try:
            # wolframalpha

            client = wa.Client(app_id)
            res = client.query(inp)
            answer = next(res.results).text
            print(answer)

        except:
            print(wiki.summary(inp))


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
