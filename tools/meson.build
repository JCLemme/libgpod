sysinfo_files = files('read-sysinfoextended.c', 'itdb-syslog.c')
sysinfo_deps = [glib, libgpod_dep]
if sgutils.found()
    sysinfo_files += files('ipod-scsi.c')
    sysinfo_deps += [sgutils]
endif
if libidev.found()
    sysinfo_files += files('ipod-lockdown.c')
endif
if libusb.found()
    sysinfo_files += files('ipod-usb.c')
    sysinfo_deps += [libusb]
endif

executable('ipod-read-sysinfo-extended', sysinfo_files,
    include_directories: configuration_inc,
    dependencies: sysinfo_deps)

common_sources = files('generic-callout.c', 'itdb-syslog.c')

executable('ipod-set-info', common_sources + ['udev-backend.c'],
    include_directories: configuration_inc,
    dependencies: [glib, libgpod_dep])
