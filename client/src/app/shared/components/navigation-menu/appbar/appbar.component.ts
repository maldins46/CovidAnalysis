import {Component, Input, OnInit} from '@angular/core';
import {ThemeService} from '../../../../core/theme/theme.service';
import {NavigationMenuItem} from '../navigation-menu-item.model';

@Component({
  selector: 'app-appbar',
  templateUrl: './appbar.component.html',
  styleUrls: ['./appbar.component.scss']
})
export class AppbarComponent implements OnInit {

  constructor(private readonly themeService: ThemeService) {}
  title = 'CovidAnalysis';
  logoPath = 'https://maldins46.github.io/CovidAnalysis/assets/logo-small.png';
  homeRoute = '/home';

  isThemeDark = false;

  @Input() menuItems: NavigationMenuItem[] = [];

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
  }

}
