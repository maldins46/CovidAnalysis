import {Component, Input, OnInit, ViewEncapsulation} from '@angular/core';
import {MenuItem} from './menu-item.model';

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
  @Input() logoPath = 'https://maldins46.github.io/CovidAnalysis/assets/images/logo-small.png';
  @Input() homeRoute = '/home';

  constructor() { }

  ngOnInit(): void { }

}
