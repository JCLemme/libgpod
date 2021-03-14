swig = find_program('swig', required: get_option('python'))
pygobject = dependency('pygobject-3.0', required: get_option('python'))

py3_mod = import('python')
py3_inst = py3_mod.find_installation('python3')

if swig.found() and py3_inst.found()
    python_conf_data = {'PACKAGE_VERSION': meson.project_version(),
                        'CONFIG_H': meson.source_root() / '@0@'.format(config_h),
                        'ITDB_H': lib_src_dir / 'itdb.h'}
    gpod_i = configure_file(input: 'gpod.i.in',
                            output: 'gpod.i',
                            configuration: python_conf_data)

    gpod_c = custom_target('gpod_c',
                           input: gpod_i,
                           output: 'gpod.c',
                           command: [swig, '-python', '-py3', '-Wall', '-Wextra',
                                     '-o', '@OUTPUT@',
                                     '-I@CURRENT_SOURCE_DIR@',
                                     '-MMD', '-MF', '@DEPFILE@',
                                     '@INPUT@'],
                           depfile: 'gpod.c.dep')

    gpod_mod = py3_inst.extension_module('gpod',
        gpod_c,
        include_directories: configuration_inc,
        dependencies: [libgpod_dep, py3_inst.dependency(), glib, gdk_pixbuf, pygobject]
    )
endif
