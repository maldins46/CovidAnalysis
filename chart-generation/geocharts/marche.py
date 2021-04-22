from data_extractors.covid_provinces import marche_geodf
import matplotlib.pyplot as plt
import pandas as pd


def weekly_incidence(save_image=False, show=False):
    pd.options.mode.chained_assignment = None
    marche_geodf['incid_sett_per_100000_round'] = marche_geodf['incid_sett_per_100000_ab'].apply(lambda x: round(x, 0))
    marche_geodf['incid_sett_per_100000_ab_label'] = marche_geodf['incid_sett_per_100000_round'].apply(lambda x: f"{x:.0f}")
    pd.options.mode.chained_assignment = 'warn'

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incidenza settimanale nuovi positivi per 100.000 abitanti,\nnell\'ultimo giorno, per provincia della regione Marche')

    for _, row in marche_geodf.iterrows():
        plt.annotate(text=row['incid_sett_per_100000_ab_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    marche_geodf.plot(ax=ax, column='incid_sett_per_100000_round', legend=False,
                      cmap='OrRd', linewidth=0.6, edgecolor='0.6')

    if save_image:
        fig.savefig('./charts/covid/incidenza_sett_marche_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def weekly_increment(save_image=False, show=False):
    """
    Geographical chart that shows the increment of the incidence,
    for all provinces of Marche.
    """

    pd.options.mode.chained_assignment = None
    marche_geodf['incremento_incidenza_100'] = marche_geodf['incremento_incidenza'].apply(lambda x: x * 100)
    marche_geodf['incremento_incidenza_label'] = marche_geodf['incremento_incidenza_100'].apply(lambda x: f"{x:.0f}%" if x <= 0 else f"+{x:.0f}%")
    pd.options.mode.chained_assignment = 'warn'

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incremento/decremento casi rispetto alla\nsettimana precedente, per provincia delle Marche')

    for _, row in marche_geodf.iterrows():
        plt.annotate(text=row['incremento_incidenza_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    pos = marche_geodf[marche_geodf['incremento_incidenza_100'] >= 0]
    base = pos.plot(ax=ax, column='incremento_incidenza_100', legend=False,
                    cmap='Oranges', linewidth=0.6, edgecolor='0.6')

    neg = marche_geodf[marche_geodf['incremento_incidenza_100'] < 0]

    pd.options.mode.chained_assignment = None
    neg['incremento_incidenza_100'] = neg['incremento_incidenza_100'].apply(lambda x: -x)
    pd.options.mode.chained_assignment = 'warn'

    neg.plot(ax=base, column='incremento_incidenza_100', legend=False,
             cmap='Greens', linewidth=0.6, edgecolor='0.6')

    if save_image:
        fig.savefig('./charts/covid/increm_sett_per_provincia_marche_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def new_positives(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Nuovi positivi nell\'ultimo giorno, in valori assoluti,\nper provincia della regione Marche')

    for _, row in marche_geodf.iterrows():
        plt.annotate(text=row['nuovi_positivi'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    marche_geodf.plot(ax=ax, column='nuovi_positivi', legend=False,
                      cmap='OrRd', linewidth=0.6, edgecolor='0.6')

    if save_image:
        fig.savefig('./charts/covid/totale_casi_per_province_marche_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
