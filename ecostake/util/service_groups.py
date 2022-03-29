from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": "ecostake_harvester ecostake_timelord_launcher ecostake_timelord ecostake_farmer ecostake_full_node ecostake_wallet".split(),
    "node": "ecostake_full_node".split(),
    "harvester": "ecostake_harvester".split(),
    "farmer": "ecostake_harvester ecostake_farmer ecostake_full_node ecostake_wallet".split(),
    "farmer-no-wallet": "ecostake_harvester ecostake_farmer ecostake_full_node".split(),
    "farmer-only": "ecostake_farmer".split(),
    "timelord": "ecostake_timelord_launcher ecostake_timelord ecostake_full_node".split(),
    "timelord-only": "ecostake_timelord".split(),
    "timelord-launcher-only": "ecostake_timelord_launcher".split(),
    "wallet": "ecostake_wallet ecostake_full_node".split(),
    "wallet-only": "ecostake_wallet".split(),
    "introducer": "ecostake_introducer".split(),
    "simulator": "ecostake_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
