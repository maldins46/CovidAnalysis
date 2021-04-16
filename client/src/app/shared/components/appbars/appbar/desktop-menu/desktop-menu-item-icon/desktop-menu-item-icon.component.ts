import {Component, Input, OnInit} from '@angular/core';
import {MenuItem} from '../../menu-item.model';
import {ThemeService} from '../../../../../../core/theme/theme.service';

@Component({
  selector: 'app-desktop-menu-item-icon',
  templateUrl: './desktop-menu-item-icon.component.html',
  styleUrls: ['./desktop-menu-item-icon.component.scss']
})
export class DesktopMenuItemIconComponent implements OnInit {
  @Input() menuItem: MenuItem | undefined;

  isThemeDark = false;

  constructor(private readonly themeService: ThemeService) { }

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
  }
}
