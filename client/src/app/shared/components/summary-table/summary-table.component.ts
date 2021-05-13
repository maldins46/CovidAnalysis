import {Component, Input, OnInit} from '@angular/core';
import {ThemeService} from '../../../core/theme/theme.service';
import {SummaryTableModel} from './summary-table.model';

@Component({
  selector: 'app-summary-table',
  templateUrl: './summary-table.component.html',
  styleUrls: ['./summary-table.component.scss']
})
export class SummaryTableComponent implements OnInit {
  isThemeDark = false;
  @Input() summaryModel: SummaryTableModel | undefined;

  constructor(private readonly themeService: ThemeService) { }

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
  }
}
