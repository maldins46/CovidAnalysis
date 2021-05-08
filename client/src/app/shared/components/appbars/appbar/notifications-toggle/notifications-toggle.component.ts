import { Component, OnInit } from '@angular/core';
import {ThemeService} from '../../../../../core/theme/theme.service';
import {PushService} from '../../../../../core/notifications/push.service';
import {MatSnackBar} from '@angular/material/snack-bar';

@Component({
  selector: 'app-notifications-toggle',
  templateUrl: './notifications-toggle.component.html',
  styleUrls: ['./notifications-toggle.component.scss']
})
export class NotificationsToggleComponent implements OnInit {
  isThemeDark = false;
  areNotifsEnabled = false;
  waitingForCompletion = false;

  constructor(private readonly themeService: ThemeService,
              private readonly pushService: PushService,
              private readonly snackbar: MatSnackBar) {
  }

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
    this.pushService.notifsEnabled.subscribe(x => this.areNotifsEnabled = x);
  }

  toggleNotifications(): void {
    this.waitingForCompletion = true;
    if (this.areNotifsEnabled) {
      this.pushService.disableNotifs().then(finished => {
        this.snackbar.open('Disattivazione del servizio di notifica in corso...');
        this.waitingForCompletion = false;
        if (finished) {
          this.snackbar.open('Notifiche disattivate!', undefined, {duration: 2000});
        } else {
          this.snackbar.open(
            'C\'è stato un problema nel disattivare del servizio di notifica! Riprova più tardi.',
            undefined,
            {duration: 2000}
          );
        }
      });
    } else {
      this.snackbar.open('Consenti a CovidAnalysis di inviarti le notifiche dall\'apposito popup del browser, per attivare il servizio!');
      this.pushService.enableNotifs().then(finished => {
        this.waitingForCompletion = false;
        if (finished) {
          this.snackbar.open(
            'Notifiche attivate! Ne riceverai una ogni non appena i grafici verranno aggiornati!',
            undefined,
            {duration: 4000}
          );
        } else {
          this.snackbar.open(
            'C\'è stato un problema nell\'attivazione del servizio di notifica! Concedi manualmente il permesso al browser, ' +
            'se non lo hai fatto in precedenza. Alterimenti, riprova più tardi tramite l\'apposita voce di menù.',
            undefined,
            {duration: 4000}
          );
        }
      });
    }
  }
}
