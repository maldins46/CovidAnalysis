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
        description: 'Incidenza settimanale per regioni'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/incidenza_sett_per_prov_mappa.png',
        description: 'Incidenza settimanale per province'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/incid_sett_per_regioni.png',
        description: 'Andamento incidenza benchmark'
      }
    ];
  }

  public getNationalTiSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/ti_mappa.png',
        description: 'Occupazione ti per regioni'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/ti_per_regioni.png',
        description: 'Andamento occupazione TI benchmark'
      }
    ];
  }

  public getOtherNationalSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/parametri_italia.png',
        description: 'Parametri Italia'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/rt_per_regioni.png',
        description: 'Indice R(t) SIRD'
      }
    ];
  }

  public getMarcheIncidenceSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/incidenza_sett_marche_mappa.png',
        description: 'Incidenza settimanale Marche mappa'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/incid_sett_marche.png',
        description: 'Andamento incidenza settimanale Marche'
      }
    ];
  }


  public getMarcheAbsSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/totale_casi_per_province_marche_mappa.png',
        description: 'Nuovi positivi Marche mappa'
      },
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/totale_casi_per_province_marche_abs.png',
        description: 'Andamento nuovi positivi Marche'
      }
    ];
  }

  public getOtherMarcheSlides(): SlideModel[] {
    return [
      {
        src: 'https://maldins46.github.io/CovidAnalysis/charts/covid/parametri_marche.png',
        description: 'Parametri Marche'
      }
    ];
  }
}
