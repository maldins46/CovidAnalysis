import {Component, Input, OnInit} from '@angular/core';
import {MenuItem} from '../../menu-item.model';
import {ThemeService} from '../../../../../../core/theme/theme.service';

@Component({
  selector: 'app-desktop-menu-item-text',
  templateUrl: './desktop-menu-item-text.component.html',
  styleUrls: ['./desktop-menu-item-text.component.scss']
})
export class DesktopMenuItemTextComponent implements OnInit {
  @Input() menuItem: MenuItem | undefined;
  isThemeDark = false;

  constructor(private readonly themeService: ThemeService) { }

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
  }
}
