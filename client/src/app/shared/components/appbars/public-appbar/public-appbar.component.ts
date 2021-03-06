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
      name: 'Italia',
      route: '/italy',
      mdiIcon: 'flag-variant-outline',
      tooltip: 'Italia',
      extendedText: false
    },
    {
      name: 'Marche',
      route: '/marche',
      mdiIcon: 'marche',
      tooltip: 'Marche',
      extendedText: false
    },
    {
      name: 'Home',
      route: '/home',
      mdiIcon: 'home-outline',
      tooltip: 'Home',
      extendedText: true
    },
    {
      name: 'Vaccini',
      route: '/vaccines',
      mdiIcon: 'flask-outline',
      tooltip: 'Vaccini',
      extendedText: false
    },
    {
      name: 'Feed',
      route: '/feed',
      mdiIcon: 'twitter',
      tooltip: 'Feed di Twitter',
      extendedText: false
    }
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
