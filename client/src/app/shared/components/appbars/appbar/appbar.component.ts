import {Component, Input, OnInit, ViewEncapsulation} from '@angular/core';
import {MenuItem} from './menu-item.model';
import {ThemeService} from '../../../../core/theme/theme.service';
import {ThemeModel} from '../../../../core/theme/theme.model';

@Component({
  selector: 'app-appbar',
  templateUrl: './appbar.component.html',
  styleUrls: ['./appbar.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class AppbarComponent implements OnInit {
  @Input() menuItems: MenuItem[] = [];
  @Input() title = 'CovidAnalysis';
  @Input() subtitle: string | undefined;
  @Input() logoPath = 'https://maldins46.github.io/CovidAnalysis/assets/logo-small.png';
  @Input() homeRoute = '/home';

  isThemeDark = false;

  theme: ThemeModel;

  constructor(private readonly themeService: ThemeService) {
    this.theme = this.themeService.getCurrentTheme();
  }

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
  }

  toggleTheme(): void {
    this.theme = this.themeService.toggleTheme();
  }
}
