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

Charts are automatically updated each day. Consult [the repository website](https://maldins46.github.io/CovidAnalysis) for a neat live COVID-19 dashboard, comprising the latest version of the charts. You can also download all the available charts in PNG format [from here](https://github.com/maldins46/CovidAnalysis/releases/latest).
