import { Pipe, PipeTransform } from '@angular/core';
import { DatePipe } from '@angular/common';


@Pipe({
  name: 'extendedDate'
})
export class ExtendedDatePipe extends
  DatePipe implements PipeTransform {
  transform(value: any, args?: any): any {
    // a fix to force the timezone formatting, omitted by the Python module
    // -- Do not try this at home ! --
    const date = new Date(`${value}-0100`);
    return super.transform(date, 'd MMMM y, ore H:mm', '+0100', 'it');
  }
}
