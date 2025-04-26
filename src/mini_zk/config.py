import os
from pathlib import Path

# Environment variable which contains the root of zettelkasten.
ZK_ROOT_ENV = "ZK_ROOT"
# Default path for zettelkasten root.
# mini-zk will fallback to this path if ZK_ROOT_ENV is not set in the system.
ZK_ROOT_PATH = "~/notes/"

# Max title length.
MAX_TITLE_LENGTH = 40

# The length of note ID prefix that is added before the note title in filename.
ID_LENGTH = 6

# Editor used to open created notes.
EDITOR = "nvim"


# validate_default_zk_root - check if ZK_ROOT_ENV is set in the system. If not set ZK_ROOT to ZK_ROOT_PATH from config.
def validate_default_zk_root():
    zk_root = os.environ.get(ZK_ROOT_ENV)
    if zk_root is None:
        print(
            f"{ZK_ROOT_ENV} environment variable not set, falling back to {ZK_ROOT_PATH} default path."
        )
        zk_root = ZK_ROOT_PATH
    return Path(zk_root).expanduser().resolve()


ZK_ROOT = validate_default_zk_root()
