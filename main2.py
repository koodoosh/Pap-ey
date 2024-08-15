from tkinter import *
from tkinter import messagebox
import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from tkinter import Tk, Label, Entry, Button
import plotly.io as pio
import pandas as pd
import webbrowser
import os



try:
    df = pd.read_csv('variables.csv')
except FileNotFoundError:
    # Create a new DataFrame if the file doesn't exist
    df = pd.DataFrame({'VariableName': ['money_account', 'money_invested', 'P_L', 'var4'],
                       'Value': [100000, 0, 0, 0]})
    df.to_csv('variables.csv', index=False)

def dictionary_save():
    global portfolio
    global df1
    df1 = pd.DataFrame(list(portfolio.items()), columns=['VariableName', 'Value'])
    df1.to_csv('portfolio.csv', index=False)
    df1 = pd.read_csv('portfolio.csv')
    portfolio = dict(zip(df1['VariableName'], df1['Value']))

def to_save_var(name,var1):
    df.loc[df['VariableName'] == name , 'Value'] = var1
    df.to_csv('variables.csv', index=False)


def display_dict(dictionary):
    text_widget.delete("1.0","end")
    for key, value in dictionary.items():
        text_widget.insert(END, f'{key}: {value}\n')

def show_popup(xyz):
    messagebox.showinfo("Information", ""+str(xyz))

df1 = pd.read_csv('portfolio.csv')
portfolio = dict(zip(df1['VariableName'], df1['Value']))


window=Tk()
window.title("LearnTrade")
window.geometry('1920x1080')
window.configure(background='black')
window.minsize(width=500, height=500)


background_image = PhotoImage(file='1234.png')

# Create a label widget to display the image
background_label = Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)


money_account = df.loc[df['VariableName'] == 'money_account', 'Value'].values[0]
money_invested = df.loc[df['VariableName'] == 'money_invested', 'Value'].values[0]
P_L = df.loc[df['VariableName'] == 'P_L', 'Value'].values[0]
var4 = df.loc[df['VariableName'] == 'var4', 'Value'].values[0]




def find_cost(x):
    from bs4 import BeautifulSoup
    import requests
    response = requests.get(f"https://www.google.com/finance/quote/{x}:NSE")
    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")
    p = soup.find(class_="YMlKec fxKbKc")
    rice = p.getText()
    pric = ""
    for i in str(rice):
        if i != "₹" and i != ",":
            pric = pric + i
    price = float(str(pric))
    return price



label1= Label(text=f" Money in account = {money_account}          ",font=('Arial',25,'bold'),bg='black',fg='white',borderwidth=7,width=30,height=1)
label1.place(x=1000,y=50)


label2= Label(text=f" Money invested = {money_invested}          ",font=('Arial',25,'bold'),bg='black',fg='white',borderwidth=7,width=30,height=1)
label2.place(x=1000,y=100)


label3= Label(text=f"Profit and loss = {P_L}          ",font=('Arial',25,'bold'),bg='black',fg='white',borderwidth=7,width=30,height=1)
label3.place(x=1000,y=150)


label4= Label(text=f"Enter the Name of the Stock Below:",font=('Arial',25,'bold'),bg='black',fg='white',borderwidth=7,width=30,height=1)
label4.place(x=30,y=20)


label5=Label(text="The price of stock is :      ",font=('Arial',25,'bold'),bg='black',fg='white',borderwidth=7,width=25,height=1)
label5.place(x=30,y=225)

entry1 = Entry(borderwidth=7,width=30,font=('Arial',25,'bold'))
entry1.place(x=30,y=75)
price=0
stock=""
def action():
    if entry1.get() == '':
        # Show error popup if condition is not met
        show_popup("No objects to concatenate")
    sstock = entry1.get()
    stock = str(sstock.upper())
    price=find_cost(stock)
    label5.config(text=f"The price of stock is : {price}")




button = Button(text="Get Price", command=action, font=('Arial',25,'bold'),bg='white', fg='black', borderwidth=7, width=10, height=1)
button.place(x=30,y=150)
print(price)

#label6=Label(text="Enter buy or sell : ",font=('Arial',35,'bold'),bg='#AAFFFE',fg='black',borderwidth=7,width=25,height=1)
#label6.place(x=700,y=300)


#entry2 = Entry(borderwidth=7,width=30,font=('Arial',35,'bold'))
#entry2.place(x=700,y=375)


label7=Label(text="Enter Quantity : ",font=('Arial',25,'bold'),bg='black',fg='white',borderwidth=7,width=15,height=1)
label7.place(x=120,y=300)


entry3 = Entry(borderwidth=7,width=30,font=('Arial',25,'bold'))
entry3.place(x=30,y=350)

label10=Label(text="Total Amount:  ",font=('Arial',25,'bold'),bg='black',fg='white',borderwidth=7,width=18,height=1)
label10.place(x=30,y=500)

def total():
    if entry1.get() == '':
        # Show error popup if condition is not met
        show_popup("No objects to concatenate")
    sstock = entry1.get()
    stock = str(sstock.upper())
    quantity = entry3.get()
    if str(quantity)[0]>='0' and str(quantity)[0]<='9':
        price = find_cost(stock)
        amount=str(int(price)*int(quantity))
        label10.config(text=f"Total Amount: {amount}")
    else:
        show_popup("Invalid Quantity")





