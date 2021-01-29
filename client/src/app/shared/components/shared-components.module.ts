import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {AppRoutingModule} from '../../app-routing.module';
import {SharedDirectivesModule} from '../directives/shared-directives.module';
import {SharedPipesModule} from '../pipes/shared-pipes.module';
import {MaterialComponentsModule} from '../material-components/material-components.module';
import {AlertDialogComponent} from './alert-dialog/alert-dialog.component';
import {FooterComponent} from './footer/footer.component';
import {MainAppbarComponent} from './main-appbar/main-appbar.component';
import {NestedAppbarComponent} from './nested-appbar/nested-appbar.component';
import {FabComponent} from './fab/fab.component';
import {TextboxDialogComponent} from './textbox-dialog/textbox-dialog.component';
import { LastUpdateComponent } from './last-update/last-update.component';

@NgModule({
  declarations: [
    AlertDialogComponent,
    FooterComponent,
    MainAppbarComponent,
    NestedAppbarComponent,
    FabComponent,
    TextboxDialogComponent,
    LastUpdateComponent
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
    AlertDialogComponent,
    FooterComponent,
    MainAppbarComponent,
    NestedAppbarComponent,
    FabComponent,
    TextboxDialogComponent,
    LastUpdateComponent
  ]
})
export class SharedComponentsModule { }
