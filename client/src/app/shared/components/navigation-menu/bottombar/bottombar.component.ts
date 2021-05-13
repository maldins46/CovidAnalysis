import {Component, Input, OnInit} from '@angular/core';
import {ThemeService} from '../../../../core/theme/theme.service';
import {NavigationMenuItem} from '../navigation-menu-item.model';

@Component({
  selector: 'app-bottombar',
  templateUrl: './bottombar.component.html',
  styleUrls: ['./bottombar.component.scss']
})
export class BottombarComponent implements OnInit {
  isThemeDark = false;
  @Input() menuItems: NavigationMenuItem[] = [];

  constructor(private readonly themeService: ThemeService) {}

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
  }
}
