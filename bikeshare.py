import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

months = {'january': 1,
          'february:': 2,
          'march': 3,
          'april': 4,
          'may': 5,
          'june': 6,
          'july': 7,
          'august': 8,
          'september': 9,
          'october': 10,
          'november': 11,
          'december': 12}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO:get user input for city (chicago, new york city, washington).HINT: Use a while loop to handle invalid inputs
    # Loop until user gives value as requested
    while True:
        city = input('Select one of the cities from this list (Chicago, New York City, Washington): ')
        city = city.lower().strip()
        if city in CITY_DATA:
            break
        else:
            print('Sorry, that is not a valid value for city \n')

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('Enter a month in full (January - December) or type all for all months: ')
        month = month.lower().strip()
        # Checks if input does not equal all
        if month != 'all':
            try:
                # Checks if the input (key) is in the months dict
                if month in months:
                    break
                else:
                    print('Value is not a valid month')
            except:
                print('Please enter a valid integer 1 - 12')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while True:
        day = input('Please type in a day of the week (Monday - Sunday) or type all for all days: ')
        day = day.lower().strip()
        if day == 'all':
            break
        elif day in days:
            break

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Opens the data file for requested city
    df = pd.read_csv(CITY_DATA[city])
    # Convert the Start Time column to a datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month != 'all':
        month_numeric = months[month]
        df['month'] = df['Start Time'].dt.month
        df = df[df['month'] == month_numeric]

    if day != 'all':
        df['weekday'] = df['Start Time'].dt.weekday_name
        df = df[df['weekday'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # Add the Month column to the df if it doesn't exist
    df['Month'] = df['Start Time'].dt.month
    # Get the max value for a count of months
    # Create lookup from months dict to get string value
    month_lookup = list(months.keys())
    common_month = month_lookup[df['Month'].value_counts().idxmax() - 1]
    common_month_value = df['Month'].value_counts().max()
    print('The most frequent month of travel is {} with {} trips'.format(common_month, common_month_value))

    # TO DO: display the most common day of week
    df['Days'] = df['Start Time'].dt.weekday_name
    common_day = df['Days'].value_counts().idxmax()
    common_day_value = df['Days'].value_counts().max()
    print('The most frequent day of travel is {} with {} trips'.format(common_day, common_day_value))

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Hour'].value_counts().idxmax()
    common_start_hour_value = df['Hour'].value_counts().max()
    print('The most frequent hour of travel is {} with {} trips'.format(common_start_hour, common_start_hour_value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # Assign the index value which will be the most common start station
    max_start_station = df['Start Station'].value_counts().idxmax()
    # Assign the max value for start station
    max_start_station_value = df['Start Station'].value_counts().max()
    print('The most common starting station is {} : {}'.format(max_start_station, max_start_station_value))

    # TO DO: display most commonly used end station
    max_end_station = df['End Station'].value_counts().idxmax()
    max_end_station_value = df['End Station'].value_counts().max()
    print('The most common ending station is {} : {}'.format(max_end_station, max_end_station_value))

    # TO DO: display most frequent combination of start station and end station trip
    common_station_combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most common start / end combination is Starting station: {} ' 
          '&  Ending Station: {}'.format(common_station_combo[0], common_station_combo[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum() / 60
    print('The total travel time for all trips is {} minutes'.format(total_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 60
    print('The mean travel time for all trips is {} minutes'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The breakdown of user types is as follows:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        get_gender_count = df['Gender'].value_counts()
        print('Reported genders counts are the following:')
        print(get_gender_count)
        unreported_gender = df['Gender'].isnull().sum()
        print('<<<< ---------- >>>>')
        print('There are {} that are not reported'.format(unreported_gender))
    except KeyError:
        print('Gender information not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        oldest_rider = int(df['Birth Year'].min())
        youngest_rider = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode())

        print('The oldest rider was born in {}, the youngest in {} and the most common year of birth amongst riders is'
              ' {}'.format(oldest_rider, youngest_rider, most_common_birth_year))
    except KeyError:
        print('Birth year information not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def show_raw_data(df):
    raw_data_view = input('Would you like to see the raw data? (y or n)')
    raw_data_view.lower().strip()
    row_count = 0
    range_set = 5
    if raw_data_view == 'y' or 'yes':
        while True:
            for row in range(range_set):
                print(df.iloc[row])
                print('<<<<< ---------------------------------------- >>>>>')

            print_more = input('Would you like to view more raw data? (y or n)')
            if print_more == 'y':
                row_count += 5
                range_set += 5
            else:
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
