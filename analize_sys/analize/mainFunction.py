import warnings, logging, sys
import matplotlib.pyplot as plt
from DataCollect import DataCollect
from DataAnalyse import ForcastData
from tkinter import *


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CommonEntry():
    def __init__(self, window = None):
        self.ent = Entry(window);

    def Return(self):
        self.ent.pack(side = RIGHT, expand = YES, fill =X);
        return self.ent;

        
class ExecuteButton():
    def __init__(self, frame, entries, Text = "Print"):
        self.button = Button(frame, text = Text);
        self.entries = entries;
        self.result = [];
        
    def Fetch(self):
        for (field, entry) in self.entries:
            String = entry.get();
            if(String != ""):
                print("%s => '%s'" % (field, String));
                entry.delete(0,END);
                self.result.append(String);
        print (self.result);
        FileName = self.result[0];
        testMode = int(self.result[1]);
        try:
            se = DataCollect(FileName).CollectData();
        except:
            print("FileName is wrong!");
        right, wrong, datatype = ForcastData(se, testMode, 5).ForcastData();
        print ("right:", right);
        print ("wrong:", wrong);
        print ("涨跌:", datatype);

    def Return(self):
        self.button.config(command = self.Fetch);
        return self.button;
    

class ExitButton():
    def __init__(self, frame, window, Text = "Exit"):
        self.button = Button(frame, text = Text);
        self.window = window;

    def exit(self):
        self.window.quit();
        self.window.destroy();

    def Return(self):
        self.button.config(command = self.exit);
        return self.button;


class MakeForm():
    def __init__(self, window, fields):
        self.window = window;
        self.fields = fields;
        self.frame = Frame(self.window);
        self.frame.pack(side = TOP, fill = X);
        self.entries = [];

    def makeSingleform(self, field):
        Smallframe = Frame(self.frame);
        Smallframe.pack(side = TOP, fill = X);
        label = Label(Smallframe, width =10, text =field);
        label.pack(side = LEFT);
        ent = CommonEntry(Smallframe).Return();
        return ent;


    def SetForms(self):
        for field in self.fields:
            ent = self.makeSingleform(field);
            self.entries.append((field, ent));
        Button1 = ExecuteButton(self.frame, self.entries, Text = "Fetch").Return();
        Button1.pack(side = LEFT);
        button2 = ExitButton(self.frame, self.window).Return();
        button2.pack(side=RIGHT);

        
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    Window = Tk();
    fields = ["DataFile", "testMode", "StockNum"];
    MakeForm(Window, fields).SetForms();
    Window.mainloop();
    #se = DataCollect('002251_up.csv').CollectData();
    #right, wrong, datatype = ForcastData(se, 1, 5).ForcastData();
    #print ("right:", right);
    #print ("wrong:", wrong);
    #print ("涨跌:", datatype);
    #up, down = ForcastData(se, 1).ForcastNextData_Real();
    #print (up, down);
    #down, up = ForcastData(se, 1).ForcastNextData_Real();
    #print (down, up);
    
