from data_extractors.covid_provinces import marche_geodf
import matplotlib.pyplot as plt


def weekly_incidence(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incidenza settimanale nuovi positivi per 100.000 abitanti,\nnell\'ultimo giorno, per provincia della regione Marche')

    for row in marche_geodf.itertuples(index=True, name='Pandas'):
        plt.annotate(text=row.incid_sett_per_100000_ab_label, xy=row.coords, horizontalalignment='center', fontsize=10)

    marche_geodf.plot(ax=ax, column='incid_sett_per_100000_round', legend=True,  scheme="quantiles",
                      cmap='OrRd', linewidth=0.6, edgecolor='0.6',
                      legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/covid/incidenza_sett_marche_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def new_positives(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Nuovi positivi nell\'ultimo giorno, in valori assoluti,\nper provincia della regione Marche')

    for row in marche_geodf.itertuples(index=True, name='Pandas'):
        plt.annotate(text=row.nuovi_positivi, xy=row.coords, horizontalalignment='center', fontsize=10)

    marche_geodf.plot(ax=ax, column='nuovi_positivi', legend=True, scheme="quantiles",
                      cmap='OrRd', linewidth=0.6, edgecolor='0.6',
                      legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/covid/totale_casi_per_province_marche_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
