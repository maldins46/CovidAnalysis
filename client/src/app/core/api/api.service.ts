import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {NationalSummaryModel} from '../../shared/models/national-summary.model';
import {BenchmarkSummaryModel} from '../../shared/models/benchmark-summary.model';
import {MarcheSummaryModel} from '../../shared/models/marche-summary.model';
import {VaccinesSummaryModel} from '../../shared/models/vaccines-summary.model';


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private readonly http: HttpClient) { }

  public getNationalSummary(): Observable<NationalSummaryModel> {
    return this.http.get<NationalSummaryModel>('https://maldins46.github.io/CovidAnalysis/assets/data/national_summary.json');
  }

  public getBenchmarkSummary(): Observable<BenchmarkSummaryModel> {
    return this.http.get<BenchmarkSummaryModel>('https://maldins46.github.io/CovidAnalysis/assets/data/benchmark_summary.json');
  }

  public getMarcheSummary(): Observable<MarcheSummaryModel> {
    return this.http.get<MarcheSummaryModel>('https://maldins46.github.io/CovidAnalysis/assets/data/marche_summary.json');
  }

  public getVaccinesSummary(): Observable<VaccinesSummaryModel> {
    return this.http.get<VaccinesSummaryModel>('https://maldins46.github.io/CovidAnalysis/assets/data/vaccines_summary.json');
  }
}
