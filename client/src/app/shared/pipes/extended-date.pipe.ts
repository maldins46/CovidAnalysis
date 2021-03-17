import { Pipe, PipeTransform } from '@angular/core';
import { DatePipe } from '@angular/common';


@Pipe({
  name: 'extendedDate'
})
export class ExtendedDatePipe extends
  DatePipe implements PipeTransform {
  transform(value: any, args?: any): any {
    return super.transform(value, 'd MMMM y, H:mm');
  }
}
