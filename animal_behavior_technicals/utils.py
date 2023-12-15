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
location_lat = 25 
climate_zone = get_climate_zone(location_lat)
print(f"The climate zone for latitude {location_lat} is: {climate_zone}")


def get_region(location_long):
    if location_long < 0:
        return 'West'
    elif location_long >= 0:
        return 'East'
    else:
        return 'Unknown'

# Example usage:
location_long = -80  # Replace with the actual longitude value
region = get_region(location_long)
print(f"The region for longitude {location_long} is: {region}")

def get_sensor_type(sensor_type_id):
    if sensor_type_id == 653:
        return 'GPS'
    elif sensor_type_id == 2365683:
        return 'Acceleration'
    else:
        return 'Unknown'

# Example usage:
sensor_id_1 = 653
sensor_type_1 = get_sensor_type(sensor_id_1)
print(f"Sensor ID {sensor_id_1} corresponds to: {sensor_type_1}")

sensor_id_2 = 2365683
sensor_type_2 = get_sensor_type(sensor_id_2)
print(f"Sensor ID {sensor_id_2} corresponds to: {sensor_type_2}")

unknown_sensor_id = 12345
unknown_sensor_type = get_sensor_type(unknown_sensor_id)
print(f"Sensor ID {unknown_sensor_id} corresponds to: {unknown_sensor_type}")


