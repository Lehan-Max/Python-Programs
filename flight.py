initial_flights_airport=int(input("enter no. of initial flights in airport: "))

number_of_flights_landed=int(input("enter no. of flights landed: "))

number_of_flights_takeoff=int(input("enter no. of flights takeoff: "))

current_no_flights=number_of_flights_landed+initial_flights_airport-number_of_flights_takeoff

print("flights landed: ",number_of_flights_landed)

print("flights takeoff: ",number_of_flights_takeoff)

print("current available flights",current_no_flights)
