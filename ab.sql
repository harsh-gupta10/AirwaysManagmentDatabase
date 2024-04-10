CREATE TABLE AIRPORT (
  City varchar(25) PRIMARY KEY,
  Airport_Type boolean,
  Number_of_terminals integer,
  Location_in_the_city varchar(100),
  Number_of_runways integer
);


CREATE TABLE AEROPLANE (
  Aeroplane_id integer PRIMARY KEY,
  Airline_name varchar(50),
  Fuel_Capacity integer,
  Seat_Capacity integer
);

CREATE TABLE EMPLOYEE (
  Employee_id integer PRIMARY KEY,
  Name varchar(100),
  Salary integer,
  Working_Hours integer,
  Working_Place boolean,
  Airport_city varchar(25),
  Flight_Id integer
);

CREATE TABLE PASSENGER (
  Passenger_ID integer PRIMARY KEY,
  Name varchar(50),
  Date_of_Birth Date,
  Nationality varchar(100)
);

CREATE TABLE FLIGHT (
  Flight_id integer PRIMARY KEY,
  Arrival_city varchar(100),
  Departure_city varchar(100),
  Total_number_of_passengers integer,
  Aeroplane_ID integer
);

CREATE TABLE TICKET (
  PNR integer PRIMARY KEY,
  Passenger_ID integer,
  Flight_id integer,
  Seat_Number integer,
  Ticket_type varchar(50),
  Booking_agent varchar(50),
  Ticket_price integer,
  Booking_Date Date,
  Booking_time timestamp
);

CREATE TABLE AIRLINE (
  Airline_Name varchar(50) PRIMARY KEY,
  Owner_Name varchar(50),
  Net_worth integer
);

CREATE TABLE BAGGAGE (
  Baggage_id integer,
  Weight integer,
  Ticket_ID integer
);

CREATE TABLE SHOPS (
  Shop_ID integer,
  Shop_Name varchar(100),
  Airport_id varchar(50),
  Shop_Type varchar(50),
  Licence_Expiry Date,
  Timings timestamp
);

CREATE TABLE WORKING_ROLE (
  Role_Id integer,
  Role varchar(100)
);

CREATE TABLE PHONE_NUMBER (
  Person_Id integer,
  Phone_number integer(10)
);

CREATE TABLE AGE_OF_PASSENGER (
  Date_of_Birth Date PRIMARY KEY,
  Age integer
);

CREATE TABLE AIRLINE_MANUFACTURE (
  Airline_name varchar(50) PRIMARY KEY,
  Manufacturer_comapany varchar(100)
);

ALTER TABLE PASSENGER ADD FOREIGN KEY (Date_of_Birth) REFERENCES AGE_OF_PASSENGER (Date_of_Birth);

ALTER TABLE WORKING_ROLE ADD FOREIGN KEY (Role_Id) REFERENCES EMPLOYEE (Employee_id);

ALTER TABLE BAGGAGE ADD FOREIGN KEY (Ticket_ID) REFERENCES TICKET (PNR);

ALTER TABLE TICKET ADD FOREIGN KEY (Passenger_ID) REFERENCES PASSENGER (Passenger_ID);

ALTER TABLE SHOPS ADD FOREIGN KEY (Airport_id) REFERENCES AIRPORT (City);

ALTER TABLE AIRLINE_MANUFACTURE ADD FOREIGN KEY (Airline_name) REFERENCES AIRLINE (Airline_Name);

ALTER TABLE AEROPLANE ADD FOREIGN KEY (Airline_name) REFERENCES AIRLINE_MANUFACTURE (Airline_name);

ALTER TABLE TICKET ADD FOREIGN KEY (Flight_id) REFERENCES FLIGHT (Flight_id);

ALTER TABLE FLIGHT ADD FOREIGN KEY (Aeroplane_ID) REFERENCES AEROPLANE (Aeroplane_id);

ALTER TABLE EMPLOYEE ADD FOREIGN KEY (Flight_Id) REFERENCES FLIGHT (Flight_id);

ALTER TABLE EMPLOYEE ADD FOREIGN KEY (Airport_city) REFERENCES AIRPORT (City);

ALTER TABLE FLIGHT ADD FOREIGN KEY (Departure_city) REFERENCES AIRPORT (City);

ALTER TABLE FLIGHT ADD FOREIGN KEY (Arrival_city) REFERENCES AIRPORT (City);

ALTER TABLE PHONE_NUMBER ADD FOREIGN KEY (Person_Id) REFERENCES EMPLOYEE (Employee_id);

ALTER TABLE PHONE_NUMBER ADD FOREIGN KEY (Person_Id) REFERENCES PASSENGER (Passenger_ID);