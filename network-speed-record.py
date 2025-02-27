# network speed recorder

import speedtest
import datetime
import psutil
import subprocess

def get_network_info():
    for interface, addrs in psutil.net_if_addrs().items():
        if interface.startswith('en'):  # Typically LAN interfaces start with 'en' on macOS
            return 'LAN', 'LAN'
        elif interface.startswith('wl'):  # Typically WiFi interfaces start with 'wl' on macOS
            try:
                ssid = subprocess.check_output(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I']).decode()
                ssid = [line.split(": ")[1] for line in ssid.split("\n") if " SSID" in line][0]
                return 'WiFi', ssid
            except Exception as e:
                return 'WiFi', 'Unknown'

    return 'Unknown', 'Unknown'

def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    network_type, network_id = get_network_info()

    with open("speed_log.csv", "a") as f:
        f.write(f"{timestamp},{download_speed:.2f},{upload_speed:.2f},{network_type},{network_id}\n")

if __name__ == "__main__":
    run_speedtest()