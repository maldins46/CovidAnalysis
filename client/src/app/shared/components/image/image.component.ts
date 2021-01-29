import {Component, Input, OnInit} from '@angular/core';
import {environment} from '../../../../environments/environment';

@Component({
  selector: 'app-image',
  templateUrl: './image.component.html',
  styleUrls: ['./image.component.scss']
})
export class ImageComponent implements OnInit {
  @Input() src: string | undefined;
  @Input() alt: string | undefined;

  defaultFallback =  '/CovidAnalysis/assets/fallbackImg.png';
  actualSrc: string | undefined;

  constructor() { }

  ngOnInit(): void {
    this.actualSrc = this.src ? this.src : this.defaultFallback;
  }

  setDefaultFallback(): void {
    this.actualSrc = this.defaultFallback;
  }

}
