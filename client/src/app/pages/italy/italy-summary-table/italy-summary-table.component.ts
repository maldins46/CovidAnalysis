import {Component, Input, OnInit} from '@angular/core';
import {NationalSummaryModel} from '../../../shared/models/national-summary.model';

@Component({
  selector: 'app-italy-summary-table',
  templateUrl: './italy-summary-table.component.html',
  styleUrls: ['./italy-summary-table.component.scss']
})
export class ItalySummaryTableComponent implements OnInit {
  @Input() nationalSummary: NationalSummaryModel | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}
