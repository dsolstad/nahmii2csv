# nahmii2csv.py

Parses swaps and liquidity mining from explorer.nahmii.io and converts it to CSV, especially formatted for kryptosekken.no for tax calculations. 

## Usage

Enter target wallet address in the `wallet` variable on line 9.

```
$ python3 nahmii2csv.py
Tidspunkt,Type,Inn,Inn-Valuta,Ut,Ut-Valuta,Gebyr,Gebyr-Valuta,Marked,Notat
2021-12-13 10:48:14,Handel,0.04,WBTC,100000.0,NII,0.00038065792,ETH,NiiFi,Swap,
2021-12-14 17:13:14,Handel,1.2389102,NIIFI-WBTCNII,0.04,WBTC,0.00052652906,ETH,NiiFi,Add liquidity,
2021-12-14 17:13:14,Handel,1.2389102,NIIFI-WBTCNII,224875.870,NII,0.0005146315,ETH,NiiFi,Add liquidity,
```
