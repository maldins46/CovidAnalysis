import {Component, Input, OnInit, Output, EventEmitter} from '@angular/core';
import {Params} from '@angular/router';

/**
 * The fab used inside the app is not a standard material fab; it contains
 * a text and an icon, and it is larger and responsive.
 */

@Component({
  selector: 'app-fab',
  templateUrl: './fab.component.html',
  styleUrls: ['./fab.component.scss']
})
export class FabComponent implements OnInit {
  @Input() title = 'FabTitle';
  @Input() iconName = 'android-debug-bridge'; // used if the custom icon pack is used
  @Input() route = '/';
  @Input() backName = 'Home';
  @Input() backRoute = '/';
  @Input() additionalQueryParams: Params | undefined;
  @Input() customAction = false;
  @Output() fabClick = new EventEmitter<void>();

  queryParams: Params | undefined;

  constructor() { }

  ngOnInit(): void {
    this.queryParams = { backRoute: this.backRoute, backName: this.backName, ...this.additionalQueryParams };
  }
}
