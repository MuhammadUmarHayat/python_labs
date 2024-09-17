import mysql.connector

# Establish connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="eyedb"
)

mycursor = mydb.cursor()

# Function to insert feedback into the database
def save():
    sql = "INSERT INTO `feedbacks`( `doctor_id`, `patient_id`, `message`) VALUES (%s, %s, %s)"
    val = ("dr2@gmail.com", "Highway 21", "nice doctor")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Thank you for your precious feedback")

# Function to display feedback from the database
def show(doctor_id):
    sql = "SELECT * FROM `feedbacks` WHERE `doctor_id` = %s"
    mycursor.execute(sql, (doctor_id,))
    myresult = mycursor.fetchall()
    
    if len(myresult) == 0:
        print("No feedback found for the given doctor ID.")
    else:
        for x in myresult:
            print(x)


def countFB():
     sql = "SELECT count(*) FROM `feedbacks`"
     mycursor.execute(sql)  # This line was missing
     myresult = mycursor.fetchall()  # Fetch the result of the query
     print(myresult[0][0])  # Print the count of feedbacks

# Main logic to handle user input
while True:
    choice = input("Please enter 1 for save, 2 for show, 3 for count or 'q' to quit: ")
    
    if choice == "1":
        save()
    elif choice == "2":
        doctor_id = input("Please enter doctor ID: ")
        show(doctor_id)
    elif choice == "3":
        countFB()
    elif choice.lower() == 'q':
        print("Exiting the program.")
        break
    else:
        print("Please enter a valid choice.")
