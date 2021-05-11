import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {DesktopMenuItemIconComponent} from './appbar/desktop-menu/desktop-menu-item-icon/desktop-menu-item-icon.component';
import {MaterialComponentsModule} from '../../material-components/material-components.module';
import {SharedPipesModule} from '../../pipes/shared-pipes.module';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {AppRoutingModule} from '../../../app-routing.module';
import {SharedDirectivesModule} from '../../directives/shared-directives.module';
import { DesktopMenuComponent } from './appbar/desktop-menu/desktop-menu.component';
import { NavigationMenuComponent } from './navigation-menu.component';
import { ThemeToggleComponent } from './appbar/theme-toggle/theme-toggle.component';
import { NotificationsToggleComponent } from './appbar/notifications-toggle/notifications-toggle.component';
import { BottombarComponent } from './bottombar/bottombar.component';
import { AppbarComponent } from './appbar/appbar.component';


@NgModule({
  declarations: [
    DesktopMenuItemIconComponent,
    DesktopMenuComponent,
    NavigationMenuComponent,
    ThemeToggleComponent,
    NotificationsToggleComponent,
    BottombarComponent,
    AppbarComponent
  ],
  exports: [
    NavigationMenuComponent,
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
export class NavigationMenuModule { }
