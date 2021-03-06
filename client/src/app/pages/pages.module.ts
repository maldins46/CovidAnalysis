import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {SharedModule} from '../shared/shared.module';
import {AppRoutingModule} from '../app-routing.module';
import { HomeComponent } from './home/home.component';
import { VaccinesComponent } from './vaccines/vaccines.component';
import {PageNotFoundComponent} from './page-not-found/page-not-found.component';
import { OfflineComponent } from './offline/offline.component';
import { MarcheComponent } from './marche/marche.component';
import { ItalyComponent } from './italy/italy.component';
import { FeedComponent } from './feed/feed.component';
import { MarcheSummaryTableComponent } from './marche/marche-summary-table/marche-summary-table.component';
import { ItalySummaryTableComponent } from './italy/italy-summary-table/italy-summary-table.component';
import { VaccinesSummaryTableComponent } from './vaccines/vaccines-summary-table/vaccines-summary-table.component';


@NgModule({
  declarations: [
    HomeComponent,
    VaccinesComponent,
    PageNotFoundComponent,
    OfflineComponent,
    MarcheComponent,
    ItalyComponent,
    FeedComponent,
    MarcheSummaryTableComponent,
    ItalySummaryTableComponent,
    VaccinesSummaryTableComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
    AppRoutingModule,
  ],
  exports: []
})
export class PagesModule { }
