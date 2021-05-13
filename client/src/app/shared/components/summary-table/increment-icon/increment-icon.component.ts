import {Component, Input} from '@angular/core';

@Component({
  selector: 'app-increment-icon',
  templateUrl: './increment-icon.component.html',
  styleUrls: ['./increment-icon.component.scss']
})
export class IncrementIconComponent {
  @Input() posIncrement = false;
  @Input() value = 0;

  positiveConditionSatisfied(): boolean {
    if (this.posIncrement) {
      return this.value >= 0;
    } else {
      return this.value < 0;
    }
  }
}
