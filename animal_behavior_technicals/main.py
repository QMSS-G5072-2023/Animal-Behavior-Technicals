# main.py
import utils

def main():
    status = 'A'
    result = utils.is_status_accurate(status)

    if result:
        print(f"The eobs_status is '{status}'.")
    else:
        print(f"The eobs_status is not '{status}'.")

if __name__ == "__main__":
    main()
