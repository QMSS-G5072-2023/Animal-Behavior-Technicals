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
    location_latitude = 25
    climate_zone = utils.get_climate_zone(location_latitude)
    print(f"The climate zone for latitude {location_latitude} is: {climate_zone}")

if __name__ == "__main__":
    main()
