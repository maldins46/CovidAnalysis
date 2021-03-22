import {Component, Input, OnInit} from '@angular/core';
import {NationalSummaryModel} from '../../../shared/models/national-summary.model';
import {VaccinesSummaryModel} from '../../../shared/models/vaccines-summary.model';

@Component({
  selector: 'app-vaccines-summary-table',
  templateUrl: './vaccines-summary-table.component.html',
  styleUrls: ['./vaccines-summary-table.component.scss']
})
export class VaccinesSummaryTableComponent implements OnInit {
  @Input() vaccinesSummary: VaccinesSummaryModel | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}
