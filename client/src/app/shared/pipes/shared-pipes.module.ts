import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {ExtendedDatePipe} from './extended-date.pipe';


@NgModule({
  declarations: [
    ExtendedDatePipe
  ],
  imports: [
    CommonModule
  ],
  exports: [
    ExtendedDatePipe
  ]
})
export class SharedPipesModule { }
