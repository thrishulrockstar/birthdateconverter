from datetime import datetime, timedelta


dob = input('Enter your date of birth (YYYY-MM-DD): ')


dob = datetime.strptime(dob, '%Y-%m-%d')

now = datetime.now()


difference = now - dob


seconds = difference.total_seconds()


print(f'Number of seconds since your date of birth: {seconds:.0f}')