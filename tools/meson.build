# compilation units that depend on libraries
disabled_obj = [[], [], [disabler()]]

if libxml.found() and libidev.found()
    il_deps = [libxml, libidev]
    ipod_lockdown = [files('ipod-lockdown.c'), il_deps, il_deps]
else
    ipod_lockdown = disabled_obj
endif

if sgutils.found()
    ipod_scsi = [files('ipod-scsi.c'), [sgutils], [sgutils]]
else
    ipod_scsi = disabled_obj
endif

if libusb.found()
    ipod_usb = [files('ipod-usb.c'), [libusb], [libusb]]
else
    ipod_usb = disabled_obj
endif

if libxml.found()
    itdb_plist = [files(lib_src_dir / 'itdb_plist.c'), [libxml], [libxml]]
else
    itdb_plist = disabled_obj
endif

# actual tools
tool_deps = [glib, libgpod_dep]

executable('ipod-read-sysinfo-extended',
    'read-sysinfoextended.c', 'itdb-syslog.c',
    ipod_lockdown[0],
    ipod_scsi[0],
    ipod_usb[0],
    install: true,
    include_directories: configuration_inc,
    dependencies: [tool_deps,
        ipod_lockdown[1], ipod_scsi[1], ipod_usb[1]])

if udev.found()
    ipod_setinfo_files = files(
        'udev-backend.c',
        'generic-callout.c',
        'itdb-syslog.c',
        lib_src_dir / 'itdb_sysinfo_extended_parser.c') + [
        itdb_plist[0],
        ipod_scsi[0],
        ipod_usb[0],
    ]
    dir_system_udev = get_option('prefix') / 'lib' / 'udev'
    dir_udev = get_option('udev-dir')
    if dir_udev == ''
        dir_udev = dir_system_udev
    endif

    executable('ipod-set-info', ipod_setinfo_files,
        install: true,
        install_dir: dir_udev,
        include_directories: configuration_inc,
        dependencies: [tool_deps, gobject,
            itdb_plist[2], ipod_scsi[1], ipod_usb[1]])

    iphone_setinfo_files = files(
        'iphone-callout.c',
        'itdb-syslog.c') + ipod_lockdown[0]

    executable('iphone-set-info', iphone_setinfo_files,
        install: true,
        install_dir: dir_udev,
        include_directories: configuration_inc,
        dependencies: [tool_deps, libxml, ipod_lockdown[2]])

    dir_udev_rules    = dir_udev / 'rules.d'
    install_data('90-libgpod.rules', install_dir : dir_udev_rules)
endif

time_sync_files = files(
    'ipod-time-sync.c',
    'itdb-syslog.c') + [ipod_scsi[0]]

executable('ipod-time-sync', time_sync_files,
    install: true,
    include_directories: configuration_inc,
    dependencies: [glib, ipod_scsi[2]])
