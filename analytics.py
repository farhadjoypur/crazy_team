import tkinter as tk
import matplotlib
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bcProject"
)

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Matplotlib Demo')

        # countData = mydb.cursor()
        # countData.execute("SELECT COUNT(name), message * FROM message")
        # countResult = countData.fetchall()
        #
        # nameData = mydb.cursor()
        # nameData.execute("SELECT * FROM message GROUP BY name")
        # nameResult = nameData.fetchall()
        # # prepare data
        #
        # for names in nameResult:
        #     print(names["name"])
        # data = {
        #     'sami': 28,
        #     'forhad': 16,
        #     'nimmi😍': 10,
        #     'joy': 7,
        #     'tahin': 9,
        # }
        data = {}
        mycursor = mydb.cursor()
        mycursor.execute("SELECT name,COUNT(*) FROM usercomment GROUP BY name")
        myresult = mycursor.fetchall()

        for x in myresult:
            data.update({x[0]:x[1]})
            print(data)
        languages = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()