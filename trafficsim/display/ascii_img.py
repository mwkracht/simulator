"""Module contains ascii art representation for traffic signal states."""

__all__ = (
    'RED_LIGHT',
    'YELLOW_LIGHT',
    'GREEN_LIGHT'
)


RED_LIGHT = r"""
                ##
               _[]_
              [____]
          .----'  '----.
      .===|    .==.    |===.
      \   |   /####\   |   /
      /   |   \####/   |   \
      '===|    `""`    |==='
      .===|    .==.    |===.
      \   |   /    \   |   /
      /   |   \    /   |   \
      '===|    `""`    |==='
      .===|    .==.    |===.
      \   |   /    \   |   /
      /   |   \    /   |   \
      '===|    `""`    |==='
          '--.______.--'
"""


YELLOW_LIGHT = r"""
                ##
               _[]_
              [____]
          .----'  '----.
      .===|    .==.    |===.
      \   |   /    \   |   /
      /   |   \    /   |   \
      '===|    `""`    |==='
      .===|    .==.    |===.
      \   |   /::::\   |   /
      /   |   \::::/   |   \
      '===|    `""`    |==='
      .===|    .==.    |===.
      \   |   /    \   |   /
      /   |   \    /   |   \
      '===|    `""`    |==='
          '--.______.--'
"""


GREEN_LIGHT = r"""
                ##
               _[]_
              [____]
          .----'  '----.
      .===|    .==.    |===.
      \   |   /    \   |   /
      /   |   \    /   |   \
      '===|    `""`    |==='
      .===|    .==.    |===.
      \   |   /    \   |   /
      /   |   \    /   |   \
      '===|    `""`    |==='
      .===|    .==.    |===.
      \   |   /&&&&\   |   /
      /   |   \&&&&/   |   \
      '===|    `""`    |==='
          '--.______.--'
"""
