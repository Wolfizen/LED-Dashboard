# LED-Dashboard

A web server to control an instance of [rgbd](https://github.com/Wolfizen/rgbd). Supports brightness control, power, and profile swapping.

Honestly this software is kinda hastily done and this readme is definitely incomplete. I don't claim this software will be ready to go out of the box. Good luck!

## Installing

* Clone the repo.
* Install the required python3 pip packages to either a virtual environment, your user environment, or the system environment.
* Copy the provided systemd unit to `.local/share/systemd/user/LED-Dashboard.service` for a user unit (preferred) or `/etc/systemd/system/LED-Dashboard.service`. for a system unit.
* Edit the unit file to reflect the code location and python package installation location.
* Enable the unit for autostart.

## Using

The app is Django-based and uses a simple sqlite DB for its data storage. The only things it stores in the DB are the current profile, brightness, and power status.

Configuration is done by editing `settings.py`. The options are at the bottom.