button6 = Button(text="Total Price",command=total,font=('Arial',25,'bold'),bg='white',fg='black',borderwidth=7,width=10,height=1)
button6.place(x=30,y=420)



def transaction():
    global money_invested
    global money_account
    global operation
    sstock=entry1.get()
    stock=str(sstock.upper())

    quantity=entry3.get()
    if str(quantity)[0]>='0' and str(quantity)[0]<='9':
        price=find_cost(stock)
        if operation=="buy":
            if (price*int(quantity))<=money_account:
                if stock not in portfolio:
                    portfolio[stock]=quantity
                    dictionary_save()

                else:
                    portfolio[stock]=str(int(portfolio[stock])+int(quantity))
                    dictionary_save()
                money_account=money_account-(price*int(quantity))
                to_save_var('money_account',money_account)
                money_invested = money_invested + (price * int(quantity))
                to_save_var('money_invested', money_invested)
            else:
                show_popup("Not Enough Funds")
        elif operation == "sell":
            if stock in portfolio and int(portfolio[stock])>=int(quantity):
                portfolio[stock]=str(int(portfolio[stock])-int(quantity))
                money_account = money_account + (price * int(quantity))
                to_save_var('money_account', money_account)
                money_invested = money_invested-(price * int(quantity))
                to_save_var('money_invested', money_invested)
                label1.config(text=f" Money in account = {money_account}          ")
                label2.config(text=f" Money invested = {money_invested}          ")
                for i in portfolio:
                    if int(portfolio[i]) == 0:
                        portfolio.pop(i)
                        dictionary_save()
                        display_dict(portfolio)
            else:
                show_popup("You dont have enough quantity to sell.")
        else:
            show_popup("Invalid Input")
        dictionary_save()
        display_dict(portfolio)
        label1.config(text=f" Money in account = {money_account}          ")
        label2.config(text=f" Money invested = {money_invested}          ")
        entry1.delete(0,END)
        entry3.delete(0, END)
        label10.config(text="Total Amount:  ")
        label5.config(text="The price of stock is :      ")
    else:
        show_popup("Invalid Quantity Input")



def buy():
    if entry1.get() == '':
        # Show error popup if condition is not met
        show_popup("No objects to concatenate")
    global operation
    operation='buy'
    transaction()
def sell():
    if entry1.get() == '':
        # Show error popup if condition is not met
        show_popup("No objects to concatenate")
    global operation
    operation='sell'
    transaction()

button2 = Button(text="BUY",command=buy,font=('Arial',25,'bold'),bg='#AAFFFE',fg='black',borderwidth=7,width=10,height=1)
button2.place(x=30,y=575)

button4 = Button(text="SELL",command=sell,font=('Arial',25,'bold'),bg='#AAFFFE',fg='black',borderwidth=7,width=10,height=1)
button4.place(x=330,y=575)


text_widget = Text(window, wrap=WORD,font=('Arial',25,'bold'),bg='black',fg='white',borderwidth=7,width=25,height=9)
text_widget.place(x=1050,y=375)

label8=Label(text="PORTFOLIO",font=('Arial',25,'bold'),bg='black',fg='white',borderwidth=7,width=20,height=1)
label8.place(x=1050,y=325)

'''
logo=PhotoImage(file='LogoS.png')
label11=Label(window,image=logo,height=200,width=200)
label11.place(x=1300,y=20)
'''
def see_P_L():

    a=0
    for stock in portfolio:
        a=a+(int(portfolio[stock])*int(find_cost(stock)))
    p=a-money_invested
    r=round(p,3)
    label3.config(text=f"Profit and loss = {r}          ")


def plot_stock_in_browser(stock):
    # Fetch historical stock data
    stock_data = yf.download(stock, period="5y", interval="1d")

    # Check if data is available
    if stock_data.empty:
        print(f"No data found for {stock}. Please check the stock symbol and try again.")
        return

    # Create a candlestick chart using Plotly
    fig = make_subplots(rows=1, cols=1)

    candlestick = go.Candlestick(
        x=stock_data.index,
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        name=stock
    )

    fig.add_trace(candlestick)

    # Update layout for better visualization
    fig.update_layout(
        title=f"{stock} Stock Price",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        xaxis_rangeslider_visible=False
    )

    # Convert Plotly figure to an HTML file
    html_file = "stock_plot.html"
    pio.write_html(fig, file=html_file, auto_open=False)

    # Open the HTML file in the default web browser
    webbrowser.open(f"file://{os.path.abspath(html_file)}")
def on_button_click():
    if entry1.get() == '':
        # Show error popup if condition is not met
        show_popup("No objects to concatenate")
    stock_symbol = entry1.get().upper()  # Using entry1 for stock symbol input
    plot_stock_in_browser(stock_symbol)


# Button to trigger the plot using entry1 input
button = Button(window, text="View Chart", command=on_button_click,font=('Arial',25,'bold'),bg='#AAFFFE',fg='black',borderwidth=7,width=25,height=1)
button.place(x=30, y=650)
redirect=PhotoImage(file='redirect.png')
label11=Button(window,image=redirect,command=on_button_click,height=20,width=20)
label11.place(x=520,y=650)


button3 = Button(text="Current P&L",command=see_P_L,font=('Arial',25,'bold'),bg='#AAFFFE',fg='black',borderwidth=7,width=10,height=1)
button3.place(x=1050,y=225)


display_dict(portfolio)


window.mainloop()