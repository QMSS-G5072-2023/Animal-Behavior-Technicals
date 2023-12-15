import utils

def main():
    # Check if eobs_status is accurate
    eobs_status = 'A'
    result_status = utils.is_status_accurate(eobs_status)

    if result_status:
        print(f"The eobs_status is accurate.")
    else:
        print(f"The eobs_status is not accurate.")

    # Check if temperature is high
    eobs_temperature_high = 36
    result_high_temperature = utils.is_high_temperature(eobs_temperature_high)

    if result_high_temperature:
        print(f"The temperature ({eobs_temperature_high}°C) is high.")
    else:
        print(f"The temperature ({eobs_temperature_high}°C) is not high.")

    # Check if temperature is low
    eobs_temperature_low = 1
    result_low_temperature = utils.is_low_temperature(eobs_temperature_low)

    if result_low_temperature:
        print(f"The temperature ({eobs_temperature_low}°C) is low.")
    else:
        print(f"The temperature ({eobs_temperature_low}°C) is not low.")

    # Get climate zone for a specific location
    location_lat = 25
    climate_zone = utils.get_climate_zone(location_lat)
    print(f"The climate zone for latitude {location_lat} is: {climate_zone}")

    location_long = -80
    region = utils.get_region(location_long)
    print(f"The region for longitude {location_long} is: {region}")

    # Example 4: Sensor Type
    sensor_id_1 = 653
    sensor_type_1 = utils.get_sensor_type(sensor_id_1)
    print(f"Sensor ID {sensor_id_1} corresponds to: {sensor_type_1}")

    sensor_id_2 = 2365683
    sensor_type_2 = utils.get_sensor_type(sensor_id_2)
    print(f"Sensor ID {sensor_id_2} corresponds to: {sensor_type_2}")

if __name__ == "__main__":
    main()
