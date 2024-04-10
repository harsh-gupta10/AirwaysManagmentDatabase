import pymysql
import subprocess as sp
import pymysql.cursors


def option1schedflight():
    query2 = ("Select MAX(Flight_id) from flight;")
    cursor.execute(query2)
    result = cursor.fetchall()
    inner_value1 = result[0][0]
    row = {}
    print("Enter flight details: ")

    row["Flight_id"] = inner_value1 + 1
    row["Departure_date"] = input("Departure Date (YYYY-MM-DD): ")
    row["Departure_time"] = input("Departure Time (HH:MM:SS): ")
    row["Arrival_city"] = input("Arrival City: ")
    row["Departure_city"] = input("Departure City: ")
    row["Total_number_of_seats"] = int(input("Total Number of Seats: "))
    row["Aeroplane_id"] = int(input("Aeroplane ID: "))
    row["Duration"] = input("Duration (HH:MM:SS): ")
    query = "INSERT INTO FLIGHT(Flight_id, departure_date, departure_time, Arrival_city, Departure_city, Total_number_of_passengers, Aeroplane_id,Duration) VALUES(%d, '%s', '%s', '%s', '%s', %d, %d, '%s')" % (
        row["Flight_id"], row["Departure_date"], row["Departure_time"], row["Arrival_city"], row["Departure_city"],
        row["Total_number_of_seats"], row["Aeroplane_id"], row["Duration"])

    cursor.execute(query)
    connection.commit()

    print("Inserted Into Database")


def option2booktick():
    # ask for booking a ticket for exisitng passenger or new customer if existing then ask only for passenger id else create new passenger
    query2 = ("Select MAX(Passenger_ID) from passenger;")
    cursor.execute(query2)
    result = cursor.fetchall()
    inner_value1 = result[0][0]
    # print(inner_value)
    query3 = ("Select MAX(PNR) from ticket;")
    cursor.execute(query3)
    result2= cursor.fetchall()
    inner_value2 = result2[0][0]
    print("Enter ticket details: ")
    row = {}
    print("Do you want to book ticket for existing passenger? (y/n)")
    str = input()
    if (str == 'n'):
        print("Enter Passenger details: ")
        row["Passenger_ID"] = inner_value1 + 1
        row["Name"] = input("Name: ")
        row["Date_of_Birth"] = input("Date of Birth (YYYY-MM-DD): ")
        row["Nationality"] = input("Nationailty: ")
        query = "INSERT INTO PASSENGER(Passenger_ID,Name,Date_of_Birth,Nationality) VALUES(%d,'%s','%s','%s')" % (
            row["Passenger_ID"], row["Name"], row["Date_of_Birth"], row["Nationality"])
        cursor.execute(query)
        connection.commit()
        print("Enter ticket details: ")
        row["PNR"] = inner_value2 + 1
        row["Flight_id"] = int(input("Flight ID: "))
        row["Seat_Number"] = int(input("Seat Number: "))
        row["Ticket_Type"] = input("Ticket Type: ")
        row["Booking_agent"] = input("Booking Agent: ")
        row["Ticket_price"] = int(input("Ticket Price: "))
        row["Booking_Date"] = input("Booking Date (YYYY-MM-DD): ")
        row["Booking_time"] = input("Booking Time (HH:MM:SS): ")
        query = "INSERT INTO TICKET(PNR, Passenger_ID, Flight_id, Seat_Number, Ticket_Type, Booking_agent, Ticket_price, Booking_Date, Booking_time) VALUES(%d, %d, %d, %d, '%s', '%s', %d, '%s', '%s')" % (
            row["PNR"], row["Passenger_ID"], row["Flight_id"], row["Seat_Number"], row["Ticket_Type"],
            row["Booking_agent"], row["Ticket_price"], row["Booking_Date"], row["Booking_time"])
        cursor.execute(query)
        connection.commit()

    else:
        print("Enter ticket details: ")
        row["PNR"] = inner_value2 + 1
        row["Passenger_ID"] = int(input("Passenger ID: "))
        row["Flight_id"] = int(input("Flight ID: "))
        row["Seat_Number"] = int(input("Seat Number: "))
        row["Ticket_Type"] = input("Ticket Type: ")
        row["Booking_agent"] = input("Booking Agent: ")
        row["Ticket_price"] = int(input("Ticket Price: "))
        row["Booking_Date"] = input("Booking Date (YYYY-MM-DD): ")
        row["Booking_time"] = input("Booking Time (HH:MM:SS): ")
        query = "INSERT INTO TICKET(PNR, Passenger_ID, Flight_id, Seat_Number, Ticket_Type, Booking_agent, Ticket_price, Booking_Date, Booking_time) VALUES(%d, %d, %d, %d, '%s', '%s', %d, '%s', '%s')" % (
            row["PNR"], row["Passenger_ID"], row["Flight_id"], row["Seat_Number"], row["Ticket_Type"],
            row["Booking_agent"], row["Ticket_price"], row["Booking_Date"], row["Booking_time"])
        cursor.execute(query)
        connection.commit()
