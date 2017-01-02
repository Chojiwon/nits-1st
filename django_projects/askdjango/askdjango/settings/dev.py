from .common import *

import os
import raven

GIT_ROOT = os.path.join(BASE_DIR, '..', '..')  # FIXME: 프로젝트에 맞춰 수정

RAVEN_CONFIG = {
    # FIXME: 각자 설정에 맞춰 수정
    # https://docs.sentry.io/clients/python/integrations/django/
    'dsn': 'https://c1647f59f36e44f4833d5c6626695cd1:392001118d9d4e00b9dd0227bde8ede5@sentry.io/124899',
    # If you are using git, you can also automatically configure the release based on the git info.
    'release': raven.fetch_git_sha(GIT_ROOT),
}

