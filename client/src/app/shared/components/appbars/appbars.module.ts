import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {DesktopMenuItemIconComponent} from './appbar/desktop-menu/desktop-menu-item-icon/desktop-menu-item-icon.component';
import {MaterialComponentsModule} from '../../material-components/material-components.module';
import {SharedPipesModule} from '../../pipes/shared-pipes.module';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {AppRoutingModule} from '../../../app-routing.module';
import {SharedDirectivesModule} from '../../directives/shared-directives.module';
import { DesktopMenuItemTextComponent } from './appbar/desktop-menu/desktop-menu-item-text/desktop-menu-item-text.component';
import { DesktopMenuComponent } from './appbar/desktop-menu/desktop-menu.component';
import { SmartphoneMenuComponent } from './appbar/smartphone-menu/smartphone-menu.component';
import { SmartphoneMenuItemComponent } from './appbar/smartphone-menu/smartphone-menu-item/smartphone-menu-item.component';
import { AppbarComponent } from './appbar/appbar.component';
import { PublicAppbarComponent } from './public-appbar/public-appbar.component';
import {NestedAppbarComponent} from './nested-appbar/nested-appbar.component';
import { ThemeToggleComponent } from './appbar/theme-toggle/theme-toggle.component';
import { NotificationsToggleComponent } from './appbar/notifications-toggle/notifications-toggle.component';



@NgModule({
  declarations: [
    DesktopMenuItemIconComponent,
    DesktopMenuItemTextComponent,
    DesktopMenuComponent,
    SmartphoneMenuComponent,
    SmartphoneMenuItemComponent,
    AppbarComponent,
    PublicAppbarComponent,
    NestedAppbarComponent,
    ThemeToggleComponent,
    NotificationsToggleComponent
  ],
  exports: [
    PublicAppbarComponent,
    NestedAppbarComponent
  ],
  imports: [
    CommonModule,
    MaterialComponentsModule,
    SharedPipesModule,
    ReactiveFormsModule,
    AppRoutingModule,
    SharedDirectivesModule,
    FormsModule
  ]
})
export class AppbarsModule { }
