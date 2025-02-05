swig = find_program('swig', required: get_option('python'))
pygobject = dependency('pygobject-3.0', required: get_option('python'))

py3_mod = import('python')
py3_inst = py3_mod.find_installation('python3', modules: ['mutagen'])

if swig.found() and py3_inst.found()
  #py_module = get_option('prefix') + py3_inst.get_path('purelib') / meson.project_name()
    py_module = py3_inst.get_path('purelib') / meson.project_name()

    python_conf_data = {'PACKAGE_VERSION': meson.project_version(),
                        'CONFIG_H': '@0@'.format(config_h.full_path()),
                        'ITDB_H': lib_src_dir / 'itdb.h'}
    gpod_i = configure_file(input: 'gpod.i.in',
        output: 'gpod.i',
        configuration: python_conf_data)

    gpod_swig = custom_target('gpod_c',
        input: gpod_i,
        output: ['gpod_wrap.c', 'gpod.py'],
        command: [swig, '-python', '-py3', '-Wall', '-Wextra',
                  '-I@CURRENT_SOURCE_DIR@',
                  '-MMD', '-MF', '@DEPFILE@',
                  '@INPUT@'],
        install: true,
        install_dir: [false, py_module],
        depend_files: config_h,
        depfile: 'gpod.c.dep')
    gpod_wrap_c = gpod_swig[0]
    gpod_py = gpod_swig[1]

    gpod_mod = py3_inst.extension_module('_gpod',
        gpod_wrap_c,
        install: true,
        subdir: py_module,
        include_directories: configuration_inc,
        dependencies: [libgpod_dep, py3_inst.dependency(), glib, gdk_pixbuf, pygobject]
    )
    init_py = files('__init__.py')[0]
    install_data(init_py, 'ipod.py', 'gtkpod.py', install_dir: py_module)
    gpod_py_dir = meson.current_build_dir()

    if get_option('test')
        subdir('tests')
    endif
endif
