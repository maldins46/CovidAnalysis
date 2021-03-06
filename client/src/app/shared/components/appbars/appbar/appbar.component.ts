import {Component, Input, OnInit, ViewEncapsulation} from '@angular/core';
import {MenuItem} from './menu-item.model';
import {ThemeService} from '../../../../core/theme/theme.service';

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

  constructor(private readonly themeService: ThemeService) {}

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
  }
}
