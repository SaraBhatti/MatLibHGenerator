from tkinter import *

def Story1(win):
    def final(tl: Toplevel, name, adjective, activity, location, disaster, emotion, name2):
        text = f'''
            Dr. {name} Data and their {adjective} Developer Academy team were excited about their {activity} day, deep in the {location}
            but their plans were quickly thwarted by a {disaster}. They felt {emotion} and frustrated as they tried
            to overcome the obstacle, but things didn't go as planned. They put their large heads together to figure it out.
            To their surprise {name2} was the one trying to sabatage them.
            they vowed to get their own back on {name2} someday!
            It turned out to be a truly challenging day for the data scientists.
        '''

        tl.geometry(newGeometry='500x550')

        Label(tl, text='Story1:', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = Toplevel(win, bg='SkyBlue1')
    NewScreen.title("A Bad day")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='A Bad Day').place(x=100, y=0)
    Label(NewScreen, text='Enter your name:').place(x=0, y=35)
    Label(NewScreen, text='Enter a bad adjective:').place(x=0, y=70)
    Label(NewScreen, text='Enter an activity:').place(x=0, y=110)
    Label(NewScreen, text='Enter an obstacle:').place(x=0, y=150)
    Label(NewScreen, text='Enter an emotion:').place(x=0, y=190)
    Label(NewScreen, text='Enter a name of one of your collegues:').place(x=0, y=230)
    Name = Entry(NewScreen, width=17)
    Name.place(x=250, y=35)
    Adjective = Entry(NewScreen, width=17)
    Adjective.place(x=250, y=70)
    Activity = Entry(NewScreen, width=17)
    Activity.place(x=250, y=105)
    Obstacle = Entry(NewScreen, width=17)
    Obstacle.place(x=250, y=150)
    Emotion = Entry(NewScreen, width=17)
    Emotion.place(x=250, y=190)
    Name2 = Entry(NewScreen, width=17)
    Name2.place(x=250, y=230)
    SubmitButton = Button(NewScreen, text="Create your story", background="Tomato3", font=('Comic Sans', 12),
                          command=lambda: final(NewScreen, Name.get(), Adjective.get(), Activity.get(), Obstacle.get(), Emotion.get(), Name2.get()))
    SubmitButton.place(x=150, y=270)

def Story2(win):
    def final(tl: Toplevel, name, adjective, activity, obstacle, emotion, name2):
        text = f'''
            Dr. {name} Data and their {adjective} Developer Academy team were excited about their {activity} day,
            but their plans were quickly thwarted by a {obstacle}. They knew who was behind it, {name2}!
            They put their heads together and by the power of data they managed to figure out a Python code to help them.
            They felt {emotion} and delighted as they overcome the obstacle. 
            It turned out to be a truly brillant day for the data scientists.
        '''

        tl.geometry(newGeometry='500x550')

        Label(tl, text='A Good Day:', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = Toplevel(win, bg='medium orchid')
    NewScreen.title("A Good Day")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='A Good Day').place(x=150, y=0)
    Label(NewScreen, text='Enter your name:').place(x=0, y=35)
    Label(NewScreen, text='Enter a good adjective:').place(x=0, y=70)
    Label(NewScreen, text='Enter an activity:').place(x=0, y=110)
    Label(NewScreen, text='Enter an obstacle:').place(x=0, y=150)
    Label(NewScreen, text='Enter an emotion:').place(x=0, y=190)
    Label(NewScreen, text='Enter a name of one of your collegues:').place(x=0, y=230)
    Name = Entry(NewScreen, width=17)
    Name.place(x=250, y=35)
    Adjective = Entry(NewScreen, width=17)
    Adjective.place(x=250, y=70)
    Activity = Entry(NewScreen, width=17)
    Activity.place(x=250, y=105)
    Obstacle = Entry(NewScreen, width=17)
    Obstacle.place(x=250, y=150)
    Emotion = Entry(NewScreen, width=17)
    Emotion.place(x=250, y=190)
    Name2 = Entry(NewScreen, width=17)
    Name2.place(x=250, y=230)
    SubmitButton = Button(NewScreen, text="Create your story", background="Coral1", font=('Comic Sans', 12),
                          command=lambda: final(NewScreen, Name.get(), Adjective.get(), Activity.get(), Obstacle.get(), Emotion.get(), Name2.get()))
    SubmitButton.place(x=150, y=270)

Screen = Tk()
Screen.title("Aventures of the Lost Data Scientists")
Screen.geometry('400x400')
Screen.config(bg="SeaGreen1")
Label(Screen, text='Adventures of the lost Data Scientist').place(x=95, y=20)

# Creating buttons
Story1Button = Button(Screen, text='A Bad Day', font=("Comic Sans", 13), command=lambda: Story1(Screen), bg='FireBrick1')
Story1Button.place(x=145, y=90)
Story2Button = Button(Screen, text='A Good Day', font=("Comic Sans", 13), command=lambda: Story2(Screen), bg='FireBrick1')
Story2Button.place(x=140, y=140)

Screen.update()
Screen.mainloop()
