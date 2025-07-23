import os

DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def return_version_from_file(_file):
    """Retun version from file"""
    if os.path.exists(_file):
        version = (open(_file, 'rb').read()).decode("utf-8")
        if version:
            return version
    return None


def project_version(request):
    """ Read project version from file"""
    version = return_version_from_file(
        os.path.join(
            DJANGO_ROOT, 'kartoza_geonode', 'version', 'version.txt'
        )
    )
    commit = return_version_from_file(
        os.path.join(
            DJANGO_ROOT, 'kartoza_geonode', 'version', 'commit.txt'
        )
    )

    if version:
        return {
            'PROJECT_VERSION': {
                'version': version,
                'commit': commit
            }
        }
    return {}
