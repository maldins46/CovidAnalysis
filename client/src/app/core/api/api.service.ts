import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {NationalSummaryModel} from '../../shared/models/national-summary.model';
import {MarcheSummaryModel} from '../../shared/models/marche-summary.model';
import {VaccinesSummaryModel} from '../../shared/models/vaccines-summary.model';
import {SlideModel} from '../../shared/models/slide.model';


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private readonly http: HttpClient) { }

  public getNationalSummary(): Observable<NationalSummaryModel> {
    return this.http.get<NationalSummaryModel>('https://maldins46.github.io/CovidAnalysis/charts/covid/national_summary.json');
  }

  public getMarcheSummary(): Observable<MarcheSummaryModel> {
    return this.http.get<MarcheSummaryModel>('https://maldins46.github.io/CovidAnalysis/charts/covid/marche_summary.json');
  }

  public getVaccinesSummary(): Observable<VaccinesSummaryModel> {
    return this.http.get<VaccinesSummaryModel>('https://maldins46.github.io/CovidAnalysis/charts/vaccines/vaccines_summary.json');
  }

  public getNationalIncidenceSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/incidenza_sett_per_regioni_mappa.png',
        description: 'Il grafico mostra l\'incidenza settimanale dei nuovi casi registrati, per ogni regione italiana, ' +
          'scalato su 100.000 abitanti. Ciò permette di confrontare tra loro le varie regioni.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/incidenza_sett_per_prov_mappa.png',
        description: 'Il grafico mostra l\'incidenza settimanale dei nuovi casi registrati, per ogni provincia italiana, ' +
          'scalato su 100.000 abitanti. Ciò permette di confrontare tra loro le varie regioni.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/increm_sett_per_regioni_mappa.png',
        description: 'Il grafico mostra l\'incremento percentuale dei casi, rispetto a quelli registrati nella settimana ' +
          'precedente, per ogni regione italiana. In questo modo è possibile individuare le zone nelle quali l\'epidemia è in espansione.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/increm_sett_per_provincia_mappa.png',
        description: 'Il grafico mostra l\'incremento percentuale dei casi, rispetto a quelli registrati nella settimana ' +
          'precedente, per ogni provincia italiana. In questo modo è possibile individuare le zone nelle quali l\'epidemia è in espansione.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/incid_sett_per_regioni.png',
        description: 'Il grafico mostra l\'evoluzione del tasso di incidenza settimanale dei nuovi positivi, per ogni ' +
          'regione del benchmark. È riportata, con la traccia semi-trasparente, la media italiana.'
      }
    ];
  }

  public getNationalTiSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/ti_mappa.png',
        description: 'Il grafico riporta, per ogni regione italiana, il tasso di occupazione dei reparti ' +
          'di terapia intensiva, all\'ultima rilevazione. Il livello di allerta è posto sopra il 30% dei posti occupati.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/increm_sett_ti_per_regioni_mappa.png',
        description: 'Il grafico mostra l\'incremento settimanale di posti occupati in terapia intensiva, rispetto ' +
          'allo stesso giorno della settimana precedente. L\'indicatore è utile per comprendere se tale parametro è ' +
          'al momento in aumento o diminuzione.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/ti_per_regioni.png',
        description: 'Il grafico riporta, per ogni regione del benchmark, l\'evoluzione riguardo ' +
          'l\' occupazione dei reparti di terapia intensiva. È riportata, con la traccia semi-trasparente, ' +
          'la media italiana. La linea gialla indica il livello d\'allerta del 30% dei posti TI occupati ' +
          '(oltre il quale sono a rischio gli interventi ordinari), mentre la linea rossa la saturazione (100% di posti occupati).'
      }
    ];
  }

  public getOtherNationalSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/parametri_italia.png',
        description: 'Il grafico raffronta differenti indicatori a livello nazionale, in valori assoluti: ' +
          'I decessi giornalieri (in media mobile di 7 giorni), l\'ammontare dei pazienti correntemente in terapia ' +
          'intensiva, i nuovi positivi registrati ogni giorno (in media mobile di 7 giorni) è l\'ammontare dei ' +
          'pazienti correntemente ricoverati con sintomi per COVID-19.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/rt_per_regioni.png',
        description: 'Il grafico mostra l\'andamento dell\'indice R(t) per le regioni del benchmark, calcolato ' +
          'con modellazione SIRD: un metodo semplificato, non quello utilizzato dall\'ISS, ma indicativo dell\'andamento. ' +
          'Per stabilizzare il dato, è stata applicata una media mobile di 7 giorni.'
      }
    ];
  }

  public getMarcheIncidenceSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/incid_sett_marche.png',
        description: 'Il grafico mostra l\'incidenza settimanale dei nuovi casi registrati, ' +
          'per ogni provincia della regione Marche, scalato su 100.000 abitanti (per rendere ' +
          'possibile il confronto). Il dato provinciale è fortemente instabile: per la consultazione, ' +
          'è stata effettuata una media mobile su un periodo di 7 giorni.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/increm_sett_per_provincia_marche_mappa.png',
        description: 'Il grafico mostra l\'incremento percentuale dei casi, rispetto a quelli registrati nella settimana ' +
          'precedente, per ogni provincia delle Marche. In questo modo è possibile individuare le zone nelle quali l\'epidemia è in espansione.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/incidenza_sett_marche_mappa.png',
        description: 'Il grafico mostra  l\'incidenza settimanale all\'ultima rilevazione, per ogni provincia' +
          'della regione Marche.'
      }
    ];
  }


  public getMarcheAbsSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/totale_casi_per_province_marche_mappa.png',
        description: 'Il grafico mostra i nuovi casi positivi registrati all\'ultima rilevazione, per ogni provincia' +
          'della regione Marche.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/totale_casi_per_province_marche_abs.png',
        description: 'Il grafico indica l\'evoluzione dei i nuovi casi positivi registrati giornalmente, tramite tampone ' +
          'molecolare, per ogni provincia della regione Marche. Il dato è riportato in valosi assoluti, per evidenziare ' +
          'il numero effettivo di casi di ogni provincia. Il dato provinciale è fortemente instabile: per la consultazione, ' +
          'è stata effettuata una media mobile su un periodo di 14 giorni, il che porta ad avere il dato arretrato ' +
          'temporalmente di una settimana. È riportata, con la traccia semi-trasparente, la media italiana.'
      }
    ];
  }

  public getOtherMarcheSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/parametri_marche.png',
        description: 'Il grafico raffronta differenti indicatori a livello regionale nelle Marche, in valori assoluti: ' +
          'I decessi giornalieri (in media mobile di 7 giorni), l\'ammontare dei pazienti correntemente in terapia ' +
          'intensiva, i nuovi positivi registrati ogni giorno (in media mobile di 7 giorni) è l\'ammontare dei ' +
          'pazienti correntemente ricoverati con sintomi per COVID-19.'
      }
    ];
  }

  public getVaccineAdministrationSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/vaccines/dosi_italia.png',
        description: 'Il grafico indica le dosi somministrate ogni giorno in Italia, facendo distinzione ' +
          'tra prime e seconde dosi. L\'altezza di ogni barra del grafico indica il totale delle ' +
          'somministrazioni giornaliere.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/vaccines/dosi_per_regioni_mappa.png',
        description: 'Il grafico indica le somministrazioni effettuate nell\'ultimo giorno, nelle regioni ' +
          'italiane. Il valore è posto in percentuale sulla popolazione della regionale, così da poter effettuare ' +
          'un confronto tra le stesse.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/vaccines/dosi_marche.png',
        description: 'Il grafico indica le dosi somministrate ogni giorno nella regione Marche, facendo distinzione ' +
          'tra prime e seconde dosi. L\'altezza di ogni barra del grafico indica il totale delle ' +
          'somministrazioni giornaliere.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/vaccines/dosi_per_regioni.png',
        description: 'Il grafico mostra le singole dosi di vaccino somministrate giornalmente per ogni regione (senza ' +
          'distinzione tra prima dose e richiamo). Il dato è scalato su 100.000 abitanti, rendendo così possibile ' +
          'mettere in relazione tra loro le regioni, tenendo conto della diversa densità di popolazione. È riportata, ' +
          'con la traccia semi-trasparente, la media italiana. È applicata una media mobile di 7 giorni, per rendere il ' +
          'grafico più comprensibile.'
      }
    ];
  }

  public getVaccineImmunizationSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/vaccines/immunizzati_mappa.png',
        description: 'Il grafico mostra la percentuale di popolazione risultante immunizzata, per ogni regione ' +
          'italiana. Ci si riferisce con immunizzata alla parte della popolazione tale da aver ricevuto ' +
          'sia la prima dose che il richiamo del vaccino.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/vaccines/copertura_mappa.png',
        description: 'Il grafico mostra la percentuale di popolazione risultante coperta con almeno una dose di vaccino.'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/vaccines/immunizzati.png',
        description: 'Il grafico mostra la percentuale di popolazione, per ogni regione del benchmark e per ' +
          'l\'Italia (traccia semi-trasparente) che puo essere definita immunizzata, ovvero tale da aver ricevuto ' +
          'sia la prima dose che il richiamo.'
      }
    ];
  }
}
