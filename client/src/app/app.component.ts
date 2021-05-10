import {Component, OnInit} from '@angular/core';
import {fadeAnimation} from './shared/animations/fade.animation';
import {ThemeService} from './core/theme/theme.service';
import {MatSnackBar, MatSnackBarRef} from '@angular/material/snack-bar';
import {CookieAcceptanceService} from './core/cookie-acceptation/cookie-acceptance.service';
import {PrivacyPolicySnackbarComponent} from './shared/components/privacy-policy-snackbar/privacy-policy-snackbar.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  animations: [fadeAnimation]
})
export class AppComponent implements OnInit {
  title = 'covidanalysis';
  isThemeDark = false;
  snackbarRef: MatSnackBarRef<PrivacyPolicySnackbarComponent> | undefined;

  constructor(private readonly themeService: ThemeService,
              private readonly snackbar: MatSnackBar,
              private readonly cookieAcceptance: CookieAcceptanceService) { }

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
    this.cookieAcceptance.areCookiesAccepted.subscribe(accepted => {
      if (!accepted) {
        this.snackbarRef = this.snackbar.openFromComponent(PrivacyPolicySnackbarComponent);
      } else {
        this.snackbarRef?.dismiss();
      }
    });
  }
}
