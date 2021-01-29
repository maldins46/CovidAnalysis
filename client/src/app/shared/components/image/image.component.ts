import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-image',
  templateUrl: './image.component.html',
  styleUrls: ['./image.component.scss']
})
export class ImageComponent implements OnInit {
  @Input() src: string | undefined;
  @Input() alt: string | undefined;

  defaultFallback = '/assets/images/fallbackImg.png';
  actualSrc: string | undefined;

  constructor() { }

  ngOnInit(): void {
    this.actualSrc = this.src ? `/CovidAnalysis/${this.src}` : this.defaultFallback;
  }

  setDefaultFallback(): void {
    this.actualSrc = this.defaultFallback;
  }

}
