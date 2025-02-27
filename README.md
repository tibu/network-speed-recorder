# Network Speed Recorder

Check network speed and record it in a speed_log.csv CSV file on a Mac

Setup of the file:

timestamp,download,upload,connection type,SSID name

Example:
2025-02-27 10:21:19,64.18,38.32,LAN,LAN

## Installation

brew install speedtest-cli
uv pip install -r requirements.txt

crontab -e
*/5 * * * * cd /Users/tiborszentmarjay/Documents/git/network-speed-recorder && /opt/homebrew/bin/uv run network-speed-record.py >> /Users/tiborszentmarjay/Documents/git/network-speed-recorder/error.log 2>&1


## Development

add dependencies to the requirements  file: uv pip freeze > requirements.txt
