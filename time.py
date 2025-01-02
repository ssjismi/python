class Time:
    def __init__(self, hour, minute, second):
        # Initialize the time with hours, minutes, and seconds
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    # Overloading the + operator
    def __add__(self, other):
        # Add the hours, minutes, and seconds separately
        total_seconds = (self.__hour * 3600 + self.__minute * 60 + self.__second) + \
                        (other.__hour * 3600 + other.__minute * 60 + other.__second)

        # Calculate new hours, minutes, and seconds
        hour = total_seconds // 3600
        minute = (total_seconds % 3600) // 60
        second = total_seconds % 60
        
        # Return a new Time object with the summed time
        return Time(hour, minute, second)

    # Method to display the time
    def display_time(self):
        print(f"{self.__hour} hours, {self.__minute} minutes, {self.__second} seconds")

# Example usage
time1 = Time(1, 45, 30)  # 1 hour, 45 minutes, 30 seconds
time2 = Time(2, 30, 45)  # 2 hours, 30 minutes, 45 seconds

# Add two time objects using the overloaded '+' operator
sum_time = time1 + time2

# Display the result
print("Time 1: ", end="")
time1.display_time()
print("Time 2: ", end="")
time2.display_time()
print("Sum of Time 1 and Time 2: ", end="")
sum_time.display_time()
