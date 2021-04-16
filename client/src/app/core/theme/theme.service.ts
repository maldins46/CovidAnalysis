import { Injectable } from '@angular/core';
import {BehaviorSubject, Observable, Subject} from 'rxjs';
import set = Reflect.set;
import {ThemeModel} from './theme.model';

@Injectable({
  providedIn: 'root'
})
export class ThemeService {
  private themes: ThemeModel[] = [
    {
      name: 'light',
      icon: 'white-balance-sunny',
      tooltip: 'Tema chiaro',
      isDark: false
    },
    {
      name: 'dark',
      icon: 'weather-night',
      tooltip: 'Tema scuro',
      isDark: true
    },
    {
      name: 'auto',
      icon: 'theme-light-dark',
      tooltip: 'Tema di sistema',
      isDark: window.matchMedia('(prefers-color-scheme: dark)').matches
    }
  ];

  private currentThemeIndex: number;


  public themeDark: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(
    false
  );

  constructor() {
    const savedTheme = localStorage.getItem('theme');
    this.currentThemeIndex = savedTheme ? parseInt(savedTheme, 10) : 2;
    localStorage.setItem('theme', String(this.currentThemeIndex));
    this.themeDark.next(this.getCurrentTheme().isDark);
  }

  toggleTheme(): ThemeModel {
    this.currentThemeIndex = (this.currentThemeIndex + 1) % 3;
    this.themeDark.next(this.getCurrentTheme().isDark);
    localStorage.setItem('theme', String(this.currentThemeIndex));
    return this.getCurrentTheme();
  }

  getCurrentTheme(): ThemeModel {
    return this.themes[this.currentThemeIndex];
  }
}
