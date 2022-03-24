from tkinter import *

root = Tk()
root.geometry("1800x1800")
root.title(" Summer Set ")



rating_arr = []

def get_input():
    user_rating = val.get("1.0", "end-1c")
    user_feedback = val1.get("1.0", "end-1c")
    rating_arr.append([user_rating, user_feedback])
    print("Thank you 🤩, you rated this program" + " ⭐️" * int(user_rating) + " out of 5 stars, because " + user_feedback)

def get_reviews():
    print(rating_arr)

def avg_rating():
    total = sum(int(i[0]) for i in rating_arr)
    print(total/len(rating_arr))

l_rate = Label(text="Rate this program out of 5 stars")
l_review = Label(text="Write a review of the program")


val = Text(root, height=1,
                width=2,
                bg="light salmon")

val1 = Text(root, height=10,
                width=25,
                bg="light salmon")


display = Button(root, height=2,
                 width=20,
                 text="Submit",
                 command=lambda: get_input())

show = Button(root, height=2,
                 width=20,
                 text="Show Reviews",
                 command=lambda: get_reviews())

show1 = Button(root, height=2,
                 width=20,
                 text="Average Rating",
                 command=lambda: avg_rating())



l_rate.pack()
val.pack()
l_review.pack()
val1.pack()
display.pack()
show.pack()
show1.pack()

mainloop()