import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../core/api/api.service';
import {NationalSummaryModel} from '../../shared/models/national-summary.model';
import {SlideModel} from '../../shared/components/carousel/slide.model';
import {SummaryTableModel} from '../../shared/components/summary-table/summary-table.model';

@Component({
  selector: 'app-italy',
  templateUrl: './italy.component.html'
})
export class ItalyComponent implements OnInit {
  incidenceSlides: SlideModel[] = [];
  tiSlides: SlideModel[] = [];
  otherSlides: SlideModel[] = [];
  nationalSummaryTable: SummaryTableModel | undefined;
  lastUpdate: string | undefined;

  constructor(private readonly api: ApiService) { }

  ngOnInit(): void {
    this.api.getNationalSummary().subscribe(data => {
      this.nationalSummaryTable = this.adaptToTable(data);
      this.lastUpdate = data.lastUpdate;
    });
    this.incidenceSlides = this.api.getNationalIncidenceSlides();
    this.tiSlides = this.api.getNationalTiSlides();
    this.otherSlides = this.api.getOtherNationalSlides();
  }

  adaptToTable(data: NationalSummaryModel): SummaryTableModel {
    return {
      heads: [ 'Italia', 'Marche', 'Veneto', 'Toscana' ],
      rows: [
        {
          title: 'Positivi ultimo giorno', isIncrementPositive: false, isPercFormat: false,
          values: [
            { increment: data.italia.newPositivesIncrement, value: data.italia.newPositives },
            { increment: data.marche.newPositivesIncrement, value: data.marche.newPositives },
            { increment: data.veneto.newPositivesIncrement, value: data.veneto.newPositives },
            { increment: data.toscana.newPositivesIncrement, value: data.toscana.newPositives }
          ]
        },
        {
          title: 'Positivi ultimi 7 giorni', isIncrementPositive: false, isPercFormat: false,
          values: [
            { increment: data.italia.weeklyPositivesIncrement, value: data.italia.weeklyPositives },
            { increment: data.marche.weeklyPositivesIncrement, value: data.marche.weeklyPositives },
            { increment: data.veneto.weeklyPositivesIncrement, value: data.veneto.weeklyPositives },
            { increment: data.toscana.weeklyPositivesIncrement, value: data.toscana.weeklyPositives }
          ]
        },
        {
          title: 'Occupaz. TI ultimo giorno', isIncrementPositive: false, isPercFormat: true,
          values: [
            { increment: data.italia.tiIncrement, value: data.italia.tiPercentage },
            { increment: data.marche.tiIncrement, value: data.marche.tiPercentage },
            { increment: data.veneto.tiIncrement, value: data.veneto.tiPercentage },
            { increment: data.toscana.tiIncrement, value: data.toscana.tiPercentage }
          ]
        }
      ]
    };
  }
}
