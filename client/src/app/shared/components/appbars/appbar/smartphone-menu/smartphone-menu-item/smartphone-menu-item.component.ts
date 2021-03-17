import {Component, Input, OnInit} from '@angular/core';
import {MenuItem} from '../../menu-item.model';

@Component({
  selector: 'app-smartphone-menu-item',
  templateUrl: './smartphone-menu-item.component.html',
  styleUrls: ['./smartphone-menu-item.component.scss']
})
export class SmartphoneMenuItemComponent implements OnInit {
  @Input() menuItem: MenuItem | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}
