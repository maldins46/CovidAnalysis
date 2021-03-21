import {Component, Input, OnInit} from '@angular/core';
import {BenchmarkSummaryModel} from '../../../shared/models/benchmark-summary.model';

@Component({
  selector: 'app-benchmark-summary-table',
  templateUrl: './benchmark-summary-table.component.html',
  styleUrls: ['./benchmark-summary-table.component.scss']
})
export class BenchmarkSummaryTableComponent implements OnInit {
  @Input() benchmarkSummary: BenchmarkSummaryModel | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}
