import { Component, OnInit } from '@angular/core';
import {BenchmarkSummaryModel} from '../../shared/models/benchmark-summary.model';
import {ApiService} from '../../core/api/api.service';
import {MarcheSummaryModel} from '../../shared/models/marche-summary.model';

@Component({
  selector: 'app-marche',
  templateUrl: './marche.component.html',
  styleUrls: ['./marche.component.scss']
})
export class MarcheComponent implements OnInit {
  marcheSummary: MarcheSummaryModel | undefined;

  constructor(private readonly api: ApiService) { }

  ngOnInit(): void {
    this.api.getMarcheSummary().subscribe(data => { this.marcheSummary = data; });
  }
}
