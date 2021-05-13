import {Component, Input, OnInit} from '@angular/core';
import {AppbarAction} from './appbar-action.model';
import {Params} from '@angular/router';

@Component({
  selector: 'app-nested-appbar',
  templateUrl: './nested-appbar.component.html',
  styleUrls: ['./nested-appbar.component.scss']
})
export class NestedAppbarComponent {
  @Input() backRoute: string | undefined;
  @Input() backPageName: string | undefined;
  @Input() title: string | undefined;
  @Input() actions: AppbarAction[] | undefined;
  @Input() backQueryParams: Params | undefined;
}
