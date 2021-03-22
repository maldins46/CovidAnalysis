import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../core/api/api.service';
import {VaccinesSummaryModel} from '../../shared/models/vaccines-summary.model';

@Component({
  selector: 'app-vaccines',
  templateUrl: './vaccines.component.html',
  styleUrls: ['./vaccines.component.scss']
})
export class VaccinesComponent implements OnInit {
  vaccinesSummary: VaccinesSummaryModel | undefined;

  constructor(private readonly api: ApiService) { }

  ngOnInit(): void {
    this.api.getVaccinesSummary().subscribe(data => { this.vaccinesSummary = data; });
  }
}
