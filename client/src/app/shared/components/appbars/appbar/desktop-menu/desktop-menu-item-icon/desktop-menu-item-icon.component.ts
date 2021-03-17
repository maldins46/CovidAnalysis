import {Component, Input, OnInit} from '@angular/core';
import {MenuItem} from '../../menu-item.model';

@Component({
  selector: 'app-desktop-menu-item-icon',
  templateUrl: './desktop-menu-item-icon.component.html',
  styleUrls: ['./desktop-menu-item-icon.component.scss']
})
export class DesktopMenuItemIconComponent implements OnInit {
  @Input() menuItem: MenuItem | undefined;

  constructor() { }

  ngOnInit(): void { }

}
