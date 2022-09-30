from typing import Dict, NamedTuple
from os import environ


DEPOSIT_CLI_VERSION = '2.3.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes


MAINNET = 'mainnet'
ROPSTEN = 'ropsten'
GOERLI = 'goerli'
PRATER = 'prater'
KILN = 'kiln'
SEPOLIA = 'sepolia'
GNOSIS_TESTNET = 'gnosis-testnet'
GNOSIS = 'gnosis'
CHIADO = 'chiado'
TEST = 'test'


# Mainnet setting
MainnetSetting = BaseChainSetting(NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'))
# Ropsten setting
RopstenSetting = BaseChainSetting(NETWORK_NAME=ROPSTEN, GENESIS_FORK_VERSION=bytes.fromhex('80000069'))
# Goerli setting
GoerliSetting = BaseChainSetting(NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'))
# Merge Testnet (spec v1.1.9)
KilnSetting = BaseChainSetting(NETWORK_NAME=KILN, GENESIS_FORK_VERSION=bytes.fromhex('70000069'))
# Sepolia setting
SepoliaSetting = BaseChainSetting(NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'))

# Gnosis Beacon Chain testnet setting
GnosisTestnetSetting = BaseChainSetting(NETWORK_NAME=GNOSIS_TESTNET, GENESIS_FORK_VERSION=bytes.fromhex('00006464'))
# Gnosis Chiado testnet setting (10200)
GnosisChiadoTestnetSetting = BaseChainSetting(NETWORK_NAME=CHIADO, GENESIS_FORK_VERSION=bytes.fromhex('000027D8')) 
# Gnosis Beacon Chain setting (100)
GnosisSetting = BaseChainSetting(NETWORK_NAME=GNOSIS, GENESIS_FORK_VERSION=bytes.fromhex('00000064'))

TestSetting = BaseChainSetting(NETWORK_NAME=TEST, GENESIS_FORK_VERSION=bytes.fromhex(environ.get('GENESIS_FORK_VERSION', '12345678')))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    ROPSTEN: RopstenSetting,
    GOERLI: GoerliSetting,
    PRATER: GoerliSetting,  # Prater is the old name of the Prater/Goerli testnet
    KILN: KilnSetting,
    SEPOLIA: SepoliaSetting,
    GNOSIS_TESTNET: GnosisTestnetSetting,
    GNOSIS: GnosisSetting,
    CHIADO: GnosisChiadoTestnetSetting,
    TEST: TestSetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]
