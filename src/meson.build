src_files = files(
    'db-artwork-debug.c',
    'db-artwork-parser.c',
    'db-artwork-writer.c',
    'db-image-parser.c',
    'db-parse-context.c',
    'itdb_artwork.c',
    'itdb_chapterdata.c',
    'itdb_device.c',
    'itdb_hash58.c',
    'itdb_hash72.c',
    'itdb_hashAB.c',
    'itdb_iphone.c',
    'itdb_itunesdb.c',
    'itdb_photoalbum.c',
    'itdb_playlist.c',
    'itdb_plist.c',
    'itdb_sqlite.c',
    'itdb_sysinfo_extended_parser.c',
    'itdb_thumb.c',
    'itdb_track.c',
    'itdb_tzinfo.c',
    'itdb_zlib.c',
    'ithumb-writer.c',
    'pixmaps.c',
    'rijndael.c',
)

header_files = files(
    'db-artwork-debug.h',
    'db-artwork-parser.h',
    'db-image-parser.h',
    'db-itunes-parser.h',
    'db-parse-context.h',
    'itdb_device.h',
    'itdb_endianness.h',
    'itdb.h',
    'itdb_plist.h',
    'itdb_private.h',
    'itdb_sqlite_queries.h',
    'itdb_sysinfo_extended_parser.h',
    'itdb_thumb.h',
    'itdb_tzinfo_data.h',
    'itdb_zlib.h',
    'pixmaps.h',
    'rijndael.h',
)

libgpod = library(meson.project_name(), src_files,
    c_args: '-DHAVE_CONFIG_H=1',
    include_directories: configuration_inc,
    dependencies: [glib, gdk_pixbuf, libxml, m_dep, gobject, sqlite, plist, gmodule, zlib],
    version: abi_version,
    install: true
)

lib_src_dir = meson.current_source_dir()
lib_inc_dir = include_directories('.')
libgpod_dep = declare_dependency(link_with: libgpod, include_directories: lib_inc_dir)

install_include_dir = meson.project_name() + '-' + api_version / 'gpod'
install_headers('itdb.h', subdir: install_include_dir)

pkg = import('pkgconfig')
pkg.generate(libraries: libgpod,
             version: api_version,
             subdirs: install_include_dir,
             name: libgpod.name(),
             filebase: libgpod.name(),
             description: 'Library to access iPod content.')

