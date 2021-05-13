import {Component, Input, OnInit} from '@angular/core';
import {NavigationMenuItem} from '../../navigation-menu-item.model';

@Component({
  selector: 'app-desktop-menu',
  templateUrl: './desktop-menu.component.html',
  styleUrls: ['./desktop-menu.component.scss']
})
export class DesktopMenuComponent implements OnInit {
  @Input() menuItems: NavigationMenuItem[] = [];
  priorityItems: NavigationMenuItem[] = [];
  iconMenuItems: NavigationMenuItem[] = [];

  ngOnInit(): void {
    this.priorityItems = this.menuItems.filter(item => item.extendedText);
    this.iconMenuItems = this.menuItems.filter(item => !item.extendedText);
  }

}
