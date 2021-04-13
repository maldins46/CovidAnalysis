import {Component, Input, OnInit, ViewEncapsulation} from '@angular/core';

@Component({
  selector: 'app-summary-table',
  templateUrl: './summary-table.component.html',
  styleUrls: ['./summary-table.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class SummaryTableComponent implements OnInit {
  constructor() { }

  ngOnInit(): void {
  }

}
