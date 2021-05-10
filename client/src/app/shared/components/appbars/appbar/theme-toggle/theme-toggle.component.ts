import { Component, OnInit } from '@angular/core';
import {ThemeModel} from '../../../../../core/theme/theme.model';
import {ThemeService} from '../../../../../core/theme/theme.service';
import {MatSnackBar} from '@angular/material/snack-bar';

@Component({
  selector: 'app-theme-toggle',
  templateUrl: './theme-toggle.component.html',
  styleUrls: ['./theme-toggle.component.scss']
})
export class ThemeToggleComponent implements OnInit {
  isThemeDark = false;
  theme: ThemeModel;

  constructor(private readonly themeService: ThemeService, private readonly snackbar: MatSnackBar) {
    this.theme = this.themeService.getCurrentTheme();
  }

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
  }

  toggleTheme(): void {
    this.theme = this.themeService.toggleTheme();
    this.snackbar.open(this.theme.snackbar, undefined, {duration: 2000});
  }
}
