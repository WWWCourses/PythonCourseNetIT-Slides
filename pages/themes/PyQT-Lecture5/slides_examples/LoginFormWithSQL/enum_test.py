from enum import Enum


class ButtonRole(Enum):
    DEFAULT = 'default'
    PRIMARY = 'primary'
    SUCCESS = 'success'
    DANGER = 'danger'
    WARNING = 'warning'
    INFO = 'info'

COLOR_SCHEMES = {
    'primary': ('#007BFF', '#0056b3'),
    'success': ('#28a745', '#218838'),
    'danger': ('#DC3545', '#c82333'),
    'warning': ('#FFC107', '#e0a800'),
    'info': ('#17a2b8', '#138496'),
    'default': ('#6C757D', '#495057'),
}

def apply_stylesheet(role=ButtonRole.DEFAULT):
    base_color, hover_color = COLOR_SCHEMES.get(
        role.value, COLOR_SCHEMES['default']
    )
    print(f'base_color: {base_color}', f'role:{str(role)}')

apply_stylesheet(ButtonRole.DANGER)
