import { Injectable } from '@angular/core';
import {SwPush} from '@angular/service-worker';
import {BehaviorSubject} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {PublicKeyResponseModel} from './public-key-response.model';

@Injectable({
  providedIn: 'root'
})
export class PushService {
  constructor(private swPush: SwPush, private readonly http: HttpClient) {
    // modifies the subscription status subject on sub change
    this.swPush.subscription.subscribe(x => {
      if (x !== null) {
        this.endpoint = x.endpoint;
        this.notifsEnabled.next(true);
      } else {
        this.notifsEnabled.next(false);
      }
    });
  }

  private endpoint: string | undefined;

  public notifsEnabled: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);

  /**
   * Tries to subscribe the push notification service. It returns true if everything succeeds
   * (or the subsription is active yet), false otherwise.
   */
  public async enableNotifs(): Promise<boolean> {
    if (!this.swPush.isEnabled) {
      console.log('You are in dev mode! SW is disabled!');
      return false;
    }

    try {
      const pkRes: PublicKeyResponseModel = await this.http.get<PublicKeyResponseModel>('https://covid-analysis-server.herokuapp.com/publickey').toPromise();
      const pushSub = await this.swPush.requestSubscription({ serverPublicKey: pkRes.publicKey });
      await this.http.post('https://covid-analysis-server.herokuapp.com/subscribe', pushSub).toPromise();
      this.notifsEnabled.next(true);
      return true;

    } catch (err) {
      await this.disableNotifs();
      return false;
    }
  }

  /**
   * Tries to unsubscribe from the notification service.
   */
  public async disableNotifs(): Promise<boolean> {
    try {
      if (this.endpoint !== undefined) {
        await this.http.request('delete',
          'https://covid-analysis-server.herokuapp.com/unsubscribe',
          { body: { endpoint: this.endpoint } }
        ).toPromise();
      }
      await this.swPush.unsubscribe();
      return true;
    } catch (err) {
      console.error(err);
      return false;
    }
  }
}
