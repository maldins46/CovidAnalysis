import {Component, Input, OnInit} from '@angular/core';
import {MenuItem} from '../../menu-item.model';

@Component({
  selector: 'app-desktop-menu-item-text',
  templateUrl: './desktop-menu-item-text.component.html',
  styleUrls: ['./desktop-menu-item-text.component.scss']
})
export class DesktopMenuItemTextComponent implements OnInit {
  @Input() menuItem: MenuItem | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}
