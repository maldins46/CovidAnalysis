from data_extractors.covid_provinces import marche_geodf
import matplotlib.pyplot as plt


def weekly_incidence(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incidenza settimanale nuovi positivi per 100.000 abitanti')

    for idx, row in marche_geodf.iterrows():
        plt.annotate(text=row['incid_sett_per_100000_ab_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    marche_geodf.plot(ax=ax, column='incid_sett_per_100000_round', legend=True, scheme="user_defined",
                      cmap='OrRd', linewidth=0.6, edgecolor='0.6', classification_kwds={'bins': [50, 100, 250, 350]},
                      legend_kwds=dict(loc='upper right', title="Incid.sett. per 100.000 ab.\n", frameon=False))

    if save_image:
        fig.savefig('./assets/incidenza_sett_marche_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def new_positives(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Nuovi positivi in val. ass. ultimo giorno')

    for idx, row in marche_geodf.iterrows():
        plt.annotate(text=row['nuovi_positivi'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    marche_geodf.plot(ax=ax, column='nuovi_positivi', legend=True, scheme="quantiles",
                      cmap='OrRd', linewidth=0.6, edgecolor='0.6',
                      legend_kwds=dict(loc='upper right', title="Nuovi positivi\n", frameon=False))

    if save_image:
        fig.savefig('./assets/totale_casi_per_province_marche_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
