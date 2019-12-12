import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



<<<<<<< HEAD
MONTHS = ['all','January', 'February', 'March', 'April', 'May', 'June']
=======
MONTHS = ['all','January', 'February', 'March', 'April', 'May', 'June']
>>>>>>> refactoring



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        city = input('Select a city by typing its name : (Chicago) - (NewYorkCity) - (Washington)\n')
        if city.lower() in ['chicago', 'newyorkcity','washington']:
            break
            print("Wrong Entry!")
            continue
        
       
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while 1:
     month = input('\nSelect a month by typing its name : (January) - (February) - (March) - (April) - (May) - (June)\n')        
     if month.lower() in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            break
            print("Wrong Entry!")



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
        day = input('\nSelect a day by typing its name :\n(Saturday) - (Sunday) - (Munday) (Tuesday) (Wedendsay) (Thursday) (Friday)\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']:
            break
            print("wrong entry!")

    
    month=month.lower()
    day=day.lower()
    city = CITY_DATA[city.lower()]
    print('-'*40)
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
    df = pd.read_csv(city)
    
    #read the data
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    #----------------day and month saved-----------------------------
    
   #  checkDay = day.lower()
   #  checkMonth = month.lower()
    
        #Pandas DataFrame containing city data filtered by month and day
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
        
    if month != 'all': 
        month =  MONTHS.index(month)
        # to get the index    
        df = df.loc[df['month'] == month]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mostCommonMonth = df['month'].mode()[0]
    print("\nMost common month is : ",mostCommonMonth)
    
    # TO DO: display the most common day of week
    mostCommonDay = df['day_of_week'].mode()[0]
    print("\nMost common day is : ",mostCommonDay)
    
    # TO DO: display the most common start hour
    mostCommonHour = df['Start Time'].mode()[0]
    print("\nMost common hour is : ",mostCommonHour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mostCommonStartStation = df['Start Station'].mode()[0]
    print("\nMost common used start statio is : ",mostCommonStartStation)
    
    
    # TO DO: display most commonly used end station
    mostCommonEndStation = df['End Station'].mode()[0]
    print("\nMost common used end statio is : ",mostCommonEndStation)


    # TO DO: display most frequent combination of start station and end station trip
    # df['Start To End Combination'] = df['Start Station'] +''+ df['End Station']
    mostCommonStartEndCombination = str((df['Start Station'] +''+ df['End Station']).mode()[0])
    print("\nMost combination of start station and end station trip is : ",mostCommonStartEndCombination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTimeSum = int(df['Trip Duration'].sum())
    print("\nTotal Travel Time : ",totalTimeSum)


    # TO DO: display mean travel time
    totalTimeMean= df['Trip Duration'].mean()
    print("\nTotal Travel Time : ",totalTimeMean)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    UserTypeCount = df['User Type'].value_counts()
    print("\n number of user types are : ",UserTypeCount)


    # TO DO: Display counts of gender
    if 'Gender' not in df :
        print("There exist no gender (Nan)")
    else:
            GenderCount = df['Gender'].value_counts()
            print("\nNumber of Gender is : ", GenderCount)
         
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print("There exist no BirthYear (Nan)")
    else:      
        MostCommonYearOfBirth = df['Birth Year'].value_counts().idxmax()
        print("\nThe most common year of birth is : ",MostCommonYearOfBirth)
        MostRecentYearOfBirth = df['Birth Year'].max()
        print("\nThe most recent year of birth is : ",MostRecentYearOfBirth)
        EarliestYearOfBirth = df['Birth Year'].min()
        print("\nThe earliest year of birth is : ",EarliestYearOfBirth)
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_point = 0
    position = 5
    display = input("Do you want to see the raw data? \nEnter (yes) or (no) ")
    if display.lower() == 'yes':
        while position <= df.shape[0] - 1:
            print(df.iloc[start_loc:end_loc,:])
            start_point=start_point+5
            position=position+5
            
            displayEnd = input("If you want to stop enter (stop) otherwise enter (no): ")
            if displayEnd.lower() == 'stop':
                break

            def display_data(df):
    start_point = 0
    position = 5
    display = input("Do you want to see the raw data? \nEnter (yes) or (no) ")
    if display.lower() == 'yes':
        while position <= df.shape[0] - 1:
            print(df.iloc[start_loc:end_loc,:])
            start_point=start_point+5
            position=position+5
            
            displayEnd = input("If you want to stop enter (stop) otherwise enter (no): ")
            if displayEnd.lower() == 'stop':
                break
            


            
            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
