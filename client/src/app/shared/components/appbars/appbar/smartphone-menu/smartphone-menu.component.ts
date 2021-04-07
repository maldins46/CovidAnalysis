import {Component, Input, OnInit} from '@angular/core';
import {MenuItem, MenuItemsUtils} from '../menu-item.model';

@Component({
  selector: 'app-smartphone-menu',
  templateUrl: './smartphone-menu.component.html',
  styleUrls: ['./smartphone-menu.component.scss']
})
export class SmartphoneMenuComponent implements OnInit {
  @Input() menuItems: MenuItem[] = [];
  sortedItems: MenuItem[] = [];

  constructor() { }

  ngOnInit(): void {
  }
}
