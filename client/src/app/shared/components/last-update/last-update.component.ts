import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../../core/api/api.service';

@Component({
  selector: 'app-last-update',
  templateUrl: './last-update.component.html',
  styleUrls: ['./last-update.component.scss']
})
export class LastUpdateComponent implements OnInit {

  lastModified: Date | undefined;

  constructor() { }

  ngOnInit(): void { }

}
