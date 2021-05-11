import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../core/api/api.service';
import {MarcheSummaryModel} from '../../shared/models/marche-summary.model';
import {SlideModel} from '../../shared/components/carousel/slide.model';
import {SummaryTableModel} from '../../shared/components/summary-table/summary-table.model';

@Component({
  selector: 'app-marche',
  templateUrl: './marche.component.html'
})
export class MarcheComponent implements OnInit {
  incidenceSlides: SlideModel[] = [];
  absSlides: SlideModel[] = [];
  otherParamsSlides: SlideModel[] = [];
  marcheSummaryTable: SummaryTableModel | undefined;
  lastUpdate: string | undefined;

  constructor(private readonly api: ApiService) { }

  ngOnInit(): void {
    this.api.getMarcheSummary().subscribe(data => {
      this.marcheSummaryTable = this.adaptToTable(data);
      this.lastUpdate = data.lastUpdate;
    });
    this.incidenceSlides = this.api.getMarcheIncidenceSlides();
    this.absSlides = this.api.getMarcheAbsSlides();
    this.otherParamsSlides = this.api.getOtherMarcheSlides();
  }

  adaptToTable(data: MarcheSummaryModel): SummaryTableModel {
    return {
      heads: [ 'Marche', 'Ancona', 'Macerata', 'Pes. e Urb.', 'Ascoli P.', 'Fermo' ],
      rows: [
        {
          title: 'Positivi ultimo giorno', isIncrementPositive: false, isPercFormat: false,
          values: [
            { increment: data.marche.newPositivesIncrement, value: data.marche.newPositives },
            { increment: data.ancona.newPositivesIncrement, value: data.ancona.newPositives },
            { increment: data.macerata.newPositivesIncrement, value: data.macerata.newPositives },
            { increment: data.pesaroeurbino.newPositivesIncrement, value: data.pesaroeurbino.newPositives },
            { increment: data.ascolipiceno.newPositivesIncrement, value: data.ascolipiceno.newPositives },
            { increment: data.fermo.newPositivesIncrement, value: data.fermo.newPositives }
          ]
        },
        {
          title: 'Positivi ultimi 7 giorni', isIncrementPositive: false, isPercFormat: false,
          values: [
            { increment: data.marche.weeklyPositivesIncrement, value: data.marche.weeklyPositives },
            { increment: data.ancona.weeklyPositivesIncrement, value: data.ancona.weeklyPositives },
            { increment: data.macerata.weeklyPositivesIncrement, value: data.macerata.weeklyPositives },
            { increment: data.pesaroeurbino.weeklyPositivesIncrement, value: data.pesaroeurbino.weeklyPositives },
            { increment: data.ascolipiceno.weeklyPositivesIncrement, value: data.ascolipiceno.weeklyPositives },
            { increment: data.fermo.weeklyPositivesIncrement, value: data.fermo.weeklyPositives }
          ]
        }
      ]
    };
  }
}

