if add_languages('cs', required: get_option('mono'))
    glib_sharp = dependency('glib-sharp-2.0')
    gtk_sharp = dependency('gtk-sharp-2.0')
    library('libgpod-sharp',
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
endif
