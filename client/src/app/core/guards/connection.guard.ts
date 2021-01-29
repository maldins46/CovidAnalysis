import { Injectable } from '@angular/core';
import {CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router} from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ConnectionGuard implements CanActivate {
  constructor(private readonly router: Router) { }

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    if (navigator.onLine) {
      return true;
    } else {
      return this.router.parseUrl('/offline');
    }
  }
}


@Injectable({
  providedIn: 'root'
})
export class OnlineGuard implements CanActivate {
  constructor(private readonly router: Router) { }

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    if (navigator.onLine) {
      return this.router.parseUrl('/home');
    } else {
      return true;
    }
  }
}
