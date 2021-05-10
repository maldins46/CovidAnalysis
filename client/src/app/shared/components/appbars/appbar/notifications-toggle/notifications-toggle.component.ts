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
              private readonly snackbar: MatSnackBar) { }

  ngOnInit(): void {
    this.themeService.themeDark.subscribe(x =>  this.isThemeDark = x);
    this.pushService.notifsEnabled.subscribe(x => this.areNotifsEnabled = x);
  }

  toggleNotifications(): void {
    this.waitingForCompletion = true;
    if (this.areNotifsEnabled) {
      this.snackbar.open('Disattivazione del servizio di notifica in corso...');
      this.pushService.disableNotifs().then(finished => {
        this.waitingForCompletion = false;
        if (finished) {
          this.snackbar.open('Notifiche disattivate!', undefined, {duration: 2000});
        } else {
          this.snackbar.open(
            'C\'è stato un problema nel disattivare il servizio di notifica! Riprova più tardi.',
            undefined,
            {duration: 4000}
          );
        }
      });
    } else {
      this.snackbar.open(
        'Attivazione del servizio di notifica in corso... Consenti la ricezione delle notifiche ' +
        'dall\'apposito popup, quando mostrato.'
      );
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
            'C\'è stato un problema nell\'attivazione del servizio :(\n' +
            'Se sei su browser Safari, purtroppo questa funzione non è supportata (per colpa di mamma Apple, non mia!).\n' +
            'Se hai in precedenza bloccato le notifiche al sito, concedi manualmente il permesso al browser.\n' +
            'Alterimenti, riprova più tardi tramite l\'apposita voce di menù.',
            undefined,
            {duration: 4000}
          );
        }
      });
    }
  }
}
