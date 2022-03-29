import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("ECOSTAKE_ROOT", "~/.ecostake/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("ECOSTAKE_KEYS_ROOT", "~/.ecostake_keys"))).resolve()
