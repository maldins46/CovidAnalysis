import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../core/api/api.service';
import {VaccinesSummaryModel} from '../../shared/models/vaccines-summary.model';
import {SlideModel} from '../../shared/components/carousel/slide.model';
import {SummaryTableModel} from '../../shared/components/summary-table/summary-table.model';
import {NationalSummaryModel} from '../../shared/models/national-summary.model';

@Component({
  selector: 'app-vaccines',
  templateUrl: './vaccines.component.html'
})
export class VaccinesComponent implements OnInit {
  vaccinesAdmSlides: SlideModel[] = [];
  vaccinesImmunesSlides: SlideModel[] = [];
  vaccinesSummaryTable: SummaryTableModel | undefined;
  lastUpdate: string | undefined;

  constructor(private readonly api: ApiService) { }

  ngOnInit(): void {
    this.api.getVaccinesSummary().subscribe(data => {
      this.vaccinesSummaryTable = this.adaptToTable(data);
      this.lastUpdate = data.lastUpdate;
    });
    this.vaccinesAdmSlides = this.api.getVaccineAdministrationSlides();
    this.vaccinesImmunesSlides = this.api.getVaccineImmunizationSlides();
  }

  adaptToTable(data: VaccinesSummaryModel): SummaryTableModel {
    return {
      heads: [ 'Italia', 'Marche', 'Veneto', 'Toscana' ],
      rows: [
        {
          title: 'Pop. completamente vaccinata', isPercFormat: true,
          values: [
            { increment: 0, value: data.italy.fullVaccPopulation },
            { increment: 0, value: data.marche.fullVaccPopulation },
            { increment: 0, value: data.veneto.fullVaccPopulation },
            { increment: 0, value: data.toscana.fullVaccPopulation }
          ]
        },
        {
          title: 'Somministraz. ultimo gg.', isIncrementPositive: true, isPercFormat: false,
          values: [
            { increment: data.italy.dailyShotsIncrement, value: data.italy.dailyShots },
            { increment: data.marche.dailyShotsIncrement, value: data.marche.dailyShots },
            { increment: data.veneto.dailyShotsIncrement, value: data.veneto.dailyShots },
            { increment: data.toscana.dailyShotsIncrement, value: data.toscana.dailyShots }
          ]
        },
        {
          title: 'Prime dosi ultimo gg.', isIncrementPositive: true, isPercFormat: false,
          values: [
            { increment: data.italy.dailyFirstShotsIncrement, value: data.italy.dailyFirstShots },
            { increment: data.marche.dailyFirstShotsIncrement, value: data.marche.dailyFirstShots },
            { increment: data.veneto.dailyFirstShotsIncrement, value: data.veneto.dailyFirstShots },
            { increment: data.toscana.dailyFirstShotsIncrement, value: data.toscana.dailyFirstShots }
          ]
        },
        {
          title: 'Seconde dosi ultimo gg.', isIncrementPositive: true, isPercFormat: false,
          values: [
            { increment: data.italy.dailySecondShotsIncrement, value: data.italy.dailySecondShots },
            { increment: data.marche.dailySecondShotsIncrement, value: data.marche.dailySecondShots },
            { increment: data.veneto.dailySecondShotsIncrement, value: data.veneto.dailySecondShots },
            { increment: data.toscana.dailySecondShotsIncrement, value: data.toscana.dailySecondShots }
          ]
        }
      ]
    };
  }
}
