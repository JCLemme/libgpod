if gdk_pixbuf.found()
  executable('test-thumbnails',
    'test-covers.c',
    dependencies: libgpod_dep)

  executable('test-write-thumbnails',
    'test-write-covers.c',
    dependencies: libgpod_dep)

  executable('test-photos',
    'test-photos.c',
    dependencies: libgpod_dep)

  executable('get-timezone',
    'get-timezone.c',
    dependencies: libgpod_dep)
endif

if taglib.found()
  # we need C++ for this test cases
  if add_languages('cpp', native: false, required: get_option('taglib')) # TODO: verify use of "native" flag
    executable('test-cp',
      'test-cp.cc',
      dependencies: [taglib, libgpod_dep])
    executable('test-rebuild-db',
      'test-rebuild-db.cc',
      dependencies: [taglib, libgpod_dep])
  endif
endif

executable('test-init-ipod',
  'test-init-ipod.c',
  dependencies: libgpod_dep)

executable('test-itdb',
  'itdb_main.c',
  dependencies: libgpod_dep)

executable('test-ls',
  'test-ls.c',
  dependencies: libgpod_dep)

executable('test-firewire-id',
  'test-fw-id.c',
  dependencies: libgpod_dep)

executable('test-sysinfo-extended-parsing',
  'test-sysinfo-extended-parsing.c',
  sysinfo_test_files,
  include_directories: lib_inc_dir,
  dependencies: libgpod_dep)


