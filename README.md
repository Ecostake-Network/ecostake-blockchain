# ecostake-blockchain (ECOSTAKE)

![Alt Ecostake Logo](https://github.com/Ecostake-Network/ecostake-blockchain/raw/main/ecostake-blockchain-gui/src/assets/img/ecostake_circle.png)

Ecostake (ECOSTAKE) is a modern, green cryptocurrency built to be efficient, decentralized, and secure.


## Useful Links

- [Ecostake Website](https://www.ecostake.online/) - Visit the Ecostake Website
- [Ecostake FAQ](https://www.ecostake.online/faq) - Find answers to Frequently Asked Questions
- [Ecostake Calculator](https://chiaforkscalculator.com/) - Estimate out how your Ecostake earnings.
- [Ecostake Blockchain DB](https://www.ecostake.online//blockchain_v1_mainnet.sqlite) - Download the latest Ecostake Blockchain Database


## Social Links
- [Discord](https://discord.gg/SAn2ZF3GJH) - Join the Ecostake Discord Community
- [Twitter](https://twitter.com/Ecostake-NetworkNet) - Follow Ecostake on Twitter


## How to Install

Ecostake Executable are available from our [GitHub Releases Page](https://github.com/Ecostake-Network/ecostake-blockchain/releases). You can also build from source. An example case for Ubuntu source installation is provided below. Please [visit our wiki page](https://github.com/Ecostake-Network/ecostake-blockchain/wiki) for more details, and for source installation on operating systems.

```
# Update, install GIT, clone Ecostake repo

   sudo apt-get update
   sudo apt install git -y
   git clone https://github.com/Ecostake-Network/ecostake-blockchain.git
  
# Install Ecostake Blockchain

   cd ecostake-blockchain
   sh install.sh
   . ./activate
   ecostake init

# Install Ecostake GUI

   sh install-gui.sh
   cd ecostake-blockchain-gui
   npm run electron &
```

If the Ecostake client is unable to find peers automatically, please connect to the following official peers:

- introducer.ecostake.online / Port: 38444
- dns-introducer.ecostake.online / Port: 38444


## How to Stake

1. Query the staking addresses according to your farming plot list:

   ```
   $ ecostake farm summary
   ...
   Staking addresses:
     ecostake1x6jjvepyvjv7395nmtywvx9mknshgy78dsmuu38m0e9grxr080nsltjugr (balance: 0, plots: 27)
   ...
   ```

2. Deposit coins to the staking address:

   ```
   $ ecostake wallet send -t ecostake1x6jjvepyvjv7395nmtywvx9mknshgy78dsmuu38m0e9grxr080nsltjugr -a 1
   ```

   Wait for the transaction get confirmed, query staking balance again:

   ```
   $ ecostake farm summary
   ...
   Staking addresses:
     ecostake1x6jjvepyvjv7395nmtywvx9mknshgy78dsmuu38m0e9grxr080nsltjugr (balance: 1, plots: 27)
   ...
   ```

3. Withdraw coins from the staking address:

   ```
   $ ecostake wallet send_from -s ecostake1x6jjvepyvjv7395nmtywvx9mknshgy78dsmuu38m0e9grxr080nsltjugr -t $RECEIVER -n $NUMCOINS
   ```

   Do a transaction to transfer a number of coins from the staking address to any receive address.

   The value of each key will depend upon how the coins were deposited to the staking address.

   Make sure to choose the wallet that contains the plot farmer key.
