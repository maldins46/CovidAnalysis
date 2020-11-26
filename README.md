# CovidAnalysis
![Python Tests](https://github.com/maldins46/CovidAnalysis/workflows/Python%20Tests/badge.svg)

Python module used to extract relevant information from Italian Government Covid Open Data. The repository uses [Open Data from the Italian Government](https://github.com/pcm-dpc/COVID-19) as a Git Submodule. As such, a plain clone does not initialize submodules. You have to clone the project this way:

```
git clone --recurse-submodules https://github.com/maldins46/CovidAnalysis.git 
```
Besides performing the clone, also recursively initialize submodules. Also, the submodule have to be updated manually periodically, by using

```
git submodule update --remote --recursive
```

## Charts
Charts are automatically updated each day. [Here](https://github.com/maldins46/CovidAnalysis/releases/latest) you can download the updated charts. These are the available live charts:

![Occupazione TI per regioni](./docs/ti_per_regioni.png)
![Positivi per regioni](./docs/positivi_per_regioni.png)
![Deceduti per regioni](./docs/deceduti_per_regioni.png)
![Ricoverati con sintomi per regioni](./docs/ricoverati_con_sintomi_per_regioni.png)
![Deceduti per regioni](./docs/totale_casi_per_province_marche.png)
