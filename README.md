# libgpod

libgpod is a library meant to abstract access to an iPod content. It
provides an easy to use API to retrieve the list of files and playlist
stored on an iPod, to modify them and to save them back to the iPod.

## Changes to the original project

- hopefully working Python 3 support
- switch to Meson as build system
- no HAL anymore

## Building

The library is now build with Meson.

```
meson build; cd build
ninja
# as root or set a prefix via `meson configure`
ninja install
```

If you want to test the Python code:
```
meson build; cd build
meson test python-test -v
```

## General

My fork is based on the one of Schraubischlump.
Here follows their README, see README.old for the original one.

## Readme for libgpod update/maintenance releases

Numerous fixes by me and others, seems worth a minor version update.
See the CHANGELOG.md file for recent release info and any associated
github issues, etc.

There is no HAL anymore, so you'll need to run one of the libgpod tools
to prep your device. You should have an ipod-read-sysinfo-extended tool
installed with this package, running it once will write a file under your
ipod mount point and you should be good to go.  Eg:

```
  $ ipod-read-sysinfo-extended /dev/sda /mnt/ipod
```

Make sure the device and mount point are what you want; see the file
README.SysInfo for more details.
