import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {AppRoutingModule} from '../../app-routing.module';
import {SharedDirectivesModule} from '../directives/shared-directives.module';
import {SharedPipesModule} from '../pipes/shared-pipes.module';
import {MaterialComponentsModule} from '../material-components/material-components.module';
import {FooterComponent} from './footer/footer.component';
import { LastUpdateComponent } from './last-update/last-update.component';
import { ImageComponent } from './image/image.component';
import { PageComponent } from './page/page.component';
import { TwitterFeedComponent } from './twitter-feed/twitter-feed.component';
import {AppbarsModule} from './appbars/appbars.module';
import { SummaryTableComponent } from './summary-table/summary-table.component';
import { IncrementIconComponent } from './increment-icon/increment-icon.component';
import { CarouselComponent } from './carousel/carousel.component';

@NgModule({
  declarations: [
    FooterComponent,
    LastUpdateComponent,
    ImageComponent,
    PageComponent,
    TwitterFeedComponent,
    SummaryTableComponent,
    IncrementIconComponent,
    CarouselComponent
  ],
  imports: [
    CommonModule,
    MaterialComponentsModule,
    SharedPipesModule,
    ReactiveFormsModule,
    AppRoutingModule,
    SharedDirectivesModule,
    FormsModule,
    AppbarsModule
  ],
    exports: [
        FooterComponent,
        LastUpdateComponent,
        ImageComponent,
        PageComponent,
        TwitterFeedComponent,
        AppbarsModule,
        SummaryTableComponent,
        IncrementIconComponent,
        CarouselComponent
    ]
})
export class SharedComponentsModule { }
