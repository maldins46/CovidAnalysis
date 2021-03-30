import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../core/api/api.service';
import {MarcheSummaryModel} from '../../shared/models/marche-summary.model';
import {SlideModel} from '../../shared/models/slide.model';

@Component({
  selector: 'app-marche',
  templateUrl: './marche.component.html',
  styleUrls: ['./marche.component.scss']
})
export class MarcheComponent implements OnInit {
  marcheSummary: MarcheSummaryModel | undefined;
  incidenceSlides: SlideModel[] = [];
  absSlides: SlideModel[] = [];
  otherParamsSlides: SlideModel[] = [];

  constructor(private readonly api: ApiService) { }

  ngOnInit(): void {
    this.api.getMarcheSummary().subscribe(data => { this.marcheSummary = data; });
    this.incidenceSlides = this.api.getMarcheIncidenceSlides();
    this.absSlides = this.api.getMarcheAbsSlides();
    this.otherParamsSlides = this.api.getOtherMarcheSlides();
  }
}
