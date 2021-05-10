import {Component, Inject, OnInit} from '@angular/core';
import {MAT_SNACK_BAR_DATA, MatSnackBarRef} from '@angular/material/snack-bar';
import {CookieAcceptanceService} from '../../../core/cookie-acceptation/cookie-acceptance.service';

@Component({
  selector: 'app-privacy-policy-snackbar',
  templateUrl: './privacy-policy-snackbar.component.html',
  styleUrls: ['./privacy-policy-snackbar.component.scss'],
})
export class PrivacyPolicySnackbarComponent implements OnInit {

  constructor(private readonly cookieAcceptance: CookieAcceptanceService) { }

  ngOnInit(): void {}

  acceptCookies(): void {
    this.cookieAcceptance.acceptCookies();
  }
}
