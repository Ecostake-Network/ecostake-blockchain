from setuptools import setup

dependencies = [
    "multidict==5.1.0",  # Avoid 5.2.0 due to Avast
    "blspy==1.0.6",  # Signature library
    "chiavdf==1.0.3",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.6",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.15",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the ecostake processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==8.1.2",  # For the CLI
    "dnspythonchia==2.2.0",  # Query DNS seeds
    "watchdog==2.1.6",  # Filesystem event watching - watches keyring.yaml
    "nest-asyncio==1.5.1",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "types-setuptools",
]

kwargs = dict(
    name="ecostake-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@ecostake.online",
    description="Ecostake blockchain full node, farmer, timelord, and wallet.",
    url="https://ecostake.online/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="ecostake blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "ecostake",
        "ecostake.cmds",
        "ecostake.clvm",
        "ecostake.consensus",
        "ecostake.daemon",
        "ecostake.full_node",
        "ecostake.timelord",
        "ecostake.farmer",
        "ecostake.harvester",
        "ecostake.introducer",
        "ecostake.plotters",
        "ecostake.plotting",
        "ecostake.pools",
        "ecostake.protocols",
        "ecostake.rpc",
        "ecostake.server",
        "ecostake.simulator",
        "ecostake.types.blockchain_format",
        "ecostake.types",
        "ecostake.util",
        "ecostake.wallet",
        "ecostake.wallet.puzzles",
        "ecostake.wallet.rl_wallet",
        "ecostake.wallet.cc_wallet",
        "ecostake.wallet.did_wallet",
        "ecostake.wallet.settings",
        "ecostake.wallet.trading",
        "ecostake.wallet.util",
        "ecostake.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "ecostake = ecostake.cmds.ecostake:main",
            "ecostake_wallet = ecostake.server.start_wallet:main",
            "ecostake_full_node = ecostake.server.start_full_node:main",
            "ecostake_harvester = ecostake.server.start_harvester:main",
            "ecostake_farmer = ecostake.server.start_farmer:main",
            "ecostake_introducer = ecostake.server.start_introducer:main",
            "ecostake_timelord = ecostake.server.start_timelord:main",
            "ecostake_timelord_launcher = ecostake.timelord.timelord_launcher:main",
            "ecostake_full_node_simulator = ecostake.simulator.start_simulator:main",
        ]
    },
    package_data={
        "ecostake": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "ecostake.util": ["initial-*.yaml", "english.txt"],
        "ecostake.ssl": ["ecostake_ca.crt", "ecostake_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)  # type: ignore
