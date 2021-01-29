import {Component, Inject, OnInit} from '@angular/core';
import { MAT_DIALOG_DATA} from '@angular/material/dialog';
import {TextboxDialogData} from './textbox-dialog.model';


@Component({
  selector: 'app-alert-dialog',
  templateUrl: './textbox-dialog.component.html',
  styleUrls: ['./textbox-dialog.component.scss']
})
export class TextboxDialogComponent implements OnInit {
  inputValue = '';

  constructor(@Inject(MAT_DIALOG_DATA) public data: TextboxDialogData) {}

  ngOnInit(): void { }

}
