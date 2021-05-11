import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {AppRoutingModule} from '../../app-routing.module';
import {SharedDirectivesModule} from '../directives/shared-directives.module';
import {SharedPipesModule} from '../pipes/shared-pipes.module';
import {MaterialComponentsModule} from '../material-components/material-components.module';
import {FooterComponent} from './footer/footer.component';
import { PageComponent } from './page/page.component';
import {NavigationMenuModule} from './navigation-menu/navigation-menu.module';
import { SummaryTableComponent } from './summary-table/summary-table.component';
import { IncrementIconComponent } from './summary-table/increment-icon/increment-icon.component';
import { CarouselComponent } from './carousel/carousel.component';
import { PrivacyPolicySnackbarComponent } from './privacy-policy-snackbar/privacy-policy-snackbar.component';
import {NestedAppbarComponent} from './nested-appbar/nested-appbar.component';

@NgModule({
  declarations: [
    FooterComponent,
    PageComponent,
    SummaryTableComponent,
    IncrementIconComponent,
    CarouselComponent,
    PrivacyPolicySnackbarComponent,
    NestedAppbarComponent
  ],
  imports: [
    CommonModule,
    MaterialComponentsModule,
    SharedPipesModule,
    ReactiveFormsModule,
    AppRoutingModule,
    SharedDirectivesModule,
    FormsModule,
    NavigationMenuModule
  ],
  exports: [
    FooterComponent,
    PageComponent,
    NavigationMenuModule,
    SummaryTableComponent,
    IncrementIconComponent,
    CarouselComponent,
    PrivacyPolicySnackbarComponent,
    NestedAppbarComponent
  ]
})
export class SharedComponentsModule { }
