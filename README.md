# nahmii2csv.py

Parses swaps, liquidity mining, airdrops and Kiwii NFT Minting from Nahmii v2 and converts it to CSV, especially formatted for kryptosekken.no for tax calculations.

## Usage

```
$ python3 nahmii2csv.py <wallet address>
Tidspunkt,Type,Inn,Inn-Valuta,Ut,Ut-Valuta,Gebyr,Gebyr-Valuta,Marked,Notat
2021-12-13 10:48:14,Handel,0.04,WBTC,100000.0,NII,0.00038065792,ETH,NiiFi,Swap,
2021-12-14 17:13:14,Handel,1.2389102,NIIFI-WBTCNII,0.04,WBTC,0.00052652906,ETH,NiiFi,Add liquidity,
2021-12-14 17:13:14,Handel,1.2389102,NIIFI-WBTCNII,224875.870,NII,0.0005146315,ETH,NiiFi,Add liquidity,
2021-12-15 12:11:45,Renteinntekt,13606.26786322117,NIIFI,,,,,NiiFi,Airdrop: Liquidity Mining,
```

## Kiwii NFT Minting

The cost of minting an egg is by default 0.2 ETH, which is hardcoded in this script. If you payed less, e.g. being on the whitelist, you need to edit this in the script, or change it in the output.

## Trusted Bridge

The Nahmii team opened a trusted bridge where you could transfer nii tokens from nahmii mainnet v1 to v2. If you did this, then you had to leave 1000 nii on v1 (by design) and you would receive 1000 extra NII on v2. You also had to pay a fee of 0.5% of the total amount transferred.

nahmii2csv handles this transaction as a normal transaction of receiving 1000 nii with a fee of 0.5%. This works given that you have tracked activity on Nahmii v1 manually. 

Example: You transferred 10000 NII to the trusted bridge, and after paying 0.5% fee you got 9950 NII plus the 1000 extra, 10950 NII in total. Since it's not possible to know the original amount sent from Nahmii v1 to exactly know how much you payed in fee, we calculate 0.502513% of the amount received, which is very close to accurate.


| Description     | Calc                | Sum  |
| --------------- |:-------------------:| -----:|
| Received        | 10000 x (1 - 0.005) | 9950 |
| Fee payed       | 9950 × 0.00502513   | 50.0000435 |
| Original amount | 9950 x 1.00502513   | 10000.0000435 |

The entry will look like the following in CSV:
```
2022-06-17 23:36:28,Overføring-Inn,1000,NII,,,50.0000435,NII,NiiFi,Trusted Bridge Transfer,
```

Note: The Trusted Bridge was mostly complete at 2022/06/17, but a few transfers were still not complete. You need to edit the script if you received the funds from the trusted bridge at a later stage.

Read more about the Trusted Bridge:  
https://blog.nahmii.io/nahmii-1-0-to-nahmii-2-0-trusted-bridge-announced-661c0cac339  
https://blog.nahmii.io/nahmii-1-0-to-nahmii-2-0-trusted-bridge-payments-completed-e1b4bc1fc0b0

## Disclaimer
Please verify each transaction manually as nahmii2csv provide no guarentee that everything is correct.
