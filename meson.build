project('gpod', 'c',
  version : '0.8.3',
  default_options : ['warning_level=3',
                     'c_std=c11',
                     'buildtype=debugoptimized'])

# ABI versioning: <major>.<minor>.<micro>
# major: ABI incompatible change
# minor: ABI compatible change (addition)
# micro: change that does not affect the ABI
abi_version = '4.3.2'
# API versioning: <major>.<minor>
# major: API incompatible change
# minor: API compatible change (addition)
api_version = '1.0'

gnome = import('gnome')

glib = dependency('glib-2.0')
gobject = dependency('gobject-2.0')
sqlite = dependency('sqlite3')
plist = dependency('libplist-2.0')
gmodule = dependency('gmodule-2.0')
zlib = dependency('zlib')
udev = dependency('libudev', required: get_option('udev'))

compiler = meson.get_compiler('c')
sgutils = compiler.find_library('libsgutils', required: get_option('sgutils'))

gdk_pixbuf = dependency('gdk-pixbuf-2.0', required: get_option('artwork-db'))
libxml = dependency('libxml-2.0', required: get_option('sysinfo'))
libusb = dependency('libusb-1.0', required: get_option('sysinfo-ng'))
libidev = dependency('libimobiledevice-1.0', required: get_option('ios'))

if get_option('test')
  taglib = dependency('taglib', required: get_option('taglib'))
endif

cc = meson.get_compiler('c')
m_dep = cc.find_library('m', required : false)

conf_data = configuration_data()
if gdk_pixbuf.found()
  conf_data.set('HAVE_GDKPIXBUF', 1)
else
  conf_data.set('HAVE_GDKPIXBUF', false)
endif

if gdk_pixbuf.found()
  conf_data.set('HAVE_GDKPIXBUF', 1)
else
  conf_data.set('HAVE_GDKPIXBUF', false)
endif

if libxml.found()
  conf_data.set('HAVE_LIBXML', 1)
else
  conf_data.set('HAVE_LIBXML', false)
endif

if libusb.found()
  conf_data.set('HAVE_LIBUSB', 1)
else
  conf_data.set('HAVE_LIBUSB', false)
endif

conf_data.set10('HAVE_G_CHECKSUM_RESET', true)
conf_data.set10('HAVE_G_INT64_EQUAL', true)
conf_data.set10('HAVE_G_INT64_HASH', true)
conf_data.set10('HAVE_G_MAPPED_FILE_UNREF', true)
conf_data.set10('HAVE_LOCALTIME_R', true)

if sgutils.found()
  conf_data.set('HAVE_SGUTILS', 1)
else
  conf_data.set('HAVE_SGUTILS', false)
endif

conf_data.set10('HAVE_STRUCT_TM_TM_GMTOFF', true)
conf_data.set10('HAVE_UNISTD_H', true)
conf_data.set10('HAVE_HAL', false) # HAL is not supported anymore
conf_data.set10('_GNU_SOURCE', true)
conf_data.set_quoted('TMPMOUNTDIR', '/tmp/ipod')
config_h = configure_file(output: 'config.h',
                          configuration: conf_data)
configuration_inc = include_directories('.')

# These extra flags are copied from Archlinux's build script for the upstream libgpod.
add_global_arguments('-DLIBGPOD_BLOB_DIR="/usr/lib64/libgpod"', '-Wno-incompatible-pointer-types', '-Wno-implicit-int', '-Wno-int-conversion', language : 'c')

subdir('po')
subdir('src')
subdir('docs')
subdir('tools')
subdir('bindings')
if get_option('test')
  subdir('tests')
endif
