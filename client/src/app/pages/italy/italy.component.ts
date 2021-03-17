import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../core/api/api.service';
import {NationalSummaryModel} from '../../shared/models/national-summary.model';

@Component({
  selector: 'app-italy',
  templateUrl: './italy.component.html',
  styleUrls: ['./italy.component.scss']
})
export class ItalyComponent implements OnInit {
  nationalSummary: NationalSummaryModel | undefined;

  constructor(private readonly api: ApiService) { }

  ngOnInit(): void {
    this.api.getNationalSummary().subscribe(data => { this.nationalSummary = data; });
  }
}
