import { NgModule } from '@angular/core';
import {CommonModule} from '@angular/common';
import {MatIconModule, MatIconRegistry} from '@angular/material/icon';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatTooltipModule} from '@angular/material/tooltip';
import {DomSanitizer} from '@angular/platform-browser';
import {MatMenuModule} from '@angular/material/menu';
import {MatRippleModule} from '@angular/material/core';
import {MatSnackBarModule} from '@angular/material/snack-bar';


@NgModule({
  declarations: [ ],
  imports: [
    CommonModule,
    MatIconModule,
    MatMenuModule,
    MatToolbarModule,
    MatButtonModule,
    MatTooltipModule,
    MatRippleModule,
    MatSnackBarModule
  ],
  exports: [
    MatIconModule,
    MatMenuModule,
    MatToolbarModule,
    MatButtonModule,
    MatTooltipModule,
    MatRippleModule,
    MatSnackBarModule
  ]
})
export class MaterialComponentsModule {
  constructor(matIconRegistry: MatIconRegistry, domSanitizer: DomSanitizer){
    matIconRegistry.addSvgIconSet(
      domSanitizer.bypassSecurityTrustResourceUrl('assets/custom-icons/mdi.svg')
    );
    matIconRegistry.addSvgIcon('marche',
      domSanitizer.bypassSecurityTrustResourceUrl('assets/custom-icons/marche.svg')
    );
  }
}
