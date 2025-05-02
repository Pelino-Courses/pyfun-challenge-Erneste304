import datetime

def date_difference(start_date, end_date):
    """
    Calculate the difference between two dates in days.
    Args:
       start_date: The starting date in 'YYYY-MM-DD' format or as datetime.date object.
       end_date: The ending date in 'YYYY-MM-DD' format or as datetime.date object.
    
    Returns:
        int: Number of days between the two dates (always positive).
    """
    if isinstance(start_date, str):
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    if isinstance(end_date, str):
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    return abs((end_date - start_date).days)

def main():
    print("Date Difference Calculator")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        
        if end_date < start_date:
            print("End date is before the start date.")
        
        difference = date_difference(start_date, end_date)
        print(f"The difference between {start_date} and {end_date} is {difference} days.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
