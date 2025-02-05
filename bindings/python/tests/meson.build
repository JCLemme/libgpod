python_path = 'PYTHONPATH=' + ':'.join([gpod_py_dir])
resource_dir = 'RESOURCE_DIR=' + meson.current_source_dir() / 'resources'
# workaround, may fail, see https://github.com/mesonbuild/meson/pull/8487
gpod_init = 'GPOD_INIT=@0@'.format(init_py.full_path())
message(gpod_init)
test('python-test',
     py3_inst,
     args: [files('tests.py')],
     env: [python_path, resource_dir, gpod_init],
     depends: gpod_mod,
)
