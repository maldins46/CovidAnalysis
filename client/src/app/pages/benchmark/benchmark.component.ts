import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../core/api/api.service';
import {BenchmarkSummaryModel} from '../../shared/models/benchmark-summary.model';

@Component({
  selector: 'app-benchmark',
  templateUrl: './benchmark.component.html',
  styleUrls: ['./benchmark.component.scss']
})
export class BenchmarkComponent implements OnInit {
  benchmarkSummary: BenchmarkSummaryModel | undefined;

  constructor(private readonly api: ApiService) { }

  ngOnInit(): void {
    this.api.getBenchmarkSummary().subscribe(data => { this.benchmarkSummary = data; });
  }
}
