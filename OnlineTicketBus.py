import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
import mysql.connector 


# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="online_ticket_bus"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()


root = tkinter.Tk()
root.title("Online Ticket Bus")


#ticket price
def enter_data():
    destination = destination_combobox.get()
    quantity_ticket_str = quantity_ticket_combobox.get()


    # Check if quantity_ticket_str is not empty
    if not quantity_ticket_str:
        # Handle the case where the quantity is not provided
        tkinter.messagebox.showwarning(title="Error", message="Quantity Ticket is required.")
        return

    quantity_ticket = int(quantity_ticket_str)


    #destination
    if destination == "Kedah to Pahang":
        price = 67
    elif destination == "Kedah to Terengganu":
        price = 75
    else:
        tkinter.messagebox.showwarning(title="Error", message="Destination is required.")
        return
    

    #quantity ticket
    if quantity_ticket > 2:
        grand_total = quantity_ticket * price * 0.9  # 10% discount for 3 and above tickets
    else:
        grand_total = quantity_ticket * price

    print('RM', grand_total)
    output_label.config(text=f"Total Price: RM {grand_total}")


    # To insert your Data to your database
    sql = "INSERT INTO user_detail (Name, Phone_number, Destination, Date, Quantity_ticket, Total_price) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name_entry.get(), phone_number_entry.get(), destination_combobox.get(), date_entry.get(), quantity_ticket_combobox.get(), grand_total)
    mycursor.execute(sql, val)
    mydb.commit()


#picker calendar
def pick_date():
    top = tkinter.Toplevel(root)
    cal = Calendar(top, font="Arial 8", selectmode="day", locale="en_US")
    cal.pack(fill="both", expand=True)
    
    def on_date_selected():
        date_label.set(cal.get_date())
        top.destroy()

    button_ok = tkinter.Button(top, text="OK", command=on_date_selected)
    button_ok.pack()
    

frame = tkinter.Frame(root)
frame.pack()


# user detail
user_info_frame =tkinter.LabelFrame(frame, text="Booking Ticket")
user_info_frame.grid(row= 0, column=0)

name_label = tkinter.Label(user_info_frame, text=" Name")
name_label.grid(row=0, column=0)
name_entry = tkinter.Entry(user_info_frame)
name_entry.grid(row=1, column=0)

phone_number_label= tkinter.Label(user_info_frame, text="Phone Number")
phone_number_label.grid(row=0, column=1)
phone_number_entry = tkinter.Entry(user_info_frame)
phone_number_entry.grid(row=1, column=1)


date_label = tkinter.Label(user_info_frame, text=" Date")
date_label.grid(row=2, column=1)
date_label = tkinter.StringVar()
date_entry = tkinter.Entry(user_info_frame, textvariable=date_label)
date_entry.grid(row=3, column=1)


#button to pick date
button_pick_date = tkinter.Button(user_info_frame, text="Pick Date", background= "grey", command=pick_date)
button_pick_date.grid(row=4, column=1)


destination_label = tkinter.Label(user_info_frame, text="Destination")
destination_combobox = ttk.Combobox(user_info_frame, values=["Kedah to Pahang", "Kedah to Terengganu"]) 
destination_label.grid(row=2, column=0)
destination_combobox.grid(row=3, column=0)


discount_label = tkinter.Label(user_info_frame, text='Purchase 3 ticket and above to get 10% off!!!', font=("Times New Romans",9, "bold"))
discount_label.grid(row=5, column=0)


quantity_ticket_label = tkinter.Label(user_info_frame, text="Quantity Ticket")
quantity_ticket_combobox= ttk.Combobox(user_info_frame, values=["1", "2", "3", "4", "5", "6"])
quantity_ticket_label.grid(row=6, column=0)
quantity_ticket_combobox.grid(row=7, column=0)


prices_text = tkinter.Text(root, height=7, width=40)
prices_text.pack(pady=20)

prices_text.insert(tkinter.END, "Destination & Prices:\n\n")
prices_text.insert(tkinter.END, "Kedah to Pahang: \nPrice: RM67\n\n")
prices_text.insert(tkinter.END, "Kedah to Terengganu: \nPrice: RM75\n\n")



# Save Button
save_button = tkinter.Button(root, text="Enter Data", background="gray", command=enter_data)
save_button.pack(pady=10)


# Output Label & result
label = tkinter.Label(root, text='Total Price', font=("Times New Romans",12))
label.pack(ipadx=10, ipady=10)
output_label = tkinter.Label(root, text="")
output_label.pack()


root.mainloop()