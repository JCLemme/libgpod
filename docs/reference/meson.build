# workaround for https://github.com/mesonbuild/meson/issues/8315
gtkdoc = find_program('gtkdoc-scan', required: get_option('doc'))
if gtkdoc.found()
  doc_conf_data = configuration_data()
  doc_conf_data.set('PACKAGE_VERSION', meson.project_version())
  version_xml = configure_file(input: 'version.xml.in',
                               output: 'version.xml',
                               configuration: doc_conf_data)
  config_inc = include_directories('.')

  gnome.gtkdoc('libgpod',
      main_xml: 'libgpod-docs.xml',
      content_files: version_xml,
      install: true,
      include_directories: config_inc,
      src_dir: lib_src_dir,
      scan_args: ['--deprecated-guards="LIBGPOD_DISABLE_DEPRECATED"'])
endif
