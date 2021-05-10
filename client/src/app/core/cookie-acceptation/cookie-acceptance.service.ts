import { Injectable } from '@angular/core';
import {BehaviorSubject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CookieAcceptanceService {
  public areCookiesAccepted: BehaviorSubject<boolean>;

  constructor() {
    const cookieAccept: boolean = !!localStorage.getItem('cookies-acceptation');
    this.areCookiesAccepted = new BehaviorSubject<boolean>(cookieAccept);
  }

  acceptCookies(): void {
    localStorage.setItem('cookies-acceptation', 'true');
    this.areCookiesAccepted.next(true);
  }
}
