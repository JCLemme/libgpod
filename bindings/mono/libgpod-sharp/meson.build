glib_sharp = dependency('glib-sharp-2.0')
gtk_sharp = dependency('gtk-sharp-2.0')

fs = import('fs')

lib_name = fs.name(libgpod.full_path())
sharp_conf_data = configuration_data()
sharp_conf_data.set('DLNAME', lib_name)
sharp_config = configure_file(input: 'libgpod-sharp.dll.config.in',
                              output: 'libgpod-sharp.dll.config',
                              install: true,
                              install_dir: get_option('libdir'),
                              configuration: sharp_conf_data)

libgpod_sharp = library('libgpod-sharp',
    'Artwork.cs',
    'AssemblyInfo.cs',
    'Chapter.cs',
    'ChapterData.cs',
    'Device.cs',
    'GPodBase.cs',
    'GPodList.cs',
    'IpodInfo.cs',
    'ITDB.cs',
    'PhotoAlbum.cs',
    'PhotoDB.cs',
    'Playlist.cs',
    'Thumbnail.cs',
    'Track.cs',
    install: true,
    cs_args: ['-unsafe+'],
    dependencies: [glib_sharp, gtk_sharp])

pkg = import('pkgconfig')
libs = libgpod_sharp
pkg.generate(libraries: libgpod_sharp,
             version: '0.1',
             subdirs: '',
             name: libgpod_sharp.name(),
             filebase: libgpod_sharp.name(),
             description: 'C# bindings for libgpod.')
