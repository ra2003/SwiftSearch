from tkinter import *
import time
class SearchWindow:
    def __init__(self, websites):
        self.screen_size = None
        self.all_websites = websites
        self.filtered_websites = websites
        self.root = self.create_root()
        self.query = StringVar()
        self.input_field = self.create_input()

        self.input_field.focus_set()
        self.root.bind("<FocusOut>", self.key_press)
        self.animate_in()


    def animate_in(self, begin = time.time(), end = time.time()+.3):
        """

        :param begin: time when first called
        :param end: time when first called + total time of aniamtion
        :return: None
        """
        final_alpha = .8
        alpha = (final_alpha/.3) * (time.time() - begin)
        self.root.attributes("-alpha",alpha)
        if time.time() <= end:
            self.root.after(25, self.animate_in, begin, end)
        else:
            self.root.attributes("-alpha", final_alpha)

    def create_root(self):
        root = Tk()
        self.screen_size = {"x":root.winfo_screenwidth(), "y":root.winfo_screenheight()}
        frame = {"w":500,"h":200,"x":0,"y":0}
        frame["y"]=self.screen_size["y"] - frame["h"]
        root.title("SwiftSearch - by NateRiz")
        root.geometry("{}x{}+{}+{}".format(frame["w"], frame["h"],frame["x"],frame["y"]))
        root.overrideredirect(1)
        return root

    def create_input(self):
        """
        Creates input field for the root
        :return: input field
        """
        input_field =Entry(self.root, width = 32, textvariable = self.query)
        self.query.set("Type a website: eg: facebook.com")
        input_field.bind("<Return>", self.exit_window)
        input_field.bind("<Escape>", self.exit_window)
        input_field.bind("<Key>", self.start_search)
        input_field.place(relx=0.5, rely=0.5, anchor=CENTER)
        return input_field

    def key_press(self, event):
        """
        
        :param event:
        :return:
        """
        default = "Type a website: eg: facebook.com"
        if event.keysym == "BackSpace" or self.query.get() == default:
            self.start_search(event)

        else:
            print(event.keysym)


    def start_search(self, event):
        """
        Deletes the default string when the user types a key
        :param event: calling event of function. will be a key.
        :return: None
        """
        default = "Type a website: eg: facebook.com"
        if self.query.get() == default:
            self.query.set("")
        elif event.keysym=="BackSpace" and len(self.query.get()) == 1:
            self.query.set("T"+default) # will delete the T in default.

    def exit_window(self, event):
        """
        leaves the window when unfocus or completes search.
        :param event: calling event of function
        :return:  None
        """
        self.root.destroy()

    def update(self):
        """
        Updates the mainloop of root
        :return: None
        """
        self.root.mainloop()


#TODO
#window in bottom right
#Animate in
#Animate out only on <Escape>
#picture bg
#default settings ini
#Search
