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

## Live charts
Charts shown here are automatically updated each day.
![Occupazione TI per regioni](https://github.com/maldins46/CovidAnalysis/releases/latest/download/ti_per_regioni.png)
![Positivi per regioni](https://github.com/maldins46/CovidAnalysis/releases/latest/download/positivi_per_regioni.png)
![Ricoverati con sintomi](https://github.com/maldins46/CovidAnalysis/releases/latest/download/ricoverati_con_sintomi.png)
