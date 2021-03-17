import {Component, Input, OnInit} from '@angular/core';
import {MenuItem} from '../menu-item.model';

@Component({
  selector: 'app-desktop-menu',
  templateUrl: './desktop-menu.component.html',
  styleUrls: ['./desktop-menu.component.scss']
})
export class DesktopMenuComponent implements OnInit {

  @Input() menuItems: MenuItem[] = [];
  textMenuItems: MenuItem[] = [];
  iconMenuItems: MenuItem[] = [];

  constructor() { }

  ngOnInit(): void {
    this.textMenuItems = this.menuItems.filter(item => item.extendedText);
    this.iconMenuItems = this.menuItems.filter(item => !item.extendedText);
  }

}
