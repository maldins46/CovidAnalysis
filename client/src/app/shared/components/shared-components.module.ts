import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {AppRoutingModule} from '../../app-routing.module';
import {SharedDirectivesModule} from '../directives/shared-directives.module';
import {SharedPipesModule} from '../pipes/shared-pipes.module';
import {MaterialComponentsModule} from '../material-components/material-components.module';
import {FooterComponent} from './footer/footer.component';
import {AppbarComponent} from './appbar/appbar.component';
import { LastUpdateComponent } from './last-update/last-update.component';
import { ImageComponent } from './image/image.component';
import { PageComponent } from './page/page.component';

@NgModule({
  declarations: [
    FooterComponent,
    AppbarComponent,
    LastUpdateComponent,
    ImageComponent,
    PageComponent
  ],
  imports: [
    CommonModule,
    MaterialComponentsModule,
    SharedPipesModule,
    ReactiveFormsModule,
    AppRoutingModule,
    SharedDirectivesModule,
    FormsModule
  ],
  exports: [
    FooterComponent,
    AppbarComponent,
    LastUpdateComponent,
    ImageComponent,
    PageComponent
  ]
})
export class SharedComponentsModule { }
