def dd_to_dms(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes_float = (decimal_degrees - degrees) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60
    return degrees, minutes, seconds

# Example usage
decimal_degrees_str = input("נא להזין מספר עשרוני: ")
decimal_degrees = float(decimal_degrees_str)
degrees, minutes, seconds = dd_to_dms(decimal_degrees)
print(f"{degrees} degrees {minutes} minutes {seconds:.2f} seconds")




