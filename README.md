# Orange Pi used as Server for Telegram, Discord, and Twitch Bots

Tested on Orange Pi Zero 2W 2GB RAM.

<img src="pics/logo.png" alt="Board Image" style="max-width: 10%; height: auto;">

<img src="pics/board.png" alt="Board Image" style="max-width: 33%; height: auto;">

## Initial Setup

1. Download the OS iso (I used the Raspberry Pi OS opizero2w Desktop version from [GitHub](https://github.com/leeboby/raspberry-pi-os-images));
2. Prepare a microSD card with the OS image (using [Balena Etcher](https://etcher.balena.io/)) and insert it into the board;
3. Connect the board to a monitor, keyboard, and mouse and power it up;
4. Go through the initial setup.

## Fix the disk space

```bash
df -h
```

If the disk space is not correct (you have a 32GB cards but it only shows 8GB), you need to expand the filesystem:

```bash
sudo raspi-config
```

Then go to **Advanced** -> **Expand Filesystem**

Reboot the system:

```bash
sudo reboot
```

Check the disk space again:

```bash
df -h
```
