import { Injectable } from '@angular/core';
import {BehaviorSubject, Observable, Subject} from 'rxjs';
import set = Reflect.set;
import {ThemeModel} from './theme.model';
import {Meta} from '@angular/platform-browser';

@Injectable({
  providedIn: 'root'
})
export class ThemeService {
  private themes: ThemeModel[] = [
    {
      name: 'light',
      icon: 'white-balance-sunny',
      tooltip: 'Tema chiaro',
      isDark: false,
      snackbar: 'Attivato il tema chiaro!'
    },
    {
      name: 'dark',
      icon: 'weather-night',
      tooltip: 'Tema scuro',
      isDark: true,
      snackbar: 'Attivato il tema scuro!'
    },
    {
      name: 'auto',
      icon: 'theme-light-dark',
      tooltip: 'Tema di sistema',
      isDark: window.matchMedia('(prefers-color-scheme: dark)').matches,
      snackbar: 'Attivato il tema automatico! Il colore del tema seguirà le impostazioni del sistema operativo!'
    }
  ];

  private currentThemeIndex: number;


  public themeDark: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(
    false
  );

  constructor(private readonly meta: Meta) {
    const savedTheme = localStorage.getItem('theme');
    this.currentThemeIndex = savedTheme ? parseInt(savedTheme, 10) : 2;
    localStorage.setItem('theme', String(this.currentThemeIndex));
    this.meta.updateTag({ name: 'theme-color', content: this.getCurrentTheme().isDark ? '#0f1216' : '#ffffff'});
    this.meta.updateTag({ name: 'color-scheme', content: this.getCurrentTheme().isDark ? 'dark' : 'light'});
    this.themeDark.next(this.getCurrentTheme().isDark);
  }

  toggleTheme(): ThemeModel {
    this.currentThemeIndex = (this.currentThemeIndex + 1) % 3;
    this.themeDark.next(this.getCurrentTheme().isDark);
    localStorage.setItem('theme', String(this.currentThemeIndex));
    this.meta.updateTag({ name: 'theme-color', content: this.getCurrentTheme().isDark ? '#0f1216' : '#ffffff'});
    return this.getCurrentTheme();
  }

  getCurrentTheme(): ThemeModel {
    return this.themes[this.currentThemeIndex];
  }
}
