def is_status_accurate(eobs_status):
    """Check if eobs_status is accurate."""
    return eobs_status == 'A'

def is_high_temperature(eobs_temperature):
    return eobs_temperature > 35

# Example usage:
temperature = 36
result = is_high_temperature(temperature)

if result:
    print(f"The temperature ({temperature}°C) is high.")
else:
    print(f"The temperature ({temperature}°C) is not high.")

def is_low_temperature(eobs_temperature):
    return eobs_temperature < 3

# Example usage:
temperature = 1
result = is_low_temperature(temperature)

if result:
    print(f"The temperature ({temperature}°C) is low.")
else:
    print(f"The temperature ({temperature}°C) is not low.")

def get_climate_zone(location_lat):
    if -30 <= location_lat <= 30:
        return 'Tropical'
    elif -60 <= location_lat < -30 or 30 < location_lat <= 60:
        return 'Temperate'
    elif -90 <= location_lat < -60 or 60 < location_lat <= 90:
        return 'Polar'
    else:
        return 'Unknown'

# Example usage:
latitude = 25 
climate_zone = get_climate_zone(latitude)
print(f"The climate zone for latitude {latitude} is: {climate_zone}")
