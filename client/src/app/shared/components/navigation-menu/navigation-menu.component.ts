import {Component} from '@angular/core';
import {NavigationMenuItem} from './navigation-menu-item.model';

@Component({
  selector: 'app-navigation-menu',
  templateUrl: './navigation-menu.component.html'
})
export class NavigationMenuComponent {

  menuItems: NavigationMenuItem[] = [
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
}
