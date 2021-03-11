project('gpod', 'c',
  version : '0.8.3',
  default_options : ['warning_level=3',
                     'c_std=c11',
                     'buildtype=debugoptimized'])

gnome = import('gnome')

glib = dependency('glib-2.0')
gobject = dependency('gobject-2.0')
sqlite = dependency('sqlite3')
plist = dependency('libplist')
gmodule = dependency('gmodule-2.0')
zlib = dependency('zlib')
udev = dependency('libudev', required: get_option('udev'))

compiler = meson.get_compiler('c')
sgutils = compiler.find_library('libsgutils', required: get_option('sgutils'))

gdk_pixbuf = dependency('gdk-pixbuf-2.0', required: get_option('artwork-db'))
libxml = dependency('libxml-2.0', required: get_option('sysinfo'))
libusb = dependency('libusb-1.0', required: get_option('sysinfo-ng'))
libidev = dependency('libimobiledevice-1.0', required: get_option('ios'))

cc = meson.get_compiler('c')
m_dep = cc.find_library('m', required : false)

conf_data = configuration_data()
conf_data.set_quoted('GETTEXT_PACKAGE', 'libgpod')

conf_data.set10('HAVE_GDKPIXBUF', gdk_pixbuf.found())
conf_data.set10('HAVE_LIBXML', libxml.found())
conf_data.set10('HAVE_LIBUSB', libusb.found())

conf_data.set10('HAVE_G_CHECKSUM_RESET', true)
conf_data.set10('HAVE_G_INT64_EQUAL', true)
conf_data.set10('HAVE_G_INT64_HASH', true)
conf_data.set10('HAVE_G_MAPPED_FILE_UNREF', true)
conf_data.set10('HAVE_LOCALTIME_R', true)
conf_data.set10('HAVE_SGUTILS', sgutils.found())
conf_data.set10('HAVE_STRUCT_TM_TM_GMTOFF', true)
conf_data.set10('HAVE_UNISTD_H', true)
conf_data.set10('HAVE_HAL', false) # HAL is not supported anymore
conf_data.set10('_GNU_SOURCE', true)
conf_data.set_quoted('TMPMOUNTDIR', '/tmp/ipod')
configure_file(output : 'config.h',
               configuration : conf_data)
configuration_inc = include_directories('.')
add_global_arguments('-DHAVE_CONFIG_H=1', language : 'c')
add_global_arguments('-DLIBGPOD_BLOB_DIR="/usr/lib64/libgpod"', language : 'c')

subdir('src')
subdir('docs')
subdir('tools')
