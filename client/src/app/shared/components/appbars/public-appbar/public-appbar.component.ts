import { Component, OnInit } from '@angular/core';
import {MenuItem} from '../appbar/menu-item.model';

@Component({
  selector: 'app-public-appbar',
  templateUrl: './public-appbar.component.html',
  styleUrls: ['./public-appbar.component.scss']
})
export class PublicAppbarComponent implements OnInit {

  publicMenuItems: MenuItem[] = [
    {
      name: 'Marche',
      route: '/marche',
      mdiIcon: 'marche',
      tooltip: 'Marche',
      extendedText: false
    },
    {
      name: 'Regioni',
      route: '/benchmark',
      mdiIcon: 'map-marker-multiple-outline',
      tooltip: 'Regioni',
      extendedText: false
    },
    {
      name: 'Vaccini',
      route: '/vaccines',
      mdiIcon: 'flask-outline',
      tooltip: 'Vaccini',
      extendedText: false
    },
    {
      name: 'Italia',
      route: '/italy',
      mdiIcon: 'flag-variant-outline',
      tooltip: 'Italia',
      extendedText: false
    },
    {
      name: 'Twitter feed',
      route: '/feed',
      mdiIcon: 'twitter',
      tooltip: 'Feed di Twitter',
      extendedText: false
    },
    {
      name: 'Home',
      route: '/home',
      mdiIcon: 'home-outline',
      tooltip: 'Home',
      extendedText: true
    }
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
