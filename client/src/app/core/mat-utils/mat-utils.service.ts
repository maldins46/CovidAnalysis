import { Injectable } from '@angular/core';
import {MatSnackBar} from '@angular/material/snack-bar';
import {MatDialog} from '@angular/material/dialog';
import {AlertDialogData} from '../../shared/components/alert-dialog/alert-dialog.model';
import {AlertDialogComponent} from '../../shared/components/alert-dialog/alert-dialog.component';
import {TextboxDialogData} from '../../shared/components/textbox-dialog/textbox-dialog.model';
import {TextboxDialogComponent} from '../../shared/components/textbox-dialog/textbox-dialog.component';

@Injectable({
  providedIn: 'root'
})
export class MatUtilsService {

  constructor(private snackBar: MatSnackBar,
              private dialog: MatDialog) { }

  createSnackBar(content: string): void {
    this.snackBar.open(content, undefined, {duration: 4000});
  }

  createAlertDialog(alertData: AlertDialogData): void {
    this.dialog.open(AlertDialogComponent, { data: alertData });
  }

  createTextboxDialog(textboxData: TextboxDialogData): void {
    this.dialog.open(TextboxDialogComponent, { data: textboxData });
  }
}
