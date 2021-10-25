""""
scans wifi... for use when walking around with picar
"""
import os
import argparse
from time import gmtime, strftime, sleep


def write_file(essid_arr: list, file_name: str):
    with open(file_name, "w") as file_handle:
        for essid in essid_arr:
            file_handle.write(f"{essid}\n")


def main():
    interface = args.interface
    delay = args.delay

    scans = 20
    while scans:
        print(f"scanning wifi interface {interface}\n")
        essid_arr = (
            os.popen(f"sudo iwlist {interface} scan | grep  ESSID | sort -u")
            .read()
            .split("\n")
        )
        if len(essid_arr) > 1:
            time_stamp = strftime("%Y-%m-%d %H:%M:%S", gmtime()).replace(" ", "-")
            essid_arr.append(time_stamp)
            sleep(delay)
            write_file(
                essid_arr,
                f"/home/pi/cs437-iot-lab-3/tests/essid-found-time-{time_stamp}.json",
            )
            scans -= 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--interface",
        type=str,
        required=False,
        help="wireless interface name",
        default="wlan0",
    )
    parser.add_argument(
        "--delay",
        type=int,
        required=False,
        help="delay in seconds between each scan",
        default=10,
    )
    args = parser.parse_args()
    main()