def option3updatepassdetails():
    print("Enter passenger id: ")
    id = int(input())
    print("Do you want to update name? (y/n)")
    str = input()
    if (str == 'y'):
        print("Enter new name: ")
        name = input()
        query = "UPDATE PASSENGER SET Name = '%s' WHERE Passenger_ID = %d" % (name, id)
        cursor.execute(query)
        connection.commit()
    print("Do you want to update Date of Birth? (y/n)")
    str = input()
    if (str == 'y'):
        print("Enter new Date of Birth: ")
        dob = input()
        query = "UPDATE PASSENGER SET Date_of_Birth = '%s' WHERE Passenger_ID = %d" % (dob, id)
        cursor.execute(query)
        connection.commit()
    print("Do you want to update Nationality? (y/n)")
    str = input()
    if (str == 'y'):
        print("Enter new Nationality: ")
        nationality = input()
        query = "UPDATE PASSENGER SET Nationality = '%s' WHERE Passenger_ID = %d" % (nationality, id)
        cursor.execute(query)
        connection.commit()


def option4changerunways():
    print("Enter airport name: ")
    id = (input())
    print("Enter new number of runways: ")
    runways = int(input())
    query = "UPDATE AIRPORT SET Number_of_runways = %d WHERE City = '%s'" % (runways, id)
    cursor.execute(query)
    connection.commit()


def option5canceltick():
    print("Enter ticket number: ")
    id = int(input())
    queryi="DELETE FROM Baggage where Ticket_ID= %d " % (id)
    cursor.execute(queryi)
    connection.commit()

    query = "DELETE FROM TICKET WHERE PNR = %d" % (id)
    cursor.execute(query)
    connection.commit()


def option6remshop():
    print("Enter airport name: ")
    id = (input())
    print("Enter shop name: ")
    shop = input()
    query = "DELETE FROM SHOPS WHERE Airport_id = '%s' AND Shop_Name = '%s'" % (id, shop)
    cursor.execute(query)
    connection.commit()


def option7printpassdet():
    print("Enter passenger id: ")
    id = int(input())
    query = "SELECT * FROM PASSENGER WHERE Passenger_ID = %d" % (id)
    cursor.execute(query)
    result = cursor.fetchall()
    # for row in result:
    print(result)


def option8printtickdet():
    print("Enter ticket number: ")
    id = int(input())
    query = "SELECT * FROM TICKET WHERE PNR = %d" % (id)
    cursor.execute(query)
    result = cursor.fetchall()
    # for row in result:
    print(result)


def option9allticketsofagencya():
    query = "SELECT * FROM TICKET WHERE Booking_agent = 'Travel Agency A'"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)


def option10domairports():
    query = "SELECT * FROM AIRPORT WHERE Airport_Type = 'Domestic'"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)


