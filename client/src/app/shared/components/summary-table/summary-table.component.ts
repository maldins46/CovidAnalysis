import {Component, Input, OnInit, ViewEncapsulation} from '@angular/core';
import {ThemeService} from '../../../core/theme/theme.service';

@Component({
  selector: 'app-summary-table',
  templateUrl: './summary-table.component.html',
  styleUrls: ['./summary-table.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class SummaryTableComponent implements OnInit {
  isThemeDark = false;

  constructor(private readonly themeService: ThemeService) { }

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
  }
}
