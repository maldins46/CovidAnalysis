import {Component, Input, OnInit} from '@angular/core';
import {MenuItem, MenuItemsUtils} from '../menu-item.model';
import {ThemeService} from '../../../../../core/theme/theme.service';

@Component({
  selector: 'app-smartphone-menu',
  templateUrl: './smartphone-menu.component.html',
  styleUrls: ['./smartphone-menu.component.scss']
})
export class SmartphoneMenuComponent implements OnInit {
  @Input() menuItems: MenuItem[] = [];
  sortedItems: MenuItem[] = [];

  isThemeDark = false;

  constructor(private readonly themeService: ThemeService) { }

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
  }
}
