import tkinter as tk
import datetime
import calendar

class CalendarViewer(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        # Header
        self.header = tk.Frame(self)
        self.prev_month_button = tk.Button(self.header, text='<', command=self.prev_month)
        self.next_month_button = tk.Button(self.header, text='>', command=self.next_month)
        self.month_year_label = tk.Label(self.header, text='')
        
        self.prev_month_button.pack(side=tk.LEFT)
        self.next_month_button.pack(side=tk.RIGHT)
        self.month_year_label.pack(side=tk.TOP)
        self.header.pack(side=tk.TOP, fill=tk.X)
        
        # Tage
        self.days = []
        for i in range(6):
            row = []
            for j in range(7):
                label = tk.Label(self, text='', relief=tk.RIDGE)
                label.grid(row=i+1, column=j, sticky='nsew')
                row.append(label)
            self.days.append(row)
        
        self.update_calendar()
    
    def update_calendar(self):
        year = datetime.date.today().year
        month = datetime.date.today().month
        self.current_date = datetime.date(year, month, 1)
        self.update_days()
        
    def prev_month(self):
        prev_month = self.current_date.month - 1
        prev_year = self.current_date.year
        if prev_month == 0:
            prev_month = 12
            prev_year -= 1
        self.current_date = datetime.date(prev_year, prev_month, 1)
        self.update_days()
        
    def next_month(self):
        next_month = self.current_date.month + 1
        next_year = self.current_date.year
        if next_month == 13:
            next_month = 1
            next_year += 1
        self.current_date = datetime.date(next_year, next_month, 1)
        self.update_days()
    
    def update_days(self):
        month = self.current_date.month
        year = self.current_date.year
        
        month_name = calendar.month_name[month]
        self.month_year_label.config(text=month_name + ' ' + str(year))
        
        cal = calendar.monthcalendar(year, month)
        for i in range(len(cal)):
            week = cal[i]
            for j in range(len(week)):
                day = week[j]
                if day == 0:
                    self.days[i][j].config(text='')
                else:
                    self.days[i][j].config(text=str(day))

root = tk.Tk()
CalendarViewer.pack(side=tk.TOP, padx=10, pady=10)
root.mainloop()
