import {Component} from '@angular/core';
import {CookieAcceptanceService} from '../../../core/cookie-acceptation/cookie-acceptance.service';

@Component({
  selector: 'app-privacy-policy-snackbar',
  templateUrl: './privacy-policy-snackbar.component.html',
  styleUrls: ['./privacy-policy-snackbar.component.scss'],
})
export class PrivacyPolicySnackbarComponent {
  constructor(private readonly cookieAcceptance: CookieAcceptanceService) { }

  acceptCookies(): void {
    this.cookieAcceptance.acceptCookies();
  }
}
