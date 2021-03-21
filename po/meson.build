i18n = import('i18n')
add_project_arguments('-DGETTEXT_PACKAGE="gpod"', language: 'c')
i18n.gettext(meson.project_name(),
    args: ['--keyword=N_', '--directory=' + meson.source_root()]
)
