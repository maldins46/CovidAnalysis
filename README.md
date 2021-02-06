# CovidAnalysis
![Python Tests](https://github.com/maldins46/CovidAnalysis/workflows/Python%20Tests/badge.svg)
![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=alert_status)
![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=sqale_rating)
![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=security_rating)
![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=reliability_rating)
![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=sqale_index)
![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=vulnerabilities)
![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=ncloc)
![Bugs](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=bugs)
![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=code_smells)
![License](https://img.shields.io/github/license/maldins46/CovidAnalysis)


Python module used to extract relevant information from Italian Government Covid Open Data. The repository uses [Open Data from the Italian Government](https://github.com/pcm-dpc/COVID-19) as a Git Submodule. As such, a plain clone does not initialize submodules. You have to clone the project this way:

```
git clone --recurse-submodules https://github.com/maldins46/CovidAnalysis.git 
```
Besides performing the clone, also recursively initialize submodules. Also, the submodule have to be updated manually periodically, by using

```
git submodule update --remote --recursive
```

Charts are automatically updated each day. Consult [the repository website](https://maldins46.github.io/CovidAnalysis) for a neat live COVID-19 dashboard, comprising the latest version of the charts. You can also download all the available charts in PNG format [from here](https://github.com/maldins46/CovidAnalysis/releases/latest).