def option11totalrevenue():
    print("Enter flight id: ")
    id = int(input())
    query = "SELECT SUM(Ticket_price) FROM TICKET WHERE Flight_id = %d" % (id)
    cursor.execute(query)
    result = cursor.fetchall()
    # for row in result:
    print(result)


def option12avgfare():
    print("Enter departure city: ")
    dep = input()
    print("Enter arrival city: ")
    arr = input()
    query = "SELECT AVG(Ticket_price) FROM TICKET JOIN FLIGHT ON TICKET.Flight_id=FLIGHT.Flight_id WHERE Departure_city = '%s' AND Arrival_city = '%s'" % (
    dep, arr)
    cursor.execute(query)
    result = cursor.fetchall()
    # for row in result:
    print(result)


def option13passdetailsstartswiths():
    query = "SELECT * FROM PASSENGER WHERE Name LIKE 'S%'"
    cursor.execute(query)
    result = cursor.fetchall()
    # print(result)
    for row in result:
        print(row)

def option14flightsinnovember():
    # print("reached here")
    query = "SELECT * FROM FLIGHT WHERE departure_date BETWEEN '2023-11-01' AND '2023-11-30'"
    cursor.execute(query)
    result = cursor.fetchall()
    # print(result)
    for row in result:
        print(row)
def option15mostusedairline():
    query = "SELECT A.Airline_Name FROM FLIGHT AS F JOIN AEROPLANE AS A ON A.Aeroplane_id = F.Aeroplane_ID GROUP BY A.Airline_Name ORDER BY COUNT(F.Flight_id) DESC LIMIT 1;"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(result)


def option16():
    print("Enter the Departure_date: ")
    date = input()
    query = "SELECT F.Flight_id, F.Arrival_city, F.Departure_city FROM FLIGHT AS F JOIN ticket AS T ON T.Flight_id = F.Flight_id WHERE F.departure_date = '%s' ORDER BY F.departure_time ASC, T.Ticket_price ASC;" % (date)
    cursor.execute(query)
    result = cursor.fetchall()
    # for row in result:
    print(result)


# def option16():


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if (ch == 1):
        option1schedflight()
    elif (ch == 2):
        option2booktick()
    elif (ch == 3):
        option3updatepassdetails()
    elif (ch == 4):
        option4changerunways()
    elif (ch == 5):
        option5canceltick()
    elif (ch == 6):
        option6remshop()
    elif (ch == 7):
        option7printpassdet()
    elif (ch == 8):
        option8printtickdet()
    elif (ch == 9):
        option9allticketsofagencya()
    elif (ch == 10):
        option10domairports()
    elif (ch == 11):
        option11totalrevenue()
    elif (ch == 12):
        option12avgfare()
    elif (ch == 13):
        option13passdetailsstartswiths()
    elif (ch == 14):
        option14flightsinnovember()
    elif (ch == 15):
        option15mostusedairline()
    elif(ch == 16):
        option16()
    else:
        print("Error: Invalid Option")


db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "air",
}

connection = pymysql.connect(**db_config)
cursor = connection.cursor()

while (1):
    print("1. Schedule a flight")  # insert
    print("2. Book a ticket")  # insert
    print("3. Update details of a passenger")  # update
    print("4. Change the number of runways in an airport")  # update
    print("5. Cancel a ticket")  # delete
    print("6. Remove a shop from airport")  # delete
    print("7. Select details of a passenger and print it")
    print("8. Select a ticket of a passenger and print its details")
    print("9. List of All ticket that are booked by Travel agency A")
    print("10. List of domestic airports")
    print("11. Total revenue collected by a flight")
    print("12. Determine the average fare for flights between two specific airports")
    print("13. Print passenger details starting  name with s")
    print("14. Print all flights scheduled in november ")
    print("15. Select the most used airline")
    print("16. Print All flights from one city to another having same date and time")
    print("17. logout")
    ch = int(input("Enter choice> "))
    if ch == 17:
        print("Success in life")
        exit()
    else:
        dispatch(ch)

cursor.close()
connection.close()



