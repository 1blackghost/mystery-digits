import time

def get_current_time():
    """
    Returns the current time in seconds using time.time().
    """
    return time.time()

def calculate_duration(start_time, end_time):
    """
    Calculates the duration between start_time and end_time.

    Parameters:
    - start_time: Start time in seconds.
    - end_time: End time in seconds.

    Returns:
    A formatted string representing the duration in the format "0h 0m 0s".
    """
    duration_seconds = end_time - start_time
    return duration_seconds


def convert(duration):
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)

    duration_string = "{:.0f}h {:.0f}m {:.0f}s".format(hours, minutes, seconds)
    return duration_string

'''
# Example usage:
start_time = get_current_time()

time.sleep(2)

end_time = get_current_time()

duration = calculate_duration(start_time, end_time)
duration=convert(duration)
print("Duration:", duration)
'''

