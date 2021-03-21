import {Component, Input, OnInit} from '@angular/core';
import {BenchmarkSummaryModel} from '../../../shared/models/benchmark-summary.model';
import {MarcheSummaryModel} from '../../../shared/models/marche-summary.model';

@Component({
  selector: 'app-marche-summary-table',
  templateUrl: './marche-summary-table.component.html',
  styleUrls: ['./marche-summary-table.component.scss']
})
export class MarcheSummaryTableComponent implements OnInit {
  @Input() marcheSummary: MarcheSummaryModel | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}
