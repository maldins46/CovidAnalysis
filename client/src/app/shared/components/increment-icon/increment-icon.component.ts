import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-increment-icon',
  templateUrl: './increment-icon.component.html',
  styleUrls: ['./increment-icon.component.scss']
})
export class IncrementIconComponent implements OnInit {
  @Input() posIncrement = false;
  @Input() value = 0;

  constructor() { }

  ngOnInit(): void { }

  positiveConditionSatisfied(): boolean {
    if (this.posIncrement) {
      return this.value >= 0;
    } else {
      return this.value < 0;
    }
  }
}
