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

if udev.found() and libxml.found()
    setinfo_files = files(
        'udev-backend.c',
        'generic-callout.c',
        'itdb-syslog.c',
        lib_src_dir / 'itdb_sysinfo_extended_parser.c',
        lib_src_dir / 'itdb_plist.c'
    )
    if sgutils.found()
        setinfo_files += files('ipod-scsi.c')
    endif

    if libusb.found()
        setinfo_files += files('ipod-usb.c')
    endif

    executable('ipod-set-info', setinfo_files,
        include_directories: configuration_inc,
        dependencies: sysinfo_deps + [libxml, gobject])

    dir_system_udev = get_option('prefix') / 'lib' / 'udev'
    dir_udev = get_option('udev-dir')
    if dir_udev == ''
        dir_udev = dir_system_udev
    endif
    dir_udev_rules    = dir_udev / 'rules.d'
    install_data('90-libgpod.rules', install_dir : dir_udev_rules)
endif

if sgutils.found()
    time_sync_files = files(
        'ipod-time-sync.c',
        'ipod-scsi.c',
        'itdb-syslog.c',
    )

    executable('ipod-time-sync', time_sync_files,
        include_directories: configuration_inc,
        dependencies: [glib, sgutils])
endif
