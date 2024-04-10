-- INSERT INTO AEROPLANE
--     (Aeroplane_id, Airline_name, Fuel_Capacity, Seat_Capacity)
-- VALUES
--     (1, 'Delta Airlines', 5000, 200),
--     (2, 'British Airways', 6000, 250),
--     (3, 'ANA', 4500, 180),
--     (4, 'Emirates', 7000, 300),
--     (5, 'Air France', 5500, 220);

-- INSERT INTO AIRPORT
--     (City, Airport_Type, Number_of_terminals, Location_in_the_city, Number_of_runways)
-- VALUES
--     ('New York', true, 4, 'JFK International Airport', 6),
--     ('Paris', true, 6, 'Los Angeles International Airport', 8),
--     ('Dubai', true, 3, 'O Hare International Airport', 7),
--     ('London', true, 5, 'Heathrow Airport', 2),
--     ('Tokyo', true, 2, 'Narita International Airport', 3);


-- INSERT INTO FLIGHT
--     (Flight_id, Arrival_city, Departure_city, Total_number_of_passengers, Aeroplane_ID)
-- VALUES
--     (1, 'London', 'New York', 150, 1),
--     (2, 'New York', 'London', 180, 2),
--     (3, 'Tokyo', 'Dubai', 200, 3),
--     (4, 'Dubai', 'Paris', 170, 4),
--     (5, 'Paris', 'New York', 190, 5);

-- INSERT INTO AIRLINE
--     (Airline_Name, Owner_Name, Net_worth)
-- VALUES
--     ('Delta Airlines', 'Delta Group', 500000000),
--     ('British Airways', 'International Airlines Group', 700000000),
--     ('ANA', 'ANA Holdings', 350000000),
--     ('Emirates', 'The Emirates Group', 1000000000),
--     ('Air France', 'Air France-KLM Group', 600000000);

-- INSERT INTO SHOPS
--     (Shop_ID, Shop_Name, Airport_id, Shop_Type, Licence_Expiry, Timings)
-- VALUES
--     (1, 'Duty-Free Shop', 'New York', 'Retail', '2023-12-31', '2023-12-02 09:00:00'),
--     (2, 'Tech Haven', 'London', 'Electronics', '2023-11-30', '2023-12-02 10:30:00'),
--     (3, 'Sushi Delight', 'Tokyo', 'Food', '2023-12-15', '2023-12-02 12:00:00'),
--     (4, 'Luxury Watches', 'Dubai', 'Accessories', '2024-01-31', '2023-12-02 14:30:00'),
--     (5, 'Fashion Paradise', 'Paris', 'Apparel', '2023-12-20', '2023-12-02 16:00:00');

-- INSERT INTO PASSENGER
--     (Passenger_ID, Name, Date_of_Birth, Nationality)
-- VALUES
--     (201, 'Michael Johnson', '1990-05-15', 'American'),
--     (202, 'Sophie Turner', '1978-07-10', 'British'),
--     (203, 'Yuki Tanaka', '1985-02-21', 'Japanese'),
--     (204, 'Khaled Al-Farsi', '1995-12-03', 'Emirati'),
--     (205, 'Isabelle Dubois', '1980-09-28', 'French');

-- INSERT INTO PHONE_NUMBER
--     (Person_Id, Phone_number)
-- VALUES
--     (105, 1234567890),
--     (102, 9876543210),
--     (104, 5551234567),
--     (103, 9998887777),
--     (101, 1112223333);

ALTER TABLE PHONE_NUMBER
MODIFY Phone_number BIGINT;

-- INSERT INTO PASSENGER
--     (Passenger_ID, Name, Date_of_Birth, Nationality)
-- VALUES
--     (101, 'Michael Johnson', '1990-05-15', 'American'),
--     (102, 'Sophie Turner', '1995-12-03', 'British'),
--     (103, 'Yuki Tanaka', '1978-07-10', 'Japanese'),
--     (104, 'Khaled Al-Farsi', '1980-09-28', 'Emirati'),
--     (105, 'Isabelle Dubois', '1985-02-21', 'French');

-- Sample data for AIRLINE_MANUFACTURE table

-- INSERT INTO AEROPLANE
--     (Aeroplane_id, Airline_name, Fuel_Capacity, Seat_Capacity)
-- VALUES
--     (1, 'Delta Airlines', 5000, 200),
--     (2, 'British Airways', 6000, 250),
--     (3, 'ANA', 4500, 180),
--     (4, 'Emirates', 7000, 300),
--     (5, 'Air France', 5500, 220);

-- INSERT INTO FLIGHT
--     (Flight_id, Arrival_city, Departure_city, Total_number_of_passengers, Aeroplane_ID)
-- VALUES
--     (1, 'London', 'New York', 150, 1),
--     (2, 'New York', 'London', 180, 2),
--     (3, 'Tokyo', 'Dubai', 200, 3),
--     (4, 'Dubai', 'Paris', 170, 4),
--     (5, 'Paris', 'New York', 190, 5);

-- INSERT INTO EMPLOYEE
--     (Employee_id, Name, Salary, Working_Hours, Working_Place, Airport_city, Flight_Id)
-- VALUES
--     (101, 'John Doe', 50000, 40, true, 'New York', 1),
--     (102, 'Alice Smith', 60000, 35, true, 'London', 2),
--     (103, 'Ken Tanaka', 55000, 38, true, 'Tokyo', 3),
--     (104, 'Fatima Ahmed', 65000, 42, true, 'Dubai', 4),
--     (105, 'Claire Dupont', 58000, 37, true, 'Paris', 5);


-- INSERT INTO WORKING_ROLE
--     (Role_Id, Role)
-- VALUES
--     (101, 'Pilot'),
--     (104, 'Flight Attendant'),
--     (102, 'Ground Crew'),
--     (103, 'Air Traffic Controller'),
--     (105, 'Maintenance Technician');

-- INSERT INTO TICKET
--     (PNR, Passenger_ID, Flight_id, Seat_Number, Ticket_type, Booking_agent, Ticket_price, Booking_Date, Booking_time)
-- VALUES
--     (1001, 101, 1, 15, 'Economy', 'Travel Agency A', 500, '2023-01-10', '2023-01-10 08:30:00'),
--     (1002, 102, 2, 22, 'Business', 'Travel Agency B', 1200, '2023-02-05', '2023-02-05 12:15:00'),
--     (1003, 103, 3, 8, 'Economy', 'Travel Agency C', 450, '2023-03-20', '2023-03-20 15:45:00'),
--     (1004, 104, 4, 14, 'First Class', 'Travel Agency D', 2000, '2023-04-12', '2023-04-12 18:00:00'),
--     (1005, 105, 5, 10, 'Economy', 'Travel Agency E', 600, '2023-05-30', '2023-05-30 21:20:00');

-- INSERT INTO BAGGAGE
--     (Baggage_id, Weight, Ticket_ID)
-- VALUES
--     (1, 20, 1001),
--     (2, 15, 1002),
--     (3, 30, 1003),
--     (4, 25, 1004),
--     (5, 18, 1005);